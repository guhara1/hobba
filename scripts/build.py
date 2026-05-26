# -*- coding: utf-8 -*-
"""통합 빌더: 전 페이지 + sitemap·rss·robots·manifest·favicon·og 생성·미니파이."""
import os
import re
import sys
from datetime import datetime, timezone, timedelta

sys.path.insert(0, os.path.dirname(__file__))
from data import COMPANY, LAST_UPDATED
from content import MAGAZINE, SAFETY, NOTICES
from pages import all_pages
from og import build_png

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = COMPANY
KST = timezone(timedelta(hours=9))


def minify(html):
    # JSON-LD / <script> / <style> 보존하며 태그 간 공백 축소
    html = re.sub(r">\s+<", "><", html)
    html = re.sub(r"\n\s*", " ", html)
    html = re.sub(r"  +", " ", html)
    return html.strip()


def write(rel, content, do_min=True):
    path = os.path.join(ROOT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if do_min and rel.endswith(".html"):
        content = minify(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def _changefreq(loc, pri):
    if loc == "/":
        return "daily"
    if "/policy/" in loc:
        return "yearly"
    if loc in ("/jobs/", "/magazine/", "/safety/", "/support/", "/advertising/",
               "/support/notice/"):
        return "weekly"
    return "monthly"


def build_sitemap(urls):
    # lastmod은 실제 콘텐츠 갱신일(LAST_UPDATED) — 매 빌드마다 바뀌지 않아 신뢰도 유지
    items = ""
    for loc, pri in urls:
        items += (f"<url><loc>{C['url']}{loc}</loc><lastmod>{LAST_UPDATED}</lastmod>"
                  f"<changefreq>{_changefreq(loc, pri)}</changefreq>"
                  f"<priority>{pri}</priority></url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + items + "</urlset>")
    write("/sitemap.xml", xml, do_min=False)
    write("/sitemap1.xml", xml, do_min=False)
    # 사이트맵 인덱스(검색엔진 제출 편의·이중화)
    idx = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
           f'<sitemap><loc>{C["url"]}/sitemap.xml</loc><lastmod>{LAST_UPDATED}</lastmod></sitemap>'
           f'<sitemap><loc>{C["url"]}/sitemap1.xml</loc><lastmod>{LAST_UPDATED}</lastmod></sitemap>'
           '</sitemapindex>')
    write("/sitemap_index.xml", idx, do_min=False)


def _esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def build_rss():
    now = datetime.now(KST)
    # (date, title, link, guid, desc, category) — 매거진+안전센터+공지 전부 포함
    entries = []
    for slug, a in MAGAZINE.items():
        entries.append((a["date"], a["title"], f"{C['url']}/magazine/{slug}/",
                        f"{C['url']}/magazine/{slug}/", a["desc"], "매거진"))
    for slug, a in SAFETY.items():
        entries.append((a["date"], a["title"], f"{C['url']}/safety/{slug}/",
                        f"{C['url']}/safety/{slug}/", a["desc"], "안전센터"))
    for n in NOTICES:
        entries.append((n["date"], f"[공지] {n['title']}", f"{C['url']}/support/notice/",
                        f"{C['url']}/support/notice/#{n['slug']}", n["body"][0], "공지사항"))
    entries.sort(key=lambda e: e[0], reverse=True)  # 최신순
    items = ""
    for date, title, link, guid, desc, cat in entries:
        pub = datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=KST)
        items += (f"<item><title>{_esc(title)}</title>"
                  f"<link>{link}</link>"
                  f"<guid isPermaLink=\"false\">{guid}</guid>"
                  f"<category>{cat}</category>"
                  f"<description>{_esc(desc)}</description>"
                  f"<pubDate>{pub.strftime('%a, %d %b %Y %H:%M:%S +0900')}</pubDate></item>")
    rss = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>'
           f"<title>{_esc(C['name'])} 매거진·안전센터</title><link>{C['url']}/</link>"
           f"<description>{_esc(C['tagline'])}</description><language>ko-KR</language>"
           f"<generator>{_esc(C['name'])}</generator><ttl>60</ttl>"
           f'<atom:link href="{C["url"]}/rss.xml" rel="self" type="application/rss+xml"/>'
           f"<lastBuildDate>{now.strftime('%a, %d %b %Y %H:%M:%S +0900')}</lastBuildDate>"
           + items + "</channel></rss>")
    write("/rss.xml", rss, do_min=False)


