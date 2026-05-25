# -*- coding: utf-8 -*-
"""공통 템플릿: CSS_BASE · head() · header_html() · promo_bar() · footer_html() · page()"""
import json
from data import COMPANY, NAV_MAIN, NAV_AD, NAV_CONTACT, MOBILE_PRIMARY, AGE_NOTICE, VERIFY

# ─────────────────────────────────────────────────────────────
# 디자인 시스템 (다크 + 골드 — 신뢰형 나이트 톤)
# ─────────────────────────────────────────────────────────────
CSS_BASE = """
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0b0b12;--surface:#15151f;--surface-2:#1d1d2c;
  --line:rgba(255,255,255,.08);
  --text:#f2eef7;--muted:#aaa4bc;--dim:#726c86;
  --g1:#e0bd86;--g2:#c39a5c;--g3:#8a6a38;
  --grad:linear-gradient(135deg,#e0bd86 0%,#c39a5c 50%,#8a6a38 100%);
  --grad-soft:linear-gradient(135deg,rgba(224,189,134,.14),rgba(138,106,56,.05));
  --gold:#d6b274;--radius:16px;--maxw:1240px;
}
html{scroll-behavior:smooth;scroll-padding-top:90px}
body{background:var(--bg);color:var(--text);line-height:1.65;letter-spacing:-.01em;
  font-family:"Pretendard","Apple SD Gothic Neo","Noto Sans KR",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  -webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
.serif{font-family:"Cormorant Garamond","Noto Serif KR",Georgia,serif;font-weight:300;font-style:italic}
.wrap{max-width:var(--maxw);margin:0 auto;padding:96px 24px}
.note-text{max-width:680px}
.kicker{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--g1);font-weight:700}
.gradtext{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
h1{font-size:clamp(34px,5.2vw,58px);font-weight:800;letter-spacing:-.035em;line-height:1.08}
h2{font-size:clamp(26px,3.6vw,42px);font-weight:800;letter-spacing:-.03em;margin-bottom:18px}
h3{font-size:clamp(17px,2vw,21px);font-weight:800;letter-spacing:-.02em}
p{color:var(--muted)}
.btn{display:inline-flex;align-items:center;gap:8px;padding:13px 24px;border-radius:999px;
  font-weight:700;font-size:14px;transition:.18s;border:1px solid transparent;cursor:pointer}
.btn-gold{background:var(--grad);color:#1a130a;box-shadow:0 6px 24px rgba(195,154,92,.25)}
.btn-gold:hover{transform:translateY(-2px)}
.btn-ghost{border-color:var(--line);color:var(--text)}
.btn-ghost:hover{border-color:var(--g2);color:var(--g1)}

/* ── 헤더 ── */
.site-header{position:sticky;top:0;z-index:50;background:rgba(11,11,18,.82);
  backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.nav{max-width:var(--maxw);margin:0 auto;display:flex;align-items:center;gap:14px;
  padding:14px 24px}
.logo{display:flex;align-items:center;gap:9px;font-weight:800;font-size:19px;flex-shrink:0}
.logo .mark{width:30px;height:30px;border-radius:9px;background:var(--grad);
  display:grid;place-items:center;color:#1a130a;font-weight:900;font-size:15px}
.nav-main{display:flex;align-items:center;gap:4px;margin-left:14px}
.nav-right{display:flex;align-items:center;gap:6px;margin-left:auto}
.nav-item{position:relative}
.nav-link{display:inline-flex;align-items:center;gap:5px;padding:9px 13px;border-radius:10px;
  font-size:14.5px;font-weight:600;color:var(--text);white-space:nowrap}
.nav-link:hover{background:var(--surface-2);color:var(--g1)}
.nav-link .car{font-size:9px;opacity:.6;transition:.18s}
.nav-item:hover .car{transform:rotate(180deg)}
.dropdown{position:absolute;top:calc(100% + 8px);left:0;min-width:220px;
  background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:8px;
  box-shadow:0 18px 50px rgba(0,0,0,.5);opacity:0;visibility:hidden;transform:translateY(8px);
  transition:.18s}
.nav-item:hover .dropdown{opacity:1;visibility:visible;transform:translateY(0)}
.dropdown a{display:block;padding:10px 13px;border-radius:9px;font-size:14px;color:var(--muted)}
.dropdown a:hover{background:var(--surface-2);color:var(--g1)}
.cta-gold{padding:10px 20px;border-radius:999px;background:var(--grad);color:#1a130a;
  font-weight:800;font-size:14px;box-shadow:0 6px 20px rgba(195,154,92,.28)}
.cta-gold:hover{transform:translateY(-1px)}
.hamburger{display:none;width:44px;height:44px;border-radius:11px;border:1px solid var(--line);
  background:var(--surface);color:var(--text);align-items:center;justify-content:center;
  margin-left:auto;cursor:pointer;flex-direction:column;gap:4px}
.hamburger span{width:18px;height:2px;background:var(--text);border-radius:2px}

/* 모바일 패널 */
.m-panel{position:fixed;inset:0 0 0 auto;width:min(86vw,360px);background:var(--surface);
  border-left:1px solid var(--line);z-index:60;transform:translateX(100%);transition:.25s;
  overflow-y:auto;padding:20px}
.m-panel.open{transform:translateX(0)}
.m-overlay{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:55;opacity:0;
  visibility:hidden;transition:.25s}
.m-overlay.open{opacity:1;visibility:visible}
.m-close{margin-left:auto;width:40px;height:40px;border-radius:10px;border:1px solid var(--line);
  background:transparent;color:var(--text);font-size:20px;cursor:pointer}
.m-sec{border-bottom:1px solid var(--line);padding:10px 0}
.m-sec>a,.m-sec>span{display:block;padding:11px 6px;font-weight:700;font-size:15.5px}
.m-sub a{display:block;padding:8px 18px;font-size:14px;color:var(--muted)}
.m-sub a:hover{color:var(--g1)}

/* promo bar */
.promo{background:linear-gradient(135deg,#3a2a10,#1a130a);border-bottom:1px solid var(--line)}
.promo-in{max-width:var(--maxw);margin:0 auto;display:flex;align-items:center;gap:14px;
  padding:10px 24px;font-size:13.5px;flex-wrap:wrap}
.promo .pill{background:var(--grad);color:#1a130a;font-weight:800;padding:3px 11px;
  border-radius:999px;font-size:12px}
.promo .arrow{margin-left:auto;color:var(--g1);font-weight:700}

/* 컴포넌트 */
.card{background:linear-gradient(160deg,var(--surface),var(--surface-2));border:1px solid var(--line);
  border-radius:var(--radius);padding:26px}
.note-card{display:flex;gap:20px;background:linear-gradient(160deg,var(--surface),var(--surface-2));
  border:1px solid var(--line);border-radius:var(--radius);padding:28px;margin-bottom:16px;transition:.2s}
.note-card:hover{transform:translateY(-2px);border-color:rgba(195,154,92,.3)}
.note-num{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-size:40px;
  color:var(--g2);line-height:1;flex-shrink:0}
.note-title{margin-bottom:10px}
.grid{display:grid;gap:18px}
.g2{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(3,1fr)}
.tag{display:inline-block;font-size:11.5px;font-weight:700;padding:4px 10px;border-radius:999px;
  background:var(--grad-soft);color:var(--g1);border:1px solid rgba(195,154,92,.25)}
.filters{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:22px}
.chip{padding:9px 18px;border-radius:999px;border:1px solid var(--line);background:var(--surface);
  color:var(--muted);font-size:13.5px;font-weight:600;cursor:pointer;font-family:inherit;transition:.15s}
.chip:hover{border-color:var(--g2);color:var(--g1)}
.chip[aria-pressed=true]{background:var(--grad);color:#1a130a;border-color:transparent}
.no-result{color:var(--dim);padding:24px 0;display:none}
.notice-box{background:var(--grad-soft);border:1px solid rgba(195,154,92,.3);border-radius:14px;
  padding:18px 20px;font-size:13.5px;color:var(--text);line-height:1.7}
details{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:0 20px;margin-bottom:10px}
summary{padding:18px 0;font-weight:700;cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:12px}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";color:var(--g1);font-weight:800}
details[open] summary::after{content:"−"}
details p{padding-bottom:18px}
table{width:100%;border-collapse:collapse;font-size:14px}
th,td{padding:13px 14px;border-bottom:1px solid var(--line);text-align:left}
th{color:var(--g1);font-weight:700}
.field{margin-bottom:16px}
.field label{display:block;font-size:13px;font-weight:700;margin-bottom:7px}
.field label .req{color:var(--g1);margin-left:3px}
.field input,.field textarea,.field select{width:100%;background:var(--surface-2);
  border:1px solid var(--line);border-radius:10px;padding:12px 14px;color:var(--text);font-size:14px;
  font-family:inherit}
.field input:focus,.field textarea:focus,.field select:focus{outline:none;border-color:var(--g2)}
.hp{position:absolute;left:-9999px;opacity:0}

/* 푸터 */
.site-footer{border-top:1px solid var(--line);background:#08080e;margin-top:40px}
.footer-in{max-width:var(--maxw);margin:0 auto;padding:56px 24px 32px;
  display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:36px}
.footer-in h4{font-size:13px;color:var(--g1);margin-bottom:14px;letter-spacing:.04em}
.footer-in a{display:block;color:var(--muted);font-size:13.5px;padding:5px 0}
.footer-in a:hover{color:var(--g1)}
.foot-info{font-size:12.5px;color:var(--dim);line-height:1.9}
.foot-bottom{border-top:1px solid var(--line);padding:20px 24px;text-align:center;
  font-size:12px;color:var(--dim);max-width:var(--maxw);margin:0 auto}
.foot-age{display:inline-block;border:1px solid rgba(195,154,92,.3);border-radius:999px;
  padding:3px 12px;color:var(--g1);font-weight:700;font-size:12px;margin-bottom:10px}

section{margin-bottom:64px}
/* CWV: 뷰포트 밖 반복 블록 렌더 스킵(LCP↓·메인스레드↓), 실측 후 크기 기억 */
.note-card,.card,details,.site-footer{content-visibility:auto;contain-intrinsic-size:auto 280px}
@media(max-width:1100px){
  .nav-main,.nav-right{display:none}
  .hamburger{display:flex}
  .footer-in{grid-template-columns:1fr 1fr;gap:24px}
}
@media(max-width:680px){
  .g2,.g3,.footer-in{grid-template-columns:1fr}
  .wrap{padding:64px 18px}
}
@media(hover:none){.site-header{backdrop-filter:none}}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
"""

