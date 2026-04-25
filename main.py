from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()


tank_data = {
"1": [(1, 8),
(2, 24),
(3, 44),
(4, 68),
(5, 95),
(6, 125),
(7, 158),
(8, 193),
(9, 230),
(10, 269),
(11, 310),
(12, 353),
(13, 398),
(14, 446),
(15, 493),
(16, 541),
(17, 593),
(18, 645),
(19, 698),
(20, 753),
(21, 809),
(22, 867),
(23, 925),
(24, 985),
(25, 1046),
(26, 1107),
(27, 1171),
(28, 1235),
(29, 1299),
(30, 1366),
(31, 1433),
(32, 1500),
(33, 1570),
(34, 1639),
(35, 1708),
(36, 1779),
(37, 1851),
(38, 1924),
(39, 1997),
(40, 2073),
(41, 2147),
(42, 2222),
(43, 2300),
(44, 2377),
(45, 2454),
(46, 2533),
(47, 2611),
(48, 2691),
(49, 2772),
(50, 2852),
(51, 2933),
(52, 3014),
(53, 3098),
(54, 3180),
(55, 3264),
(56, 3348),
(57, 3432),
(58, 3517),
(59, 3603),
(60, 3688),
(61, 3774),
(62, 3861),
(63, 3948),
(64, 4035),
(65, 4123),
(66, 4212),
(67, 4300),
(68, 4388),
(69, 4479),
(70, 4568),
(71, 4658),
(72, 4749),
(73, 4839),
(74, 4929),
(75, 5021),
(76, 5112),
(77, 5204),
(78, 5296),
(79, 5388),
(80, 5481),
(81, 5573),
(82, 5667),
(83, 5759),
(84, 5851),
(85, 5946),
(86, 6039),
(87, 6132),
(88, 6228),
(89, 6322),
(90, 6415),
(91, 6508),
(92, 6604),
(93, 6698),
(94, 6792),
(95, 6888),
(96, 6982),
(97, 7076),
(98, 7172),
(99, 7267),
(100, 7361),
(101, 7457),
(102, 7552),
(103, 7647),
(104, 7744),
(105, 7839),
(106, 7933),
(107, 8028),
(108, 8124),
(109, 8218),
(110, 8312),
(111, 8409),
(112, 8503),
(113, 8597),
(114, 8693),
(115, 8786),
(116, 8880),
(117, 8976),
(118, 9069),
(119, 9163),
(120, 9257),
(121, 9352),
(122, 9445),
(123, 9538),
(124, 9632),
(125, 9724),
(126, 9816),
(127, 9910),
(128, 10003),
(129, 10094),
(130, 10187),
(131, 10279),
(132, 10370),
(133, 10460),
(134, 10552),
(135, 10642),
(136, 10732),
(137, 10823),
(138, 10912),
(139, 11001),
(140, 11091),
(141, 11179),
(142, 11267),
(143, 11356),
(144, 11443),
(145, 11530),
(146, 11618),
(147, 11703),
(148, 11788),
(149, 11873),
(150, 11959),
(151, 12046),
(152, 12126),
(153, 12211),
(154, 12294),
(155, 12376),
(156, 12459),
(157, 12539),
(158, 12620),
(159, 12701),
(160, 12781),
(161, 12859),
(162, 12936),
(163, 13015),
(164, 13092),
(165, 13168),
(166, 13245),
(167, 13319),
(168, 13393),
(169, 13468),
(170, 13541),
(171, 13612),
(172, 13684),
(173, 13754),
(174, 13823),
(175, 13891),
(176, 13960),
(177, 14026),
(178, 14092),
(179, 14158),
(180, 14221),
(181, 14284),
(182, 14347),
(183, 14408),
(184, 14467),
(185, 14526),
(186, 14584),
(187, 14640),
(188, 14694),
(189, 14748),
(190, 14800),
(191, 14851),
(192, 14901),
(193, 14948),
(194, 14955),
(195, 15041),
(196, 15084),
(197, 15124),
(198, 15164),
(199, 15201),
(200, 15236),
(201, 15270),
(202, 15300),
(203, 15327),
(204, 15351),
(205, 15372),
(206, 15388),
(207, 15397),
        # (H, V)
        ],
        "2": [(1, 9),
        (2, 25),
        (3, 45),
        (4, 70),
        (5, 97),
        (6, 127),
        (7, 161),
        (8, 196),
        (9, 233),
        (10, 273),
        (11, 314),
        (12, 357),
        (13, 402),
        (14, 450),
        (15, 497),
        (16, 546),
        (17, 598),
        (18, 650),
        (19, 703),
        (20, 759),
        (21, 815),
        (22, 873),
        (23, 932),
        (24, 991),
        (25, 1053),
        (26, 1115),
        (27, 1179),
        (28, 1243),
        (29, 1307),
        (30, 1375),
        (31, 1441),
        (32, 1509),
        (33, 1579),
        (34, 1648),
        (35, 1718),
        (36, 1791),
        (37, 1862),
        (38, 1936),
        (39, 2009),
        (40, 2084),
        (41, 2159),
        (42, 2235),
        (43, 2313),
        (44, 2390),
        (45, 2467),
        (46, 2547),
        (47, 2625),
        (48, 2705),
        (49, 2787),
        (50, 2868),
        (51, 2948),
        (52, 3030),
        (53, 3114),
        (54, 3197),
        (55, 3281),
        (56, 3366),
        (57, 3451),
        (58, 3535),
        (59, 3622),
        (60, 3708),
        (61, 3794),
        (62, 3881),
        (63, 3969),
        (64, 4056),
        (65, 4146),
        (66, 4234),
        (67, 4322),
        (68, 4411),
        (69, 4502),
        (70, 4592),
        (71, 4682),
        (72, 4774),
        (73, 4865),
        (74, 4955),
        (75, 5048),
        (76, 5138),
        (77, 5231),
        (78, 5325),
        (79, 5416),
        (80, 5509),
        (81, 5602),
        (82, 5696),
        (83, 5789),
        (84, 5881),
        (85, 5977),
        (86, 6070),
        (87, 6164),
        (88, 6260),
        (89, 6354),
        (90, 6448),
        (91, 6544),
        (92, 6639),
        (93, 6732),
        (94, 6827),
        (95, 6924),
        (96, 7018),
        (97, 7113),
        (98, 7210),
        (99, 7304),
        (100, 7399),
        (101, 7496),
        (102, 7591),
        (103, 7687),
        (104, 7784),
        (105, 7879),
        (106, 7974),
        (107, 8071),
        (108, 8166),
        (109, 8261),
        (110, 8355),
        (111, 8452),
        (112, 8546),
        (113, 8641),
        (114, 8738),
        (115, 8832),
        (116, 8926),
        (117, 9022),
        (118, 9116),
        (119, 9210),
        (120, 9306),
        (121, 9400),
        (122, 9493),
        (123, 9587),
        (124, 9681),
        (125, 9774),
        (126, 9866),
        (127, 9961),
        (128, 10054),
        (129, 10145),
        (130, 10239),
        (131, 10331),
        (132, 10422),
        (133, 10515),
        (134, 10605),
        (135, 10696),
        (136, 10786),
        (137, 10878),
        (138, 10967),
        (139, 11057),
        (140, 11147),
        (141, 11235),
        (142, 11324),
        (143, 11413),
        (144, 11501),
        (145, 11589),
        (146, 11676),
        (147, 11762),
        (148, 11847),
        (149, 11933),
        (150, 12019),
        (151, 12104),
        (152, 12187),
        (153, 12272),
        (154, 12355),
        (155, 12437),
        (156, 12521),
        (157, 12602),
        (158, 12682),
        (159, 12764),
        (160, 12844),
        (161, 12922),
        (162, 13002),
        (163, 13079),
        (164, 13156),
        (165, 13233),
        (166, 13310),
        (167, 13384),
        (168, 13458),
        (169, 13533),
        (170, 13607),
        (171, 13678),
        (172, 13750),
        (173, 13820),
        (174, 13890),
        (175, 13959),
        (176, 14027),
        (177, 14094),
        (178, 14160),
        (179, 14225),
        (180, 14289),
        (181, 14352),
        (182, 14415),
        (183, 14476),
        (184, 14536),
        (185, 14595),
        (186, 14653),
        (187, 14709),
        (188, 14764),
        (189, 14817),
        (190, 14869),
        (191, 14920),
        (192, 14970),
        (193, 15017),
        (194, 15064),
        (195, 15110),
        (196, 15153),
        (197, 15194),
        (198, 15234),
        (199, 15271),
        (200, 15305),
        (201, 15339),
        (202, 15369),
        (203, 15396),
        (204, 15420),
        (205, 15440),
        (206, 15456),
        ],
        "3": [(1,11),(2,30),(3,56),(4,86),(5,119),(6,157),(7,197),(8,241),(9,287),(10,336),
        (11,387),(12,440),(13,496),(14,553),(15,613),(16,674),(17,737),(18,802),(19,869),(20,937),
        (21,1007),(22,1079),(23,1152),(24,1226),(25,1302),(26,1379),(27,1457),(28,1537),(29,1618),(30,1700),
        (31,1783),(32,1868),(33,1954),(34,2040),(35,2128),(36,2217),(37,2307),(38,2398),(39,2490),(40,2583),

        (41,2677),(42,2772),(43,2867),(44,2964),(45,3061),(46,3160),(47,3259),(48,3359),(49,3459),(50,3561),
        (51,3663),(52,3766),(53,3870),(54,3974),(55,4080),(56,4185),(57,4292),(58,4399),(59,4507),(60,4616),
        (61,4725),(62,4834),(63,4945),(64,5056),(65,5167),(66,5279),(67,5392),(68,5505),(69,5618),(70,5733),
        (71,5847),(72,5962),(73,6078),(74,6194),(75,6310),(76,6427),(77,6545),(78,6663),(79,6781),(80,6899),

        (81,7019),(82,7138),(83,7258),(84,7378),(85,7498),(86,7619),(87,7740),(88,7862),(89,7984),(90,8106),
        (91,8228),(92,8351),(93,8474),(94,8597),(95,8721),(96,8845),(97,8969),(98,9093),(99,9217),(100,9342),
        (101,9467),(102,9592),(103,9717),(104,9843),(105,9968),(106,10094),(107,10220),(108,10346),(109,10473),(110,10599),
        (111,10725),(112,10852),(113,10979),(114,11106),(115,11233),(116,11360),(117,11487),(118,11614),(119,11741),(120,11868),(121,11996),(122,12123),(123,12250),(124,12378),(125,12505),(126,12632),(127,12760),(128,12887),(129,13014),(130,13142),
        (131,13269),(132,13396),(133,13523),(134,13650),(135,13777),(136,13904),(137,14031),(138,14158),(139,14285),(140,14411),
        (141,14537),(142,14664),(143,14790),(144,14916),(145,15042),(146,15167),(147,15293),(148,15418),(149,15543),(150,15668),
        (151,15793),(152,15917),(153,16041),(154,16165),(155,16289),(156,16413),(157,16536),(158,16659),(159,16782),(160,16904),

        (161,17026),(162,17148),(163,17270),(164,17391),(165,17512),(166,17632),(167,17752),(168,17872),(169,17992),(170,18111),
        (171,18229),(172,18347),(173,18465),(174,18583),(175,18700),(176,18816),(177,18932),(178,19048),(179,19163),(180,19278),
        (181,19392),(182,19505),(183,19618),(184,19731),(185,19843),(186,19954),(187,20065),(188,20176),(189,20285),(190,20394),
        (191,20503),(192,20611),(193,20718),(194,20825),(195,20930),(196,21036),(197,21140),(198,21244),(199,21347),(200,21449),

        (201,21551),(202,21651),(203,21751),(204,21850),(205,21949),(206,22046),(207,22143),(208,22238),(209,22333),(210,22427),
        (211,22520),(212,22612),(213,22703),(214,22793),(215,22882),(216,22970),(217,23056),(218,23142),(219,23227),(220,23310),
        (221,23392),(222,23473),(223,23553),(224,23631),(225,23708),(226,23784),(227,23858),(228,23931),(229,24003),(230,24073),
        (231,24141),(232,24208),(233,24273),(234,24336),(235,24397),(236,24457),(237,24514),(238,24570),(239,24623),(240,24674),
        ]
        }

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import psycopg2
import os
import json