def build_robots():
    # Crawl-delay 제거(크롤 속도 제약 없앰) — 빠른 색인 우선. 검색·AI 봇 전체 허용, /api만 차단.
    txt = (
        "User-agent: Googlebot\nAllow: /\n\n"
        "User-agent: Googlebot-Image\nAllow: /\n\n"
        "User-agent: Bingbot\nAllow: /\n\n"
        "User-agent: Yeti\nAllow: /\n\n"          # 네이버
        "User-agent: NaverBot\nAllow: /\n\n"
        "User-agent: Daum\nAllow: /\n\n"
        "User-agent: Daumoa\nAllow: /\n\n"
        "User-agent: GPTBot\nAllow: /\n\n"
        "User-agent: OAI-SearchBot\nAllow: /\n\n"
        "User-agent: ChatGPT-User\nAllow: /\n\n"
        "User-agent: ClaudeBot\nAllow: /\n\n"
        "User-agent: PerplexityBot\nAllow: /\n\n"
        "User-agent: *\nAllow: /\nDisallow: /api/\n\n"
        f"Sitemap: {C['url']}/sitemap.xml\n"
        f"Sitemap: {C['url']}/sitemap1.xml\n"
        f"Sitemap: {C['url']}/sitemap_index.xml\n"
        f"Host: {C['domain']}\n")
    write("/robots.txt", txt, do_min=False)


def build_manifest():
    m = ('{"name":"%s","short_name":"%s","start_url":"/","display":"standalone",'
         '"background_color":"#0b0b12","theme_color":"#0b0b12",'
         '"icons":[{"src":"/favicon.svg","sizes":"any","type":"image/svg+xml"}]}'
         % (C["name"], C["name"]))
    write("/site.webmanifest", m, do_min=False)


def build_headers():
    # Cloudflare Pages _headers: 정적자원 장기 캐시 + 보안/성능 헤더
    txt = (
        "/*\n"
        "  X-Content-Type-Options: nosniff\n"
        "  Referrer-Policy: strict-origin-when-cross-origin\n"
        "  X-Frame-Options: SAMEORIGIN\n"
        "  Permissions-Policy: geolocation=(), microphone=(), camera=()\n"
        "  Strict-Transport-Security: max-age=31536000; includeSubDomains\n\n"
        "/*.html\n"
        "  Cache-Control: public, max-age=0, must-revalidate\n\n"
        "/\n"
        "  Cache-Control: public, max-age=0, must-revalidate\n\n"
        "/assets/*\n"
        "  Cache-Control: public, max-age=31536000, immutable\n\n"
        "/favicon.svg\n"
        "  Cache-Control: public, max-age=604800\n\n"
        "/site.webmanifest\n"
        "  Cache-Control: public, max-age=604800\n")
    write("/_headers", txt, do_min=False)


def build_favicon():
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
           '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
           '<stop offset="0" stop-color="#e0bd86"/><stop offset="1" stop-color="#8a6a38"/></linearGradient></defs>'
           '<rect width="64" height="64" rx="14" fill="url(#g)"/>'
           '<text x="32" y="44" font-family="Georgia,serif" font-size="38" font-weight="700" '
           'text-anchor="middle" fill="#1a130a">H</text></svg>')
    write("/favicon.svg", svg, do_min=False)


# 광고/문의 폼 priorities
PRIORITY = {
    "/": "1.0", "/jobs/": "0.9", "/magazine/": "0.9", "/safety/": "0.9",
    "/support/": "0.8", "/about/": "0.8", "/advertising/": "0.9", "/advertising/contact/": "0.8",
}


def main():
    pages = all_pages()
    urls = []
    for rel, html in pages:
        write(rel, html)
        if rel == "/404.html" or rel.startswith("/promo/"):
            continue  # 404·샘플 홍보(noindex)는 sitemap 제외
        loc = "/" if rel == "/index.html" else "/" + rel[:-len("index.html")].lstrip("/")
        pri = PRIORITY.get(loc, "0.7")
        if "/policy/" in loc:
            pri = "0.3"
        urls.append((loc, pri))

    build_sitemap(urls)
    build_rss()
    build_robots()
    build_manifest()
    build_headers()
    build_favicon()
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    build_png(os.path.join(ROOT, "assets", "og.png"))
    print(f"✅ {len(pages)} HTML 페이지 생성 완료")
    for rel, _ in sorted(pages):
        print("  ", "/" if rel == "/index.html" else "/" + rel[:-len('index.html')].lstrip('/'))
    print("✅ sitemap.xml · sitemap1.xml · sitemap_index.xml · rss.xml · robots.txt · site.webmanifest · favicon.svg · _headers · assets/og.png")


if __name__ == "__main__":
    main()