# ─────────────────────────────────────────────────────────────
def head(title, desc, path, *, og_type="website", jsonld=None, verification=False,
         modified=None, image="/assets/og.png", image_alt=None):
    c = COMPANY
    url = c["url"] + path
    img = c["url"] + image
    alt = image_alt or f'{c["name"]} — {c["tagline"]}'
    metas = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1">',
        '<meta name="theme-color" content="#0b0b12">',
        '<meta name="format-detection" content="telephone=no">',
        '<meta name="robots" content="index,follow,max-image-preview:large">',
        '<meta name="googlebot" content="index,follow">',
        '<meta name="referrer" content="strict-origin-when-cross-origin">',
        f'<title>{title}</title>',
        f'<meta name="description" content="{desc}">',
        f'<meta name="author" content="{c["name"]}">',
        f'<link rel="canonical" href="{url}">',
        f'<link rel="alternate" hreflang="ko-KR" href="{url}">',
        f'<link rel="alternate" hreflang="x-default" href="{url}">',
        f'<meta property="og:type" content="{og_type}">',
        f'<meta property="og:site_name" content="{c["name"]}">',
        '<meta property="og:locale" content="ko_KR">',
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{desc}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{img}">',
        f'<meta property="og:image:secure_url" content="{img}">',
        '<meta property="og:image:type" content="image/png">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{alt}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{desc}">',
        f'<meta name="twitter:image" content="{img}">',
        f'<meta name="twitter:image:alt" content="{alt}">',
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">',
        '<link rel="manifest" href="/site.webmanifest">',
        f'<link rel="alternate" type="application/rss+xml" title="{c["name"]} 매거진" href="/rss.xml">',
    ]
    if modified:
        metas.append(f'<meta property="og:updated_time" content="{modified}">')
        metas.append(f'<meta property="article:modified_time" content="{modified}">')
    if verification:
        if VERIFY.get("naver"):
            metas.append(f'<meta name="naver-site-verification" content="{VERIFY["naver"]}">')
        if VERIFY.get("google"):
            metas.append(f'<meta name="google-site-verification" content="{VERIFY["google"]}">')
    graph = _base_graph()
    if jsonld:
        graph += jsonld if isinstance(jsonld, list) else [jsonld]
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    return ("<!doctype html><html lang=\"ko\"><head>" + "".join(metas) +
            f'<style>{CSS_BASE}</style>' +
            f'<script type="application/ld+json">{ld}</script></head>')