def get_conn():
    url = os.getenv("DATABASE_URL")
    if not url:
        raise Exception("❌ DATABASE_URL chưa được set!")
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    return psycopg2.connect(url)


def init_db():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS xe (
        ten_xe TEXT PRIMARY KEY,
        h1 REAL, h2 REAL, h3 REAL, h4 REAL, h5 REAL,
        t1_xe REAL, t2_xe REAL, t3_xe REAL, t4_xe REAL, t5_xe REAL
    )
    """)

    conn.commit()
    conn.close()


init_db()


# ===== HÀM =====
def h_to_v(h, table):
    for i in range(len(table) - 1):
        h1, v1 = table[i]
        h2, v2 = table[i+1]
        if h1 <= h <= h2:
            return v1 + (h - h1)*(v2 - v1)/(h2 - h1)
    return None


def v_to_h(v, table):
    for i in range(len(table) - 1):
        h1, v1 = table[i]
        h2, v2 = table[i+1]
        if v1 <= v <= v2:
            return h1 + (v - v1)*(h2 - h1)/(v2 - v1)
    return None
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
    <style>
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            font-family: Arial;
            color: white;
            text-align: center;
            padding-top: 80px;
        }

        h1 {
            font-size: 42px;
            margin-bottom: 40px;
        }

        .card {
            display: inline-block;
            width: 220px;
            padding: 25px;
            margin: 15px;
            border-radius: 15px;
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            text-decoration: none;
            color: white;
            transition: 0.3s;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
        }

        .card:hover {
            transform: translateY(-8px);
            box-shadow: 0 0 30px rgba(0,255,150,0.4);
        }

        .icon {
            font-size: 40px;
            margin-bottom: 10px;
        }

        .title {
            font-size: 20px;
            margin-bottom: 5px;
        }

        .desc {
            font-size: 13px;
            opacity: 0.7;
        }
    </style>
    </head>

    <body>

    <h1>🚀 Hệ thống quản lý xăng dầu</h1>

    <a href="/nhap-xe-tec" class="card">
        <div class="icon">🚛</div>
        <div class="title">Nhập xe téc</div>
        <div class="desc">Quản lý & tính toán xe nhập</div>
    </a>

    <a href="/quy-doi" class="card">
        <div class="icon">⛽</div>
        <div class="title">Quy đổi</div>
        <div class="desc">Chiều cao ↔ Thể tích</div>
    </a>

    </body>
    </html>
    """


