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
        import sqlite3
        return sqlite3.connect("xe.db")
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
app = FastAPI()

from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
<head>
    <title>Quản lý xăng dầu</title>
    <link rel="icon" type="image/png" href="/static/favicon.png?v=1">

    <style>
        body {
           margin: 0;
    font-family: Arial;
    color: #222;
    text-align: center;
    padding-top: 80px;

    background: linear-gradient(135deg, #f5f7fa, #e4e7eb);  
        }

        /* ===== HEADER ===== */
        .header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 60px;

            background: linear-gradient(90deg, #0f2027, #203a43);
            color: white;

            display: flex;
            justify-content: space-between;
            align-items: center;

            padding: 0 40px;
            box-sizing: border-box;
            z-index: 1000;

            overflow: hidden;
        }

        .logo-group {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo-group img {
            height: 35px;
            border-radius: 6px;
        }

        .logo-text {
            font-weight: bold;
            font-size: 18px;
        }

        .menu a {
            margin-left: 25px;
            color: white;
            text-decoration: none;
        }

        .menu a:hover {
            color: #00eaff;
        }

        /* ===== TRUCK ===== */
        .truck {
            position: absolute;
            top: 18px;
            left: 200px;
            font-size: 14px;
            opacity: 0.7;

            animation: moveTruck 12s linear infinite alternate;
        }

        @keyframes moveTruck {
            0% {
                left: 250px;
            }
            100% {
                left: calc(100% - 620px);
            }
        }
/* ===== BANNER BODY ===== */
.banner {
    width: 100%;
    height: 350px;

    background: url('/static/banne.png') no-repeat center center;
    background-size:contain;   /* QUAN TRỌNG */

    display: flex;
    align-items: center;
    justify-content: center;

    position: relative;
}



/* nội dung */
.banner-content {
    position: relative;
    color: white;
    text-align: center;
}

.banner-content h1 {
    font-size: 15px;
    margin-bottom: 10px;
}

.banner-content p {
    opacity: 0.9;
}

    </style>
</head>

<body>

<!-- HEADER -->
<div class="header">

    <div class="logo-group">
        <img src="/static/logo.png">
        <div class="logo-text">Quản lý xăng dầu</div>
    </div>

    <div class="truck">Petrolimex - Lạng Sơn-Cửa Hàng 29</div>

    <div class="menu">
        <a href="/">Trang chủ</a>
        <a href="/nhap-xe-tec">Nhập xe</a>
        <a href="/quy-doi">Quy đổi</a>
        <a href="/san-pham">Sản phẩm</a>
    </div>

</div>

<!-- CONTENT -->
<img src="/static/banner.png" class="banner-img">
<div class="banner">
    <div class="banner-content">
       
</div>


<!-- FOOTER -->
<div class="footer">
    © 2026 - Quản lý xăng dầu | Version 1.0 <br>
    Developed by <a href="/developer" style="color:orange">Hai Dinh</a> | 27/04/2026
</div>

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
     <title>Quy Đổi Barem Bể</title>
    <link rel="icon" type="image/png" href="/static/favicon.png?v=1">
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
        /* tiêu đề chính */
        .title-main {
            color: #00eaff;
            text-shadow: 0 0 10px rgba(0,255,255,0.7);
        }

        /* cảnh báo */
        .title-warning {
            color: #ff4d4d;
            text-shadow: 0 0 10px rgba(255,0,0,0.7);
            font-weight: bold;
        }

        /* phụ */
        .title-sub {
            color: rgba(255,255,255,0.7);
            font-style: italic;
        }
        body {
    padding-top: 80px;
}
    </style>
    </head>

    <body>
    

    <div class="card">

    <h1 class="title-main">⛽ Quy đổi</h1>
    <h2 class="title-warning">áp dụng riêng CH29</h2>
    <h3 class="title-sub">(Bình Gia - Lạng Sơn)</h3>

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

        </div>

        <a href="/" class="back">← Trang chính</a>

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
        A95: {final_a95:.2f} Lít --> ({ "THỪA" if final_a95 > 0 else "THIẾU" if final_a95 < 0 else "Đu Đủ" })
        </h3>

        <h3 style="color:{'lime' if final_do005 > 0 else 'red' if final_do005 < 0 else 'orange'}">
        DO 0.05: {final_do005:.2f}  Lít --> ({"Thừa" if final_do005 > 0 else "Thiếu" if final_do005 < 0 else "Đủ Đu"})
        </h3>

        <h3 style="color:{'lime' if final_do0001 > 0 else 'red' if final_do0001 < 0 else 'orange'}">
        DO 0.001: {final_do0001:.2f} Lít -->({"Thừa" if final_do0001 > 0 else "Thiếu" if final_do0001 < 0 else "Đủ"})
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
    import json
    du_lieu_xe_json = json.dumps(du_lieu_xe)

    return f"""
    <html>
    <head>
     <title>Nhập xe xi-téc</title>
    <link rel="icon" type="image/png" href="/static/favicon.png?v=1">
    <style>
    body {{
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        font-family: Arial;
        margin: 0;
        padding: 30px;
        color: white;
    }}
  
    select.input {{
    min-width: 120px;
    width: auto;
    padding: 8px 35px 8px 10px;
}}
    .section {{
    margin-top: 20px;
    color: #00eaff;
    font-weight: bold;
}}

.row {{
    display: flex;
    gap: 10px;
    justify-content: center;
    margin-bottom: 10px;
    flex-wrap: wrap;
}}

.input {{
    padding: 8px;
    border-radius: 10px;
    border: none;
    outline: none;
    width: 90px;
    background: rgba(255,255,255,0.08);
    color: white;
}}

.input:focus {{
    box-shadow: 0 0 8px #00eaff;
}}
    .section {{
    margin-top: 20px;
    color: #00eaff;
    font-weight: bold;
}}

.label {{
    font-weight: bold;
    margin-right: 5px;
}}

/* màu từng loại xăng */
.a95 {{
    color: #ff4d4d;
}}

.do005 {{
    color: #00c6ff;
}}

.do0001 {{
    color: #00ff9d;
}}

/* input đẹp hơn */
.input {{
    padding: 8px;
    border-radius: 8px;
    border: none;
    outline: none;
    width: 90px;
    background: rgba(255,255,255,0.1);
    color: white;
}}

/* nút */
.btn {{
    padding: 10px 20px;
    border-radius: 10px;
    border: none;
    background: linear-gradient(45deg, #00c6ff, #0072ff);
    color: white;
    cursor: pointer;
    margin-left: 10px;
}}

.btn:hover {{
    transform: scale(1.05);
}}

        .main {{
            display: flex;
            justify-content: center;
            gap: 20px;
        }}

        .card {{
            background: rgba(255,255,255,0.05);
            padding: 25px;
            border-radius: 15px;
            width: 700px;
            backdrop-filter: blur(10px);
            box-shadow: 0 0 25px rgba(0,0,0,0.5);
        }}

        .result {{
            background: rgba(255,255,255,0.05);
            padding: 20px;
            border-radius: 15px;
            width: 300px;
        }}

        h1, h2, h3 {{
            margin: 10px 0;
        }}

        .row {{
            display: flex;
            gap: 10px;
            margin-bottom: 10px;
            flex-wrap: wrap;
        }}

        

            button:hover {{
                background: #0072ff;
            }}

            .link {{
                color: orange;
                margin-top: 20px;
                display: block;
            }}
            select.input {{
    background: rgba(255,255,255,0.15);
    color: white;
    cursor: pointer;
    border: 1px solid rgba(0,255,255,0.3);
}}

select.input:focus {{
    border: 1px solid #00eaff;
    box-shadow: 0 0 8px #00eaff;
}}

select option {{
    background: #1e2f36;
    color: white;
}}
select.input {{
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;

    background: rgba(255,255,255,0.15);
    color: white;
    border: 1px solid rgba(0,255,255,0.4);
    border-radius: 10px;
    padding: 8px 30px 8px 10px;
    cursor: pointer;

    transition: 0.2s;

    /* mũi tên đẹp */
    background-image: url("data:image/svg+xml;utf8,<svg fill='white' height='20' viewBox='0 0 20 20' width='20' xmlns='http://www.w3.org/2000/svg'><polygon points='0,5 10,15 20,5'/></svg>");
    background-repeat: no-repeat;
    background-position: right 8px center;
}}

select.input:hover {{
    border-color: #00eaff;
}}

select.input:focus {{
    outline: none;
    border-color: #00eaff;
    box-shadow: 0 0 8px #00eaff;
}}

/* dropdown bên trong */
select option {{
    background: #1e2f36;
    color: white;
}}
            </style>
            </head>

            <body>

            <div class="main">

            <div class="card">

            <h1>🚛 Nhập xe téc</h1>

            <a href="/them-xe" style="color:lime;">➕ Thêm xe</a>
            <a id="xoaLink"
               href="/xoa-xe?ten_xe={form_data.get('ten_xe','')}"
               style="color:red;margin-left:15px;"
               onclick="return confirm('Xóa xe này?')">
                🗑 Xóa
            </a>

            <form action="/nhap-xe-tec" method="post" onsubmit="daSubmit = true;">

            <h2>🚛 Chọn xe</h2>
            <select class="input" name="ten_xe" onchange="chonXe(this.value)">
            <option value="">-- Chọn xe --</option>
            {options}
            </select>

                
    

    <h2 class="section">🛢️ Khoang 1</h2>
<div class="row">
    <input class="input" name="t1_xe" value="{form_data.get('t1_xe','')}" placeholder="Barem">
    <input class="input" name="t1_ch" value="{form_data.get('t1_ch','')}" placeholder="CH Đo">
    <input class="input" name="h1" value="{form_data.get('h1','')}" placeholder="Lít/Cm">
    <input class="input" name="t1_du" value="{form_data.get('t1_du','')}" placeholder="Dư Hóa Đơn">

    <select class="input fuel-select" name="fuel1" onchange="doiMau(this)">
        <option value="a95" {"selected" if form_data.get("fuel1")=="a95" else ""}>Xăng RON95</option>
        <option value="do005" {"selected" if form_data.get("fuel1")=="do005" else ""}>DO 0.05S-II</option>
        <option value="do0001" {"selected" if form_data.get("fuel1")=="do0001" else ""}>DO 0.001S-V</option>
    </select>
</div>

<h2 class="section">🛢️ Khoang 2</h2>
<div class="row">
    <input class="input" name="t2_xe" value="{form_data.get('t2_xe','')}" placeholder="Barem">
    <input class="input" name="t2_ch" value="{form_data.get('t2_ch','')}" placeholder="CH Đo">
    <input class="input" name="h2" value="{form_data.get('h2','')}" placeholder="Lít/Cm">
    <input class="input" name="t2_du" value="{form_data.get('t2_du','')}" placeholder="Dư Hóa Đơn">

    <select class="input fuel-select" name="fuel2" onchange="doiMau(this)">
        <option value="a95" {"selected" if form_data.get("fuel2")=="a95" else ""}>Xăng RON95</option>
        <option value="do005" {"selected" if form_data.get("fuel2")=="do005" else ""}>DO 0.05S-II</option>
        <option value="do0001" {"selected" if form_data.get("fuel2")=="do0001" else ""}>DO 0.001S-V</option>
    </select>
</div>

<h2 class="section">🛢️ Khoang 3</h2>
<div class="row">
    <input class="input" name="t3_xe" value="{form_data.get('t3_xe','')}" placeholder="Barem">
    <input class="input" name="t3_ch" value="{form_data.get('t3_ch','')}" placeholder="CH Đo">
    <input class="input" name="h3" value="{form_data.get('h3','')}" placeholder="Lít/Cm">
    <input class="input" name="t3_du" value="{form_data.get('t3_du','')}" placeholder="Dư Hóa Đơn">

    <select class="input fuel-select" name="fuel3" onchange="doiMau(this)">
        <option value="a95" {"selected" if form_data.get("fuel3")=="a95" else ""}>Xăng RON95</option>
        <option value="do005" {"selected" if form_data.get("fuel3")=="do005" else ""}>DO 0.05S-II</option>
        <option value="do0001" {"selected" if form_data.get("fuel3")=="do0001" else ""}>DO 0.001S-V</option>
    </select>
</div>

<h2 class="section">🛢️ Khoang 4</h2>
<div class="row">
    <input class="input" name="t4_xe" value="{form_data.get('t4_xe','')}" placeholder="Barem">
    <input class="input" name="t4_ch" value="{form_data.get('t4_ch','')}" placeholder="CH Đo">
    <input class="input" name="h4" value="{form_data.get('h4','')}" placeholder="Lít/Cm">
    <input class="input" name="t4_du" value="{form_data.get('t4_du','')}" placeholder="Dư Hóa Đơn">

    <select class="input fuel-select" name="fuel4" onchange="doiMau(this)">
        <option value="a95" {"selected" if form_data.get("fuel4")=="a95" else ""}>Xăng RON95</option>
        <option value="do005" {"selected" if form_data.get("fuel4")=="do005" else ""}>DO 0.05S-II</option>
        <option value="do0001" {"selected" if form_data.get("fuel4")=="do0001" else ""}>DO 0.001S-V</option>
    </select>
</div>

<h2 class="section">🛢️ Khoang 5</h2>
<div class="row">
    <input class="input" name="t5_xe" value="{form_data.get('t5_xe','')}" placeholder="Barem">
    <input class="input" name="t5_ch" value="{form_data.get('t5_ch','')}" placeholder="CH Đo">
    <input class="input" name="h5" value="{form_data.get('h5','')}" placeholder="Lít/Cm">
    <input class="input" name="t5_du" value="{form_data.get('t5_du','')}" placeholder="Dư Hóa Đơn">

    <select class="input fuel-select" name="fuel5" onchange="doiMau(this)">
        <option value="a95" {"selected" if form_data.get("fuel5")=="a95" else ""}>Xăng RON95</option>
        <option value="do005" {"selected" if form_data.get("fuel5")=="do005" else ""}>DO 0.05S-II</option>
        <option value="do0001" {"selected" if form_data.get("fuel5")=="do0001" else ""}>DO 0.001S-V</option>
    </select>
</div>

        <h2 class="section">📦 Số lượng hàng trên hóa đơn</h2>
        <div class="row">
            <label class="label a95">A95</label>
            <input class="input" name="sl_a95" value="{form_data.get('sl_a95','')}">

            <label class="label do005">DO 0.05</label>
            <input class="input" name="sl_do005" value="{form_data.get('sl_do005','')}">

            <label class="label do0001">DO 0.001</label>
            <input class="input" name="sl_do0001" value="{form_data.get('sl_do0001','')}">
        </div>

        <h2 class="section">🌡️ Nhiệt độ trên hóa đơn</h2>
        <div class="row">
            <label class="label a95">A95</label>
            <input class="input" name="temp_hd_a95" value="{form_data.get('temp_hd_a95','')}">

            <label class="label do005">DO 0.05</label>
            <input class="input" name="temp_hd_do005" value="{form_data.get('temp_hd_do005','')}">

            <label class="label do0001">DO 0.001</label>
            <input class="input" name="temp_hd_do0001" value="{form_data.get('temp_hd_do0001','')}">
        </div>

        <h2 class="section">🌡️ Nhiệt độ đo tại cửa hàng</h2>
        <div class="row">
            <label class="label a95">A95</label>
            <input class="input" name="temp_ch_a95" value="{form_data.get('temp_ch_a95','')}">

            <label class="label do005">DO 0.05</label>
            <input class="input" name="temp_ch_do005" value="{form_data.get('temp_ch_do005','')}">

            <label class="label do0001">DO 0.001</label>
            <input class="input" name="temp_ch_do0001" value="{form_data.get('temp_ch_do0001','')}">
        </div>

        <h2 class="section">🚚 Quãng đường vận chuyển (km)</h2>
        <div class="row">
            <input class="input" name="distance" value="{form_data.get('distance','')}" placeholder="Số Km">
            <button class="btn">Tính</button>

        </div>

        </form>
        </div>

        <div class="result">
        {ket_qua_html}
        </div>

        </div>

        <a href="/" class="link">← Trang chính</a>
        <script>
        let du_lieu_xe = {du_lieu_xe_json};
        </script>
        <script>
        function chonXe(ten) {{
            let xe = du_lieu_xe[ten];
            if (!xe) {{
                return;
                }}

    document.getElementsByName("h1")[0].value = xe.h1;
    document.getElementsByName("h2")[0].value = xe.h2;
    document.getElementsByName("h3")[0].value = xe.h3;
    document.getElementsByName("h4")[0].value = xe.h4;
    document.getElementsByName("h5")[0].value = xe.h5;

    document.getElementsByName("t1_xe")[0].value = xe.t1_xe;
    document.getElementsByName("t2_xe")[0].value = xe.t2_xe;
    document.getElementsByName("t3_xe")[0].value = xe.t3_xe;
    document.getElementsByName("t4_xe")[0].value = xe.t4_xe;
    document.getElementsByName("t5_xe")[0].value = xe.t5_xe;
    document.getElementById("xoaLink").href = "/xoa-xe?ten_xe=" + ten;
        }}
        </script>
     <script>
function doiMau(el) {{
    if (el.value === "a95") {{
        el.style.borderColor = "#ff4d4d";
        el.style.color = "#ff4d4d";
    }}
    else if (el.value === "do005") {{
        el.style.borderColor = "#00c6ff";
        el.style.color = "#00c6ff";
    }}
    else {{
        el.style.borderColor = "#00ff9d";
        el.style.color = "#00ff9d";
    }}
}}
</script>
<script>
window.onload = function() {{
    document.querySelectorAll("select.input").forEach(el => {{
        doiMau(el);
        }});
}}
</script>

        </body>
        </html>
    """
from fastapi.responses import RedirectResponse

@app.get("/xoa-xe",response_class=HTMLResponse)
def xoa_xe(ten_xe: str):
    conn = get_conn()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM xe WHERE ten_xe=%s", (ten_xe,))
    except:
        cursor.execute("DELETE FROM xe WHERE ten_xe=?", (ten_xe,))

    conn.commit()
    conn.close()

    return RedirectResponse("/nhap-xe-tec", status_code=303)
   
@app.get("/them-xe", response_class=HTMLResponse)
def form_them_xe():
    return """
    <html>
     <title>Thêm Xe</title>
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
    import os

    conn = get_conn()
    cursor = conn.cursor()

    # 👇 AUTO chọn DB
    if os.getenv("DATABASE_URL"):
        # PostgreSQL (Render)
        cursor.execute("""
        INSERT INTO xe VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (ten_xe) DO NOTHING
        """, (ten_xe, h1, h2, h3, h4, h5, t1_xe, t2_xe, t3_xe, t4_xe, t5_xe))

    else:
        # SQLite (local)
        cursor.execute("""
        INSERT OR IGNORE INTO xe VALUES (?,?,?,?,?,?,?,?,?,?,?)
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
from fastapi.responses import HTMLResponse

@app.get("/san-pham", response_class=HTMLResponse)
def san_pham():
    return """
    <html>
    <head>
     <title>Sản Phẩm</title>
    <link rel="icon" type="image/png" href="/static/favicon.png?v=1">
    <style>
                
        body {
            background: #0f2027;
            font-family: Arial;
            color: white;
            text-align: center;
            padding: 40px;
        }

        .grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
        }

        .item {
            width: 150px;
            text-align: center;
            cursor: pointer;
        }

        .item img {
            width: 120px;
            height: 120px;          /* 🔥 quan trọng */
            object-fit: contain;
            background: white;
            border-radius: 10px;
            padding: 5px;
            transition: 0.3s;
        }

        .item img:hover {
            transform: scale(1.1);
        }
        .item p {
        font-size: 13px;
        margin-top: 8px;
        }
        .item p {
        height: 35px;
        overflow: hidden;
        }
        .item {
        transition: 0.3s;
        }

        .item:hover {
        transform: translateY(-5px);
        }
        .item img {
        border: 1px solid rgba(255,255,255,0.2);
        }
        </style>
    </head>

    <body>

    <h1>Sản Phẩm Được Bán Tại Các Đại Lý Petrolimex Trên Toàn Quốc</h1>

    <div class="grid">

        <div class="item" onclick="moModal(
          'https://daunhotsongphat.vn/storage/uploads/products/ca3611cb7c94caa232425ef1428ac115-2115.jpeg',
          'Dầu Racer SJ',
          'Dầu nhớt xe máy Petrolimex',
          'SAE 20W50 - API SJ - 800ml'
        )">
            <img src="https://daunhotsongphat.vn/storage/uploads/products/ca3611cb7c94caa232425ef1428ac115-2115.jpeg">
            <p>Dầu Racer SJ</p>
        </div>

        <!-- thêm sản phẩm ở đây -->
        <div class="item" onclick="moModal(
          'https://daunhonpetrolimex.com/image/cache/catalog/plc%20racer%202t%201l-450x450.jpg',
          'Race 2T',
          'PLC Racer 2T là dầu động cơ xăng 2 thì được pha chế từ dầu gốc có chất lượng cao cùng với phụ gia chống mài mòn và dễ hòa trộn với xăng. ',
          'Độ nhớt ở 100oC'
        )">
            <img src="https://daunhonpetrolimex.com/image/cache/catalog/plc%20racer%202t%201l-450x450.jpg">
            <p>Racer 2T</p>
        </div>
        <div class="item" onclick="moModal(
          'https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lm2s74cgr1zz23',
          'PLC RACER SCOOTER MB',
          'Dầu động cơ PLC RACER SCOOTER MB là dầu động cơ đa cấp cho xe máy tay ga cấp chất lượng cao nhất theo tiêu chuẩn JASO T904-2006. Dầu có chứa các loại phụ gia chống mài mòn, tẩy rửa tốt, chống tạo cặn với công nghệ tiên tiến nhất đem lại tính năng bảo vệ động cơ ở mức cao nhất, đáp ứng các tiêu chuẩn của nhà chế tạo động cơ. ',
          'có tại petrolimex-cửa hàng 29 ,xã Bình Gia , Lạng Sơn'
        )">
            <img src="https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lm2s74cgr1zz23">
            <p>PLC RACER SCOOTER MB</p>
        </div>
        <div class="item" onclick="moModal(
          'https://cdn0597.cdn4s.com/media/san-pham/b%C3%ACnh%20gas/binh-gas-petrolimex-12kg-gas-petrolimex-chinh-hang.jpg',
          'Bình gas Petrolimex 12kg',
          'Hãng sản xuất:Công ty cổ phần Gas Petrolimex (Petrolimex Gas) Trọng lượng: 12 Kg Màu bình: Màu Xanh ',
          'Tiêu chuẩn chất lượng: Vỏ bình gas sản xuất theo tiêu chuẩn DOT-4BA-240, DOT-4BW-240 và TCVN 6292-1997'
        )">
            <img src="https://cdn0597.cdn4s.com/media/san-pham/b%C3%ACnh%20gas/binh-gas-petrolimex-12kg-gas-petrolimex-chinh-hang.jpg">
            <p>Bình gas Petrolimex 12kg</p>
        </div>
        <div class="item" onclick="moModal(
          'https://cdn1288.cdn4s2.com/media/san_pham/binh-gas-petrolimex-48kg.jpg',
          'Bình gas công nghiệp petrolimex 48kg',
          'Đối với những gia đình có nhu cầu sử dụng ga vừa phải thì chỉ cần một chiếc bình gas 12kg là phù hợp. Còn những bếp ăn có công suất lớn, nhu cầu sử dụng nhiều, phục vụ nhiều người và cần nhanh nhạy thì bình gas công nghiệp 48kg lại là lựa chọn lý tưởng.',
          'Đặc điểm của bình là có màu xanh ngọc, thiết kế thon dài, khối lượng ga trong bình là 48kg, trọng lượng vỏ đạt khoảng 37 – 40kg.'
        )">
            <img src="https://cdn1288.cdn4s2.com/media/san_pham/binh-gas-petrolimex-48kg.jpg">
            <p>Bình gas công nghiệp petrolimex 48kg</p>
        </div>
        <div class="item" onclick="moModal(
        'https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lva6ptuyzlus58',
        'PLC Komat SHD',
        'PLC Komat SHD được pha chế từ nguyên liệu tinh chế và các phụ gia chọn lọc tạo thành các sản phẩm bôi trơn hoàn hảo, có tính chống gỉ tốt, giữ cho động cơ luôn sạch, không tạo bọt.',
        'PLC Komat SHD được dùng cho động cơ xăng và diesel của ôtô, máy móc, thiết bị sử dụng nhiên liệu có hàm lượng lưu huỳnh thấp, hoạt động ở điều kiện tương đối cao. Loại dầu này đáp ứng tiêu chuẩn API: SC/CC và cấp MIL-L-2104B.'
        )">
        <img src="https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lva6ptuyzlus58">
        <p>PLC Komat SHD</p>
        </div>
        <div class="item" onclick="moModal(
          'https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m0lry6cygya700',
          'Dầu thủy lực Petrolimex PLC AW Hydroil 68',
          'Dầu thủy lực PLC AW HYDROIL 68 được pha chế từ dầu gốc có chỉ số độ nhớt cao và các phụ gia chống oxy hóa, chống mài mòn, ăn mòn và chống tạo bọt, giúp bảo vệ hoàn hảo hệ thống thủy lực và các thiết bị sử dụng dầu',
          'Ngày nay các sản phẩm dầu thủy lực PLC được ứng dụng rộng rãi trong hầu hết các ngành công nghiệp'
        )">
            <img src="https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m0lry6cygya700">
            <p>Dầu thủy lực Petrolimex PLC AW Hydroil 68</p>
        </div>
        <div class="item" onclick="moModal(
          'https://xangdauvanduc.com/wp-content/uploads/2025/07/plc-gear-oil-mp-90-ep-thung-18l-scaled.jpg',
          'GEAR OIL MP 90 EP',
          'PLC GEAR OIL MP là dầu hộp số được pha chế từ nguyên liệu có chất lượng cao, phù hợp với cấp chất lượng API: GL-4 và MIL-L-2105B',
          'PLC Gear oil MP 90 EP là dầu hộp số đa năng với phụ gia EP cung cấp khả năng bôi trơn hoàn hảo cho các phương tiện giao thông trên xa lộ, các phương tiện nông nghiệp.'
        )">
            <img src="https://xangdauvanduc.com/wp-content/uploads/2025/07/plc-gear-oil-mp-90-ep-thung-18l-scaled.jpg">
            <p>GEAR OIL MP 90 EP</p>
        </div>
        <div class="item" onclick="moModal(
          'https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m0mroh4q499p07',
          'PLC Cater CI-4',
          'Dầu đạt cấp độ nhớt SAE: 15W-40, đáp ứng các yêu cầu cấp chất lượng API: CI-4 đối với động cơ Diesel và cấp API: SL đối với động cơ xăng.',
          'Phuy 209L, Xô 18L, Thùng 18L, 25L và Hộp 1L, 5L, 6L.'
        )">
        <img src="https://down-vn.img.susercontent.com/file/vn-11134207-7ras8-m0mroh4q499p07">
        <p>PLC Cater CI-4</p>
    </div>
    <div class="item" onclick="moModal(
      'https://down-vn.img.susercontent.com/file/8f8687121b92feb2262279f5db9c4e22',
      'Dầu Phanh DOT3',
      'Dầu phanh Castrol Brake Fluid DOT 3 (1 Lít) là sản phẩm cao cấp đến từ thương hiệu nổi tiếng Castrol, được thiết kế chuyên biệt cho hệ thống phanh thủy lực của ô tô và xe tải.',
      'VHDP DOT3 sử dụng cho các hệ thống phanh và côn ly hợp lắp trên các xe ôtô hoạt động ở vùng nhiệt đới với cuppen do Việt Nam'
    )">
        <img src="https://down-vn.img.susercontent.com/file/8f8687121b92feb2262279f5db9c4e22">
        <p>Dầu Phanh DOT3</p>
    </div>
    <div class="item" onclick="moModal(
      'https://nhuanhatminh.vn/wp-content/uploads/2022/07/kich-thuoc-thung-phi-nhua-1.jpg',
      'Phuy Nhựa',
      'Thùng phuy nhựa được làm bằng polyetylen mật độ cao (HDPE) hoặc polypropylen (PP) có độ bền cao, chống ăn mòn hoá học',
      'Thùng phuy nhựa 30l, 50l, 120l, 200l, 220l'
    )">
        <img src="https://nhuanhatminh.vn/wp-content/uploads/2022/07/kich-thuoc-thung-phi-nhua-1.jpg">
        <p>Phuy Nhựa </p>
    </div>

        
    </div>
    <a href="/" class="link">← Trang chính</a>
    <!-- MODAL -->
    <div id="modal" style="
      display:none;
      position:fixed;
      top:0; left:0;
      width:100%; height:100%;
      background:rgba(0,0,0,0.8);
      justify-content:center;
      align-items:center;
    " onclick="dongModal()">

      <div onclick="event.stopPropagation()" style="
        background:white;
        padding:20px;
        border-radius:15px;
        display:flex;
        gap:20px;
        align-items:center;
        max-width:700px;
      ">

        <img id="modal_img" style="
          width:250px;
          border-radius:10px;
        ">

        <div style="text-align:left; color:black">

          <h2 id="modal_ten"></h2>

          <p id="modal_mota"></p>

          <p id="modal_thongso" style="font-weight:bold;"></p>

          <button onclick="dongModal()" style="
            padding:8px 20px;
            border:none;
            border-radius:8px;
            background:#333;
            color:white;
            cursor:pointer;
          ">Đóng</button>

        </div>

      </div>
    </div>

    <script>
    function moModal(img, ten, mota, thongso) {
      document.getElementById("modal").style.display = "flex";
      document.getElementById("modal_img").src = img;
      document.getElementById("modal_ten").innerText = ten;
      document.getElementById("modal_mota").innerText = mota;
      document.getElementById("modal_thongso").innerText = thongso;
    }

    function dongModal() {
      document.getElementById("modal").style.display = "none";
    }
    </script>

    </body>
    </html>
    """
from fastapi.responses import HTMLResponse

@app.get("/developer", response_class=HTMLResponse)
def developer():
    return """
    <html>
     <title>Nhà phát triển</title>
    <link rel="icon" type="image/png" href="/static/favicon.png?v=1">
    <body style="background:black;color:white;text-align:center;padding-top:80px;font-family:Arial">

    <h1>👨‍💻 Developed by</h1>
    <h2>Hai Dinh</h2>

    <p>What program do you use?</p>
    <p><i>*whispers*</i> ChatGPT</p>

    <br>
    <a href="/" style="color:orange">← Trang chính</a>

    </body>
    </html>
    """



    