def _base_graph():
    c = COMPANY
    og = {"@type": "ImageObject", "@id": c["url"] + "/#primaryimage",
          "url": c["url"] + "/assets/og.png", "width": 1200, "height": 630,
          "caption": f'{c["name"]} — {c["tagline"]}'}
    logo = {"@type": "ImageObject", "@id": c["url"] + "/#logo",
            "url": c["url"] + "/favicon.svg", "caption": c["name"]}
    return [
        {"@type": "Organization", "@id": c["url"] + "/#org", "name": c["name"],
         "legalName": c["legal_name"], "url": c["url"], "email": c["email"],
         "description": c["tagline"], "logo": logo, "image": og,
         "foundingDate": "2026", "knowsAbout": ["호빠알바 채용정보", "구직자 안전", "채용광고 검수"],
         "contactPoint": {"@type": "ContactPoint", "contactType": "customer service",
                          "email": c["email"], "availableLanguage": "Korean"}},
        {"@type": "WebSite", "@id": c["url"] + "/#site", "name": c["name"], "url": c["url"],
         "inLanguage": "ko-KR", "publisher": {"@id": c["url"] + "/#org"},
         "potentialAction": {"@type": "SearchAction",
                             "target": c["url"] + "/jobs/?q={query}", "query-input": "required name=query"}},
        og, logo,
    ]