# ===== GIAO DIỆN =====
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse



@app.get("/quy-doi", response_class=HTMLResponse)
def quy_doi():
    return """
    <html>
    <head>
    <style>
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            font-family: Arial;
            color: white;
            text-align: center;
            padding-top: 50px;
        }

        .card {
            display: inline-block;
            padding: 30px;
            border-radius: 15px;
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
            width: 300px;
        }

        h1 {
            margin-bottom: 20px;
        }

        select, input {
            width: 90%;
            padding: 8px;
            margin: 10px 0;
            border-radius: 8px;
            border: none;
            text-align: center;
        }

        button {
            padding: 10px 20px;
            border: none;
            border-radius: 10px;
            background: #00c6ff;
            color: white;
            cursor: pointer;
            margin-top: 15px;
        }

        button:hover {
            background: #0072ff;
        }

        .back {
            display: block;
            margin-top: 20px;
            color: orange;
            text-decoration: none;
        }

        .back:hover {
            text-decoration: underline;
        }

        .label {
            margin-top: 10px;
            font-weight: bold;
        }
    </style>
    </head>

    <body>

    <div class="card">
        <h1>⛽ Quy đổi</h1>

        <form action="/convert" method="post">

            <select name="mode">
                <option value="h_to_v">Chiều cao → Thể tích</option>
                <option value="v_to_h">Thể tích → Chiều cao</option>
            </select>

            <div class="label">Bể DO 0,05</div>
            <input name="value1" placeholder="Nhập giá trị...">

            <div class="label">Bể A95</div>
            <input name="value2" placeholder="Nhập giá trị...">

            <div class="label">Bể DO 0,001</div>
            <input name="value3" placeholder="Nhập giá trị...">

            <button type="submit">Tính</button>

        </form>

        <a href="/" class="back">← Trang chính</a>
    </div>

    </body>
    </html>
    """

