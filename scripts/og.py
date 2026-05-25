# -*- coding: utf-8 -*-
"""의존성 없는 OG 이미지(1200×630 PNG) 생성. zlib(stdlib)만 사용."""
import struct
import zlib

W, H = 1200, 630

# 5×7 비트맵 글리프 (선호 썸네일 워드마크용)
FONT = {
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "C": ["01110", "10001", "10000", "10000", "10000", "10001", "01110"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "9": ["01110", "10001", "10001", "01111", "00001", "00001", "01110"],
    "+": ["00000", "00100", "00100", "11111", "00100", "00100", "00000"],
    " ": ["00000"] * 7,
}


def _new_buf():
    return bytearray(W * H * 3)


def _set(buf, x, y, c):
    if 0 <= x < W and 0 <= y < H:
        i = (y * W + x) * 3
        buf[i], buf[i + 1], buf[i + 2] = c


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _text(buf, text, x0, y0, scale, color):
    cx = x0
    for ch in text:
        glyph = FONT.get(ch, FONT[" "])
        for ry, row in enumerate(glyph):
            for rx, bit in enumerate(row):
                if bit == "1":
                    for dx in range(scale):
                        for dy in range(scale):
                            _set(buf, cx + rx * scale + dx, y0 + ry * scale + dy, color)
        cx += (3 if ch == " " else 6) * scale
    return cx - x0


def _text_width(text, scale):
    return sum((3 if ch == " " else 6) * scale for ch in text)


def build_png(path):
    buf = _new_buf()
    c0, c1 = (24, 24, 38), (11, 11, 18)
    for y in range(H):
        for x in range(W):
            t = (x + y) / (W + H)
            _set(buf, x, y, _lerp(c0, c1, t))

    gold_l, gold_d = (224, 189, 134), (138, 106, 56)

    # 워드마크 중앙 정렬
    scale = 16
    word = "HOBBA CLUB"
    wmw = _text_width(word, scale)
    gh = 7 * scale
    x0 = (W - wmw) // 2
    y0 = (H - gh) // 2 - 20
    _text(buf, word, x0, y0, scale, gold_l)

    # 골드 언더라인 (그라데이션)
    uy = y0 + gh + 36
    uw = wmw
    for x in range(uw):
        col = _lerp(gold_l, gold_d, x / max(uw, 1))
        for dy in range(8):
            _set(buf, x0 + x, uy + dy, col)

    # 19+ 우상단 표식
    _text(buf, "19+", W - _text_width("19+", 10) - 60, 60, 10, gold_l)

    raw = bytearray()
    for y in range(H):
        raw.append(0)  # filter type 0
        raw += buf[y * W * 3:(y + 1) * W * 3]
    comp = zlib.compress(bytes(raw), 9)

    def chunk(tag, data):
        c = tag + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xffffffff)

    ihdr = struct.pack(">IIBBBBB", W, H, 8, 2, 0, 0, 0)
    png = (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) +
           chunk(b"IDAT", comp) + chunk(b"IEND", b""))
    with open(path, "wb") as f:
        f.write(png)