def webpage_ld(path, name, desc, *, published=None, modified=None, breadcrumb_node=None):
    """선호 이미지(primaryImageOfPage) + 갱신일을 명시한 WebPage 노드."""
    c = COMPANY
    node = {"@type": "WebPage", "@id": c["url"] + path + "#webpage",
            "url": c["url"] + path, "name": name, "description": desc,
            "isPartOf": {"@id": c["url"] + "/#site"},
            "inLanguage": "ko-KR",
            "primaryImageOfPage": {"@id": c["url"] + "/#primaryimage"},
            "image": {"@id": c["url"] + "/#primaryimage"},
            "publisher": {"@id": c["url"] + "/#org"}}
    if published:
        node["datePublished"] = published
    if modified:
        node["dateModified"] = modified
    if breadcrumb_node:
        node["breadcrumb"] = breadcrumb_node
    return node


def breadcrumb(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n,
         "item": COMPANY["url"] + h} for i, (n, h) in enumerate(items)]}


def faq_ld(pairs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}


# ─────────────────────────────────────────────────────────────
def _dropdown(children):
    links = "".join(f'<a href="{ch["href"]}">{ch["label"]}</a>' for ch in children)
    return f'<div class="dropdown">{links}</div>'


def header_html():
    main = ""
    for it in NAV_MAIN:
        if it.get("children"):
            main += (f'<div class="nav-item"><a class="nav-link" href="{it["href"]}">'
                     f'{it["label"]}<span class="car">▼</span></a>{_dropdown(it["children"])}</div>')
        else:
            main += f'<div class="nav-item"><a class="nav-link" href="{it["href"]}">{it["label"]}</a></div>'
    right = (f'<div class="nav-item"><a class="nav-link" href="{NAV_AD["href"]}">'
             f'{NAV_AD["label"]}<span class="car">▼</span></a>{_dropdown(NAV_AD["children"])}</div>'
             f'<a class="cta-gold" href="{NAV_CONTACT["href"]}">{NAV_CONTACT["label"]}</a>')

    # 모바일 패널
    m = ""
    for it in NAV_MAIN:
        if it.get("children"):
            subs = "".join(f'<a href="{ch["href"]}">{ch["label"]}</a>' for ch in it["children"])
            m += (f'<div class="m-sec"><a href="{it["href"]}">{it["label"]}</a>'
                  f'<div class="m-sub">{subs}</div></div>')
        else:
            m += f'<div class="m-sec"><a href="{it["href"]}">{it["label"]}</a></div>'
    ad_subs = "".join(f'<a href="{ch["href"]}">{ch["label"]}</a>' for ch in NAV_AD["children"])
    m += (f'<div class="m-sec"><a href="{NAV_AD["href"]}">{NAV_AD["label"]}</a>'
          f'<div class="m-sub">{ad_subs}</div></div>'
          f'<div class="m-sec"><a href="{NAV_CONTACT["href"]}" style="color:var(--g1)">{NAV_CONTACT["label"]}</a></div>')

    return f"""<header class="site-header"><nav class="nav">
<a class="logo" href="/"><span class="mark">H</span>{COMPANY["name"]}</a>
<div class="nav-main">{main}</div>
<div class="nav-right">{right}</div>
<button class="hamburger" aria-label="메뉴 열기" onclick="window.__om()"><span></span><span></span><span></span></button>
</nav></header>
<div class="m-overlay" id="mov" onclick="window.__cm()"></div>
<aside class="m-panel" id="mp"><div style="display:flex;align-items:center">
<a class="logo" href="/"><span class="mark">H</span>{COMPANY["name"]}</a>
<button class="m-close" onclick="window.__cm()" aria-label="닫기">×</button></div>{m}</aside>"""