@app.post("/convert", response_class=HTMLResponse)
def convert(
    mode: str = Form(...),
    value1: float = Form(0),
    value2: float = Form(0),
    value3: float = Form(0),
):
    table1 = tank_data["1"]
    table2 = tank_data["2"]
    table3 = tank_data["3"]

    if mode == "h_to_v":
        kq1 = h_to_v(value1, table1)
        kq2 = h_to_v(value2, table2)
        kq3 = h_to_v(value3, table3)
    else:
        kq1 = v_to_h(value1, table1)
        kq2 = v_to_h(value2, table2)
        kq3 = v_to_h(value3, table3)

    return f"""
    
        <html>
        <head>
        <style>
            body {{
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                font-family: Arial;
                color: white;
                text-align: center;
                padding-top: 60px;
            }}

            .card {{
                display: inline-block;
                padding: 30px;
                border-radius: 15px;
                background: rgba(255,255,255,0.05);
                backdrop-filter: blur(10px);
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }}

            h1 {{
                margin-bottom: 25px;
            }}

            p {{
                font-size: 18px;
                        margin: 10px 0;
                    }}

            .back {{
                display: inline-block;
                margin-top: 20px;
                color: orange;
                text-decoration: none;
            }}

            .back:hover {{
                text-decoration: underline;
            }}
        </style>
        </head>

        <body>

        <div class="card">
            <h1>⛽ Kết quả quy đổi</h1>

            <p>Bể DO 0,05: {kq1:.2f} {"lít" if mode == "h_to_v" else "cm"}</p>
            <p>Bể A95: {kq2:.2f} {"lít" if mode == "h_to_v" else "cm"}</p>
            <p>Bể DO 0,001: {kq3:.2f} {"lít" if mode == "h_to_v" else "cm"}</p>

            <a href="/quy-doi" class="back">← Quay lại</a>
        </div>

        </body>
        </html>
        """

