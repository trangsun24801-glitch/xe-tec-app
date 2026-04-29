import os
import sqlite3
import psycopg2
import requests
import re


# ===== LẤY GIÁ (KHÔNG SELENIUM) =====
def lay_gia_xang():
    url = "https://langson.petrolimex.com.vn/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(url, headers=headers, timeout=15)
        text = res.text
    except Exception as e:
        print("Lỗi request:", e)
        return {}

    lines = text.split("\n")

    data = {}

    for line in lines:
        numbers = re.findall(r"\d+\.\d+", line)

        if len(numbers) >= 2:
            name = re.sub(r"\d+\.\d+", "", line).strip()

            if "RON 95-V" in name:
                data["ron95_v"] = (name, numbers[0], numbers[1])

            elif "RON 95-III" in name:
                data["ron95_iii"] = (name, numbers[0], numbers[1])

            elif "E5" in name:
                data["e5"] = (name, numbers[0], numbers[1])

            elif "DO 0,05" in name:
                data["do005"] = (name, numbers[0], numbers[1])

            elif "DO 0,001" in name:
                data["do0001"] = (name, numbers[0], numbers[1])

            elif "Dầu hỏa" in name:
                data["dauhoa"] = (name, numbers[0], numbers[1])

    print("DATA LẤY ĐƯỢC:", data)
    return data


# ===== DB CONNECT =====
def get_conn():
    url = os.getenv("DATABASE_URL")

    # LOCAL
    if not url:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        DB_PATH = os.path.join(BASE_DIR, "xe.db")
        print("DB đang dùng:", DB_PATH)
        return sqlite3.connect(DB_PATH)

    # RENDER (PostgreSQL)
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)

    return psycopg2.connect(url)


# ===== SAVE =====
def save_price(data):
    if not data:
        print("❌ Không có dữ liệu để lưu")
        return

    conn = get_conn()
    cur = conn.cursor()

    try:
        # PostgreSQL
        cur.execute("""
            CREATE TABLE IF NOT EXISTS gia_xang (
                id SERIAL PRIMARY KEY,
                name TEXT,
                vung1 TEXT,
                vung2 TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    except:
        # SQLite
        cur.execute("""
            CREATE TABLE IF NOT EXISTS gia_xang (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                vung1 TEXT,
                vung2 TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

    cur.execute("DELETE FROM gia_xang")

    for item in data.values():
        try:
            cur.execute("""
                INSERT INTO gia_xang (name, vung1, vung2)
                VALUES (%s, %s, %s)
            """, item)
        except:
            cur.execute("""
                INSERT INTO gia_xang (name, vung1, vung2)
                VALUES (?, ?, ?)
            """, item)

    conn.commit()
    conn.close()
    print("✅ Đã lưu DB")


# ===== RUN =====
if __name__ == "__main__":
    data = lay_gia_xang()
    save_price(data)