def promo_bar():
    return ('<div class="promo"><div class="promo-in"><span class="pill">광고안내</span>'
            '<span>호빠클럽 채용광고 등록 · VVIP/VIP/프리미엄 · 만 19세 이상 검수 게재</span>'
            '<a class="arrow" href="/advertising/">광고 알아보기 →</a></div></div>')


def footer_html():
    c = COMPANY
    cols = [
        ("채용·콘텐츠", [("채용정보", "/jobs/"), ("매거진", "/magazine/"),
                     ("안전센터", "/safety/"), ("운영 정보", "/about/"),
                     ("공지사항", "/support/notice/")]),
        ("고객·정책", [("자주 묻는 질문", "/support/faq/"), ("문의하기", "/support/contact/"),
                   ("이용약관", "/policy/terms/"), ("개인정보처리방침", "/policy/privacy/"),
                   ("청소년 보호정책", "/policy/youth/")]),
    ]
    col_html = ""
    for title, links in cols:
        ls = "".join(f'<a href="{h}">{n}</a>' for n, h in links)
        col_html += f'<div><h4>{title}</h4>{ls}</div>'
    info = (f'<div><h4>회사정보</h4><div class="foot-info">'
            f'{c["name"]} · 대표 {c["ceo"]}<br>'
            f'고객센터 {c["tel"]} ({c["tel_hours"]})<br>'
            f'이메일 {c["email"]}<br>'
            f'직업정보제공사업: {c["job_report_no"]}<br>'
            f'개인정보책임자: {c["privacy_officer"]}</div></div>')
    return f"""<footer class="site-footer"><div class="footer-in">{col_html}{info}</div>
<div class="foot-bottom"><span class="foot-age">19+ 만 19세 이상 이용</span><br>
{AGE_NOTICE}<br><br>© {c['name']}. All rights reserved.</div></footer>"""


JS = """
window.__om=function(){document.getElementById('mp').classList.add('open');document.getElementById('mov').classList.add('open')};
window.__cm=function(){document.getElementById('mp').classList.remove('open');document.getElementById('mov').classList.remove('open')};
(window.requestIdleCallback||function(f){setTimeout(f,1)})(function(){document.querySelectorAll('#mp a').forEach(function(a){a.addEventListener('click',window.__cm)})});
"""


def page(title, desc, path, body, **kw):
    return (head(title, desc, path, **kw) + "<body>" + promo_bar() + header_html() +
            "<main>" + body + "</main>" + footer_html() +
            f"<script>{JS}</script></body></html>")