from fastapi import Request
@app.api_route("/nhap-xe-tec", methods=["GET","POST"], response_class=HTMLResponse)
async def xe_tec(request: Request):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM xe")
    rows = cursor.fetchall()

    conn.close()
    ket_qua_html = ""
    form_data = {}
    if request.method == "POST":
        
        form = await request.form()
        form_data = dict(form)
        print("TEN XE:", form_data.get("ten_xe"))

        def get_float(name):
            val = form.get(name)
            return float(val) if val not in [None, ""] else 0

        t1_xe = get_float("t1_xe")
        t1_ch = get_float("t1_ch")
        h1 = get_float("h1")
        t1_du = get_float("t1_du")
        t2_xe = get_float("t2_xe"); t2_ch = get_float("t2_ch"); h2 = get_float("h2"); t2_du = get_float("t2_du")
        t3_xe = get_float("t3_xe"); t3_ch = get_float("t3_ch"); h3 = get_float("h3"); t3_du = get_float("t3_du")
        t4_xe = get_float("t4_xe"); t4_ch = get_float("t4_ch"); h4 = get_float("h4"); t4_du = get_float("t4_du")
        t5_xe = get_float("t5_xe"); t5_ch = get_float("t5_ch"); h5 = get_float("h5"); t5_du = get_float("t5_du")
        fuel1 = form.get("fuel1")
        fuel2 = form.get("fuel2")
        fuel3 = form.get("fuel3")
        fuel4 = form.get("fuel4")
        fuel5 = form.get("fuel5")
        # ===== SỐ LƯỢNG =====
        sl_a95 = get_float("sl_a95")
        sl_do005 = get_float("sl_do005")
        sl_do0001 = get_float("sl_do0001")

        # ===== NHIỆT ĐỘ HÓA ĐƠN =====
        temp_hd_a95 = get_float("temp_hd_a95")
        temp_hd_do005 = get_float("temp_hd_do005")
        temp_hd_do0001 = get_float("temp_hd_do0001")

        # ===== NHIỆT ĐỘ CỬA HÀNG =====
        temp_ch_a95 = get_float("temp_ch_a95")
        temp_ch_do005 = get_float("temp_ch_do005")
        temp_ch_do0001 = get_float("temp_ch_do0001")

        # ===== QUÃNG ĐƯỜNG =====
        distance = get_float("distance")

        # ===== TÍNH TOÁN =====
        def tinh(xe, ch, h):
            if xe == 0 and ch == 0 and h == 0:
                return 0
            return (xe - ch) * h

        k1 = tinh(t1_xe, t1_ch, h1)
        k2 = tinh(t2_xe, t2_ch, h2)
        k3 = tinh(t3_xe, t3_ch, h3)
        k4 = tinh(t4_xe, t4_ch, h4)
        k5 = tinh(t5_xe, t5_ch, h5)

        du1 = t1_du * h1
        du2 = t2_du * h2
        du3 = t3_du * h3
        du4 = t4_du * h4
        du5 = t5_du * h5

        k1_real = k1 - du1
        k2_real = k2 - du2
        k3_real = k3 - du3
        k4_real = k4 - du4
        k5_real = k5 - du5

        A95 = 0
        DO005 = 0
        DO0001 = 0

        def cong(fuel, val):
            nonlocal A95, DO005, DO0001
            if fuel == "a95":
                A95 += val
            elif fuel == "do005":
                DO005 += val
            else:
                DO0001 += val

        cong(fuel1, k1_real)
        cong(fuel2, k2_real)
        cong(fuel3, k3_real)
        cong(fuel4, k4_real)
        cong(fuel5, k5_real)

        # ===== CHÊNH NHIỆT =====
        chenh_a95 = (temp_ch_a95 - temp_hd_a95) * sl_a95 * 0.0013
        chenh_do005 = (temp_ch_do005 - temp_hd_do005) * sl_do005 * 0.0009
        chenh_do0001 = (temp_ch_do0001 - temp_hd_do0001) * sl_do0001 * 0.0009

        # ===== HAO HỤT =====
        hao_a95 = distance * sl_a95 * 0.000005
        hao_do005 = distance * sl_do005 * 0.000003
        hao_do0001 = distance * sl_do0001 * 0.000003

        # ===== FINAL =====
        final_a95 = A95 - chenh_a95 + hao_a95
        final_do005 = DO005 - chenh_do005 + hao_do005
        final_do0001 = DO0001 - chenh_do0001 + hao_do0001
        ket_qua_html = f"""
        <div style="margin-top:30px;padding:20px;background:#222;border-radius:10px;">
        <h2>📊 KẾT LUẬN</h2>

        <h3 style="color:{'lime' if final_a95 > 0 else 'red' if final_a95 < 0 else 'orange'}">
        A95: {final_a95:.2f} ({ "THỪA" if final_a95 > 0 else "THIẾU" if final_a95 < 0 else "CHUẨN" })
        </h3>

        <h3 style="color:{'lime' if final_do005 > 0 else 'red' if final_do005 < 0 else 'orange'}">
        DO 0.05: {final_do005:.2f}
        </h3>

        <h3 style="color:{'lime' if final_do0001 > 0 else 'red' if final_do0001 < 0 else 'orange'}">
        DO 0.001: {final_do0001:.2f}
        </h3>
        </div>
        """

    du_lieu_xe = {}
    options = ""

    for row in rows:
        ten = row[0]

        du_lieu_xe[ten] = {
            "h1": row[1], "h2": row[2], "h3": row[3],
            "h4": row[4], "h5": row[5],
            "t1_xe": row[6], "t2_xe": row[7],
            "t3_xe": row[8], "t4_xe": row[9],
            "t5_xe": row[10],
        }

        selected = "selected" if form_data.get("ten_xe") == ten else ""
        options += f'<option value="{ten}" {selected}>{ten}</option>'

    return f"""
    <html>
   <body style="
    background:#111;
    font-family:Arial;
    ">
    <div style="
    display:flex;
    justify-content:center;
    gap:10px;
    align-items:flex-start;
    padding-top:1px;
    ">
    <div style="background:#1c1c1c;padding:10px;border-radius:8px;width:600px;color:white;margin-top:0px;box-shadow:0 0 20px rgba(0,0,0,0.5);">
    

    <h1 style="margin:0 0 5px 0;">🚛 Nhập xe téc</h1>
    <div style="margin-bottom:5px;">
    <a href="/them-xe" style="color:lime;margin-right:15px;">➕ Thêm xe</a>
    
    <a id="xoaLink" href="#" style="color:red;"
    onclick="return confirm('Xóa xe này?')">🗑 Xóa</a>
    </div>
    
    
    
    <script>
    const duLieuXe = {json.dumps(du_lieu_xe)};

    // 👇 biến chặn không cho chạy lại sau khi POST
    let daSubmit = false;

    function chonXe(xe) {{
        // ❌ nếu vừa submit xong thì không auto fill nữa
        if (daSubmit) return;

        const data = duLieuXe[xe];
        if (!data) return;

        for (let key in data) {{
            let input = document.getElementsByName(key)[0];

            // 👇 chỉ fill khi ô trống
            if (input && input.value === "") {{
                input.value = data[key];
            }}
        }}

        document.getElementById("xoaLink").href = "/xoa-xe?ten=" + xe;
    }}
    </script>
        

    
   

    <form action="/nhap-xe-tec" method="post" onsubmit="daSubmit = true;">
    <h2 style="margin:0 0 5px 0;">🚛 Chọn xe</h2>
    <select name="ten_xe" onchange="chonXe(this.value)">
    <option value="">-- Chọn xe --</option>
    {options}
    </select>

    <h3>Khoang 1</h3>
    <div style="display:flex; gap:10px; justify-content:center; margin-bottom:10px;">

    <input name="t1_xe"value="{form_data.get('t1_xe','')}" placeholder="Barem" style="width:80px">
    <input name="t1_ch"value="{form_data.get('t1_ch','')}" placeholder="CH Đo" style="width:80px">
    <input name="h1"value="{form_data.get('h1','')}" placeholder="Lít/Cm" style="width:80px">
    <input name="t1_du"value="{form_data.get('t1_du','')}" placeholder="Dư Hóa Đơn" style="width:85px">

    <select name="fuel1">
    <option value="a95" {"selected" if form_data.get("fuel1")=="a95" else ""}>A95</option>
    <option value="do005" {"selected" if form_data.get("fuel1")=="do005" else ""}>DO 0.05</option>
    <option value="do0001" {"selected" if form_data.get("fuel1")=="do0001" else ""}>DO 0.001</option>
    </select>
    </div>
    

    <h3>Khoang 2</h3>
    <div style="display:flex; gap:10px; justify-content:center; margin-bottom:10px;">

    <input name="t2_xe"value="{form_data.get('t2_xe','')}" placeholder="Barem" style="width:80px">
    <input name="t2_ch"value="{form_data.get('t2_ch','')}" placeholder="CH Đo" style="width:80px">
    <input name="h2" value="{form_data.get('h2','')}"placeholder="Lít/Cm" style="width:80px">
    <input name="t2_du"value="{form_data.get('t2_du','')}" placeholder="Dư Hóa Đơn" style="width:85px">

    <select name="fuel2">
       <option value="a95" {"selected" if form_data.get("fuel2")=="a95" else ""}>A95</option>
    <option value="do005" {"selected" if form_data.get("fuel2")=="do005" else ""}>DO 0.05</option>
    <option value="do0001" {"selected" if form_data.get("fuel2")=="do0001" else ""}>DO 0.001</option>
    </select>

</div>

    <h3>Khoang 3</h3>
    <div style="display:flex; gap:10px; justify-content:center; margin-bottom:10px;">

    <input name="t3_xe"value="{form_data.get('t3_xe','')}" placeholder="Barem" style="width:80px">
    <input name="t3_ch"value="{form_data.get('t3_ch','')}" placeholder="CH Đo" style="width:80px">
    <input name="h3"value="{form_data.get('h3','')}" placeholder="Lít/Cm" style="width:80px">
    <input name="t3_du"value="{form_data.get('t3_du','')}" placeholder="Dư Hóa Đơn" style="width:85px">

    <select name="fuel3">
        <option value="a95" {"selected" if form_data.get("fuel3")=="a95" else ""}>A95</option>
    <option value="do005" {"selected" if form_data.get("fuel3")=="do005" else ""}>DO 0.05</option>
    <option value="do0001" {"selected" if form_data.get("fuel3")=="do0001" else ""}>DO 0.001</option>
    </select>

</div>

    <h3>Khoang 4</h3>
    <div style="display:flex; gap:10px; justify-content:center; margin-bottom:10px;">

    <input name="t4_xe"value="{form_data.get('t4_xe','')}" placeholder="Barem" style="width:80px">
    <input name="t4_ch"value="{form_data.get('t4_ch','')}" placeholder="CH Đo" style="width:80px">
    <input name="h4"value="{form_data.get('h4','')}"placeholder="Lít/Cm" style="width:80px">
    <input name="t4_du"value="{form_data.get('t4_du','')}" placeholder="Dư Hóa Đơn" style="width:85px">

    <select name="fuel4">
       <option value="a95" {"selected" if form_data.get("fuel4")=="a95" else ""}>A95</option>
    <option value="do005" {"selected" if form_data.get("fuel4")=="do005" else ""}>DO 0.05</option>
    <option value="do0001" {"selected" if form_data.get("fuel4")=="do0001" else ""}>DO 0.001</option>
    </select>

</div>
    <h3>Khoang 5</h3>
    <div style="display:flex; gap:10px; justify-content:center; margin-bottom:10px;">

    <input name="t5_xe"value="{form_data.get('t5_xe','')}" placeholder="Barem" style="width:80px">
    <input name="t5_ch"value="{form_data.get('t5_ch','')}" placeholder="CH Đo" style="width:80px">
    <input name="h5"value="{form_data.get('h5','')}" placeholder="Lít/Cm" style="width:80px">
    <input name="t5_du"value="{form_data.get('t5_du','')}" placeholder="Dư Hóa Đơn" style="width:85px">

    <select name="fuel5">
        <option value="a95" {"selected" if form_data.get("fuel5")=="a95" else ""}>A95</option>
    <option value="do005" {"selected" if form_data.get("fuel5")=="do005" else ""}>DO 0.05</option>
    <option value="do0001" {"selected" if form_data.get("fuel5")=="do0001" else ""}>DO 0.001</option>
    </select>

</div>
    <h2 style="margin-top:5px;">📦 Số lượng hàng trên hóa đơn</h2>
    <span style="color:red;">A95:</span><input name="sl_a95"value="{form_data.get('sl_a95','')}" style="width:20%;padding:4px;margin-bottom:4px;">
    <span style="color:#00bfff;">DO 0.05:</span><input name="sl_do005"value="{form_data.get('sl_do005','')}"style="width:20%;padding:4px;margin-bottom:4px;">
    <span style="color:#7CFC00;">DO 0.001:</span><input name="sl_do0001"value="{form_data.get('sl_do0001','')}"style="width:20%;padding:4px;margin-bottom:4px;">

   <h2 style="margin-top:5px;">🌡️ Nhiệt độ trên hóa đơn</h2>
    <span style="color:red;">A95:</span><input name="temp_hd_a95"value="{form_data.get('temp_hd_a95','')}"style="width:7%;padding:2px;margin-bottom:2px;">
    <span style="color:#00bfff;">DO 0.05:</span><input name="temp_hd_do005"value="{form_data.get('temp_hd_do005','')}"style="width:7%;padding:2px;margin-bottom:2px;">
    <span style="color:#7CFC00;">DO 0.001:</span><input name="temp_hd_do0001"value="{form_data.get('temp_hd_do0001','')}"style="width:7%;padding:2px;margin-bottom:2px;">

   <h2 style="margin-top:5px;">🌡️ Nhiệt độ đo tại cửa hàng </h2>
    <span style="color:red;">A95:</span><input name="temp_ch_a95"value="{form_data.get('temp_ch_a95','')}"style="width:7%;padding:2px;margin-bottom:2px;">
    <span style="color:#00bfff;">DO 0.05:</span><input name="temp_ch_do005"value="{form_data.get('temp_ch_do005','')}"style="width:7%;padding:2px;margin-bottom:2px;">
    <span style="color:#7CFC00;">DO 0.001:</span><input name="temp_ch_do0001"value="{form_data.get('temp_ch_do0001','')}"style="width:7%;padding:2px;margin-bottom:2px;">
    <h2 style="margin-top:5px;">🚚 Quãng đường vận chuyển (km)</h2>
    <input name="distance" value="{form_data.get('distance','')}"placeholder="Nhập km"style="width:12%;padding:4px;margin-bottom:4px;"><br>
    <button type="submit">Tính</button>

    </form>
    
    </div>
    <div style="
    background:#1c1c1c;
    padding:20px;
    border-radius:12px;
    width:300px;
    color:white;
    box-shadow:0 0 20px rgba(0,0,0,0.5);
    ">
    {ket_qua_html}
    </div>
    
    <br>
    <a href="/" style="color:orange">← Trang chính</a>
    <script>
    function chonXe(xe) {{
    const data = duLieuXe[xe];
    if (!data) return;

    for (let key in data) {{
        let input = document.getElementsByName(key)[0];
        if (input) input.value = data[key];
    }}

    // 👉 cập nhật link xóa
    document.getElementById("xoaLink").href = "/xoa-xe?ten=" + xe;
    }}
    

    </script>
    
    </div>
    </body>
    </html>
    """
@app.get("/xoa-xe", response_class=HTMLResponse)
def xoa_xe(ten: str):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM xe WHERE ten_xe=%s", (ten,))

    conn.commit()
    conn.close()

    return """
    <html>
    <head>
    <meta http-equiv="refresh" content="1;url=/nhap-xe-tec">
    </head>
    <body style="background:#111;color:white;text-align:center;padding-top:80px;font-family:Arial">
    <h1 style="color:red">🗑 Đã xóa xe!</h1>
    <p>Đang quay lại...</p>
    </body>
    </html>
    """
@app.get("/them-xe", response_class=HTMLResponse)
def form_them_xe():
    return """
    <html>
    <body style="background:#111;color:white;text-align:center;padding-top:40px;font-family:Arial">

    <h1>➕ Thêm xe</h1>

    <form action="/luu-xe" method="post">

    <input name="ten_xe" placeholder="Biển số"><br><br>

    <h3>Tấm mức</h3>
    <input name="t1_xe" placeholder="Khoang 1 ( VD: 40.5)">
    <input name="t2_xe" placeholder="Khoang 2">
    <input name="t3_xe" placeholder="Khoang 3">
    <input name="t4_xe" placeholder="Khoang 4">
    <input name="t5_xe" placeholder="Khoang 5"><br><br>
    <h3>Cm/Lít</h3>
    <input name="h1" placeholder=" Khoang 1 (VD: 6.3) ">
    <input name="h2" placeholder="Khoang 2">
    <input name="h3" placeholder="Khoang 3">
    <input name="h4" placeholder="Khoang 4">
    <input name="h5" placeholder="Khoang 5"><br><br>

    <button type="submit">Lưu</button>

    </form>

    <br>
    <a href="/nhap-xe-tec" style="color:orange">← Quay lại</a>

    </body>
    </html>
    """
@app.post("/luu-xe", response_class=HTMLResponse)
def luu_xe(
    ten_xe: str = Form(...),
    h1: float = Form(0), h2: float = Form(0), h3: float = Form(0),
    h4: float = Form(0), h5: float = Form(0),
    t1_xe: float = Form(0), t2_xe: float = Form(0), t3_xe: float = Form(0),
    t4_xe: float = Form(0), t5_xe: float = Form(0),
):
    conn = conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO xe VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT (ten_xe) DO NOTHING
    """, (ten_xe, h1, h2, h3, h4, h5, t1_xe, t2_xe, t3_xe, t4_xe, t5_xe))

    conn.commit()
    conn.close()

    return """
    
    <html>
    <head>
    <meta http-equiv="refresh" content="1;url=/nhap-xe-tec">
    </head>
    <body style="background:#111;color:white;text-align:center;padding-top:80px;font-family:Arial">

    <h1 style="color:lime">✅ Đã lưu xe!</h1>
    <p>Đang quay lại...</p>

    </body>
    </html>
    """


    

