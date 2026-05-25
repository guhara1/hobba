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
  --bg:#0a0a10;--surface:#14141e;--surface-2:#1b1b28;--surface-3:#22222f;
  --line:rgba(255,255,255,.07);--line-2:rgba(255,255,255,.12);
  --text:#f4f1f9;--muted:#a7a1b8;--dim:#6f6982;
  --g1:#e6c894;--g2:#c89c5c;--g3:#8a6a38;
  --grad:linear-gradient(135deg,#e6c894 0%,#cc9f60 52%,#8a6a38 100%);
  --grad-soft:linear-gradient(150deg,rgba(230,200,148,.12),rgba(138,106,56,.04));
  --gold:#d6b274;--radius:18px;--radius-sm:12px;--maxw:1200px;--measure:720px;
  --shadow:0 1px 0 rgba(255,255,255,.03) inset,0 18px 40px -24px rgba(0,0,0,.7);
}
html{scroll-behavior:smooth;scroll-padding-top:96px}
body{background:var(--bg);color:var(--text);line-height:1.7;letter-spacing:-.011em;
  font-family:"Pretendard","Apple SD Gothic Neo","Noto Sans KR",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;
  background-image:radial-gradient(1100px 520px at 50% -160px,rgba(230,200,148,.10),transparent 70%);
  background-repeat:no-repeat}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
.serif{font-family:"Cormorant Garamond","Noto Serif KR",Georgia,serif;font-weight:300;font-style:italic}
.wrap{max-width:var(--maxw);margin:0 auto;padding:64px 24px}
.note-text{max-width:var(--measure)}
.kicker{display:inline-block;font-size:11.5px;letter-spacing:.22em;text-transform:uppercase;
  color:var(--g1);font-weight:800;margin-bottom:14px}
.gradtext{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
h1{font-size:clamp(32px,5vw,56px);font-weight:800;letter-spacing:-.038em;line-height:1.1}
h2{font-size:clamp(25px,3.4vw,38px);font-weight:800;letter-spacing:-.03em;line-height:1.18;margin-bottom:14px}
h3{font-size:clamp(16px,2vw,20px);font-weight:800;letter-spacing:-.02em;line-height:1.35}
p{color:var(--muted)}
.lead{font-size:clamp(15px,1.5vw,17px);color:var(--muted)}

/* ── 히어로 ── */
.hero{padding-top:84px;padding-bottom:44px}
.hero h1{margin-bottom:18px}
.hero-sub{font-size:clamp(15px,1.6vw,17.5px);line-height:1.75}
.hero-cta{margin-top:30px;display:flex;gap:12px;flex-wrap:wrap}
.hero-byline{margin-top:22px}
.hero-byline p{font-size:12.5px;color:var(--dim)}

/* ── 버튼 ── */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:13px 26px;
  border-radius:999px;font-weight:700;font-size:14px;line-height:1;transition:transform .18s,border-color .18s,background .18s;
  border:1px solid transparent;cursor:pointer;font-family:inherit}
.btn-gold{background:var(--grad);color:#15100a;box-shadow:0 10px 28px -10px rgba(200,156,92,.6)}
.btn-gold:hover{transform:translateY(-2px)}
.btn-ghost{border-color:var(--line-2);color:var(--text);background:rgba(255,255,255,.02)}
.btn-ghost:hover{border-color:var(--g2);color:var(--g1);background:rgba(230,200,148,.06)}

/* ── 헤더 ── */
.site-header{position:sticky;top:0;z-index:50;background:rgba(10,10,16,.72);
  backdrop-filter:saturate(140%) blur(16px);border-bottom:1px solid var(--line)}
.nav{max-width:var(--maxw);margin:0 auto;display:flex;align-items:center;gap:10px;padding:13px 24px}
.logo{display:flex;align-items:center;gap:10px;font-weight:800;font-size:19px;flex-shrink:0;letter-spacing:-.02em}
.logo .mark{width:32px;height:32px;border-radius:10px;background:var(--grad);
  display:grid;place-items:center;color:#15100a;font-weight:900;font-size:16px;box-shadow:0 6px 16px -6px rgba(200,156,92,.7)}
.nav-main{display:flex;align-items:center;gap:2px;margin-left:18px}
.nav-right{display:flex;align-items:center;gap:8px;margin-left:auto}
.nav-item{position:relative}
.nav-link{display:inline-flex;align-items:center;gap:5px;padding:9px 14px;border-radius:10px;
  font-size:14.5px;font-weight:600;color:var(--text);white-space:nowrap;transition:.15s}
.nav-link:hover{background:rgba(255,255,255,.05);color:var(--g1)}
.nav-link .car{font-size:8px;opacity:.55;transition:transform .2s}
.nav-item:hover .car{transform:rotate(180deg)}
.dropdown{position:absolute;top:calc(100% + 10px);left:0;min-width:236px;
  background:rgba(20,20,30,.98);border:1px solid var(--line-2);border-radius:16px;padding:8px;
  box-shadow:0 24px 60px -16px rgba(0,0,0,.75);opacity:0;visibility:hidden;transform:translateY(10px) scale(.98);
  transform-origin:top left;transition:.18s}
.dropdown::before{content:"";position:absolute;top:-10px;left:0;right:0;height:10px}
.nav-item:hover .dropdown{opacity:1;visibility:visible;transform:translateY(0) scale(1)}
.dropdown a{display:block;padding:11px 14px;border-radius:10px;font-size:14px;color:var(--muted);
  font-weight:500;transition:.13s}
.dropdown a:hover{background:rgba(230,200,148,.08);color:var(--g1);transform:translateX(2px)}
.cta-gold{padding:10px 20px;border-radius:999px;background:var(--grad);color:#15100a;
  font-weight:800;font-size:14px;box-shadow:0 10px 24px -10px rgba(200,156,92,.65);transition:transform .18s}
.cta-gold:hover{transform:translateY(-1px)}
.hamburger{display:none;width:44px;height:44px;border-radius:12px;border:1px solid var(--line-2);
  background:var(--surface);color:var(--text);align-items:center;justify-content:center;
  margin-left:auto;cursor:pointer;flex-direction:column;gap:4px}
.hamburger span{width:18px;height:2px;background:var(--text);border-radius:2px}

/* 모바일 패널 */
.m-panel{position:fixed;inset:0 0 0 auto;width:min(88vw,370px);background:var(--surface);
  border-left:1px solid var(--line-2);z-index:60;transform:translateX(100%);transition:.28s cubic-bezier(.4,0,.2,1);
  overflow-y:auto;padding:18px 20px}
.m-panel.open{transform:translateX(0)}
.m-overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:55;opacity:0;
  visibility:hidden;transition:.25s;backdrop-filter:blur(2px)}
.m-overlay.open{opacity:1;visibility:visible}
.m-close{margin-left:auto;width:40px;height:40px;border-radius:11px;border:1px solid var(--line-2);
  background:transparent;color:var(--text);font-size:20px;cursor:pointer}
.m-sec{border-bottom:1px solid var(--line);padding:6px 0}
.m-sec>a,.m-sec>span{display:block;padding:12px 6px;font-weight:700;font-size:15.5px}
.m-sub{padding-bottom:6px}
.m-sub a{display:block;padding:9px 16px;font-size:14px;color:var(--muted);border-radius:8px}
.m-sub a:hover{color:var(--g1);background:rgba(255,255,255,.04)}

/* promo bar */
.promo{background:linear-gradient(135deg,#33260f,#15100a);border-bottom:1px solid var(--line)}
.promo-in{max-width:var(--maxw);margin:0 auto;display:flex;align-items:center;gap:14px;
  padding:10px 24px;font-size:13px;flex-wrap:wrap;color:var(--muted)}
.promo .pill{background:var(--grad);color:#15100a;font-weight:800;padding:4px 11px;border-radius:999px;font-size:11.5px}
.promo .arrow{margin-left:auto;color:var(--g1);font-weight:700;white-space:nowrap}

/* ── 카드 ── */
.card{background:linear-gradient(160deg,var(--surface),var(--surface-2));border:1px solid var(--line);
  border-radius:var(--radius);padding:26px;box-shadow:var(--shadow);transition:transform .2s,border-color .2s}
a.card:hover,.card-h:hover{transform:translateY(-3px);border-color:rgba(230,200,148,.32)}
.note-card{display:flex;gap:22px;background:linear-gradient(160deg,var(--surface),var(--surface-2));
  border:1px solid var(--line);border-radius:var(--radius);padding:26px 28px;margin-bottom:14px;
  box-shadow:var(--shadow);transition:transform .2s,border-color .2s;position:relative;overflow:hidden}
.note-card::before{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--grad);
  opacity:0;transition:.2s}
.note-card:hover{transform:translateY(-2px);border-color:rgba(230,200,148,.28)}
.note-card:hover::before{opacity:1}
.note-num{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-size:42px;
  color:var(--g2);line-height:.9;flex-shrink:0;width:46px}
.note-title{margin-bottom:9px}
.note-card p{font-size:14.5px;line-height:1.72}
.grid{display:grid;gap:18px}
.g2{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(3,1fr)}
.tag{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.02em;padding:5px 11px;
  border-radius:999px;background:var(--grad-soft);color:var(--g1);border:1px solid rgba(230,200,148,.28)}
.filters{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:24px}
.chip{padding:9px 18px;border-radius:999px;border:1px solid var(--line-2);background:rgba(255,255,255,.02);
  color:var(--muted);font-size:13.5px;font-weight:600;cursor:pointer;font-family:inherit;transition:.15s}
.chip:hover{border-color:var(--g2);color:var(--g1)}
.chip[aria-pressed=true]{background:var(--grad);color:#15100a;border-color:transparent}
.no-result{color:var(--dim);padding:24px 0;display:none}

/* 광고 배너(가로 4개) */
.ad-row-head{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:14px}
.ad-row-head .lbl{display:inline-flex;align-items:center;gap:8px;font-size:13.5px;letter-spacing:.1em;
  text-transform:uppercase;font-weight:800}
.ad-row-head a{font-size:13px;color:var(--g1);font-weight:600;white-space:nowrap}
.lbl .ic{font-size:16px;line-height:1;display:inline-block;animation:adbob 2.4s ease-in-out infinite;
  filter:drop-shadow(0 2px 6px rgba(200,156,92,.45))}
.lbl .tx-vvip{background:linear-gradient(90deg,#e6c894,#fff1d2 30%,#c89c5c 55%,#e6c894);
  background-size:220% auto;-webkit-background-clip:text;background-clip:text;
  -webkit-text-fill-color:transparent;color:transparent;animation:shimmer 3.2s linear infinite}
.lbl .tx-vip{color:var(--g1)}
.lbl .tx-prem{color:var(--g2)}
.lbl.vip .ic{animation-delay:.3s}.lbl.prem .ic{animation-delay:.6s}
@keyframes adbob{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}
@keyframes shimmer{0%{background-position:0 center}100%{background-position:220% center}}
.ad-banner-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.ad-banner{position:relative;display:flex;flex-direction:column;gap:8px;min-height:150px;
  padding:20px;border-radius:var(--radius);border:1px solid rgba(230,200,148,.3);
  background:linear-gradient(160deg,rgba(230,200,148,.12),rgba(138,106,56,.05)),var(--surface);
  box-shadow:var(--shadow);transition:transform .2s,border-color .2s}
.ad-banner:hover{transform:translateY(-3px);border-color:var(--g2)}
.ad-banner .b-badge{align-self:flex-start;font-size:10.5px;font-weight:800;letter-spacing:.08em;
  padding:3px 9px;border-radius:999px;background:var(--grad);color:#15100a}
.ad-banner .b-title{font-size:16px;font-weight:800;margin-top:2px}
.ad-banner .b-area{font-size:12.5px;color:var(--dim)}
.ad-banner .b-copy{font-size:13px;color:var(--muted);margin-top:auto}
.ad-banner .b-sample{position:absolute;top:14px;right:14px;font-size:10px;color:var(--dim);
  border:1px solid var(--line-2);border-radius:999px;padding:2px 8px}

/* 메인 광고 쇼케이스 — 3등급 시각 차등 */
/* VVIP: 골드 충진+글로우+랭킹넘버, 가장 큼 */
.vvip-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.vvip-banner{position:relative;overflow:hidden;display:flex;flex-direction:column;min-height:190px;
  padding:24px;border-radius:20px;border:1px solid rgba(238,205,140,.6);
  background:radial-gradient(130% 150% at 0% 0%,rgba(244,210,142,.30),transparent 56%),linear-gradient(160deg,#2b2215,#191309);
  box-shadow:0 22px 48px -26px rgba(200,156,92,.7);transition:transform .22s,box-shadow .22s}
.vvip-banner:hover{transform:translateY(-4px);box-shadow:0 30px 64px -24px rgba(200,156,92,.8)}
.vvip-banner::before{content:"";position:absolute;left:0;right:0;top:0;height:3px;background:var(--grad)}
.vvip-rank{position:absolute;top:6px;right:18px;font-family:"Cormorant Garamond",Georgia,serif;
  font-style:italic;font-size:68px;line-height:1;color:rgba(246,214,150,.30)}
.vvip-badge{align-self:flex-start;font-size:11px;font-weight:900;letter-spacing:.1em;padding:4px 12px;
  border-radius:999px;background:var(--grad);color:#15100a;box-shadow:0 8px 18px -6px rgba(200,156,92,.85)}
.vvip-banner .t{font-size:19px;font-weight:800;letter-spacing:-.02em;margin-top:12px;color:#fdf6e7}
.vvip-banner .a{font-size:13px;color:#e7d9b8;font-weight:500;margin-top:5px}
.vvip-banner .c{margin-top:auto;padding-top:14px;font-size:13.5px;color:#f4ce86;font-weight:700}
/* VIP: 중간 — 골드 테두리, 랭킹 없음, 4열 */
.vip-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:13px}
.vip-banner{position:relative;overflow:hidden;display:flex;flex-direction:column;gap:5px;min-height:128px;padding:18px;
  border-radius:15px;border:1px solid rgba(230,200,148,.38);
  background:linear-gradient(160deg,#242531,#191a25);
  transition:transform .18s,border-color .18s,box-shadow .18s}
.vip-banner::before{content:"";position:absolute;left:0;right:0;top:0;height:2px;
  background:linear-gradient(90deg,var(--g2),transparent 72%)}
.vip-banner:hover{transform:translateY(-3px);border-color:var(--g2);box-shadow:0 16px 36px -22px rgba(200,156,92,.5)}
.vip-badge{align-self:flex-start;font-size:10.5px;font-weight:800;letter-spacing:.08em;padding:3px 10px;
  border-radius:999px;color:var(--g1);border:1px solid rgba(230,200,148,.5);background:rgba(230,200,148,.1)}
.vip-banner .t{font-size:17px;font-weight:800;letter-spacing:-.01em;margin-top:6px;color:#fdf6e7}
.vip-banner .a{font-size:13px;color:#e7d9b8;font-weight:500;margin-top:2px}
.vip-banner .c{margin-top:auto;font-size:13px;color:#f4ce86;font-weight:700}
/* 프리미엄(일반): 한줄광고 리스트형 */
.linead{border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--surface)}
.linead a{display:flex;align-items:center;gap:14px;padding:14px 18px;border-bottom:1px solid var(--line);transition:background .13s}
.linead a:last-child{border-bottom:none}
.linead a:hover{background:rgba(230,200,148,.05)}
.linead .nm{flex:0 0 92px;font-weight:700;font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.linead .cp{flex:1 1 auto;min-width:0;color:var(--g1);font-size:13.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.linead .ar{flex:0 0 auto;display:inline-flex;align-items:center;gap:4px;color:var(--dim);font-size:12.5px;white-space:nowrap}
.linead .ar svg{opacity:.7}
.linead .u{flex:0 0 auto;font-size:11px;font-weight:800;padding:3px 9px;border-radius:7px}
.linead .u.tc{background:rgba(202,120,42,.22);color:#f0b277;border:1px solid rgba(202,120,42,.5)}
.linead .u.hr{background:rgba(72,108,206,.22);color:#a9c2ff;border:1px solid rgba(72,108,206,.5)}
.linead .pr{flex:0 0 92px;text-align:right;font-weight:800;font-size:14px;white-space:nowrap}
@media(max-width:680px){
  .linead a{flex-wrap:wrap;gap:8px 12px}
  .linead .nm{flex-basis:auto}
  .linead .cp{order:5;flex-basis:100%}
  .linead .pr{flex-basis:auto;margin-left:auto}
}

/* 19+ 성인 인증 게이트 */
.agegate{position:fixed;inset:0;z-index:9999;background:rgba(6,6,11,.94);backdrop-filter:blur(10px);
  display:none;align-items:center;justify-content:center;padding:24px}
.agegate-box{max-width:448px;width:100%;background:linear-gradient(165deg,var(--surface-2),var(--surface));
  border:1px solid var(--line-2);border-radius:22px;padding:44px 34px;text-align:center;
  box-shadow:0 40px 90px -30px rgba(0,0,0,.85)}
.agegate-badge{width:76px;height:76px;border-radius:50%;background:var(--grad);color:#15100a;
  font-weight:900;font-size:23px;display:grid;place-items:center;margin:0 auto 22px;
  box-shadow:0 14px 30px -10px rgba(200,156,92,.7)}
.agegate-box h2{font-size:23px;margin-bottom:14px}
.agegate-box p{font-size:14px;margin-bottom:8px;line-height:1.65}
.agegate-actions{display:flex;flex-direction:column;gap:10px;margin:28px 0 14px}
.agegate-note{font-size:12px;color:var(--dim)}

/* 안내 박스 */
.notice-box{background:var(--grad-soft);border:1px solid rgba(230,200,148,.26);border-radius:var(--radius-sm);
  padding:18px 22px;font-size:13.5px;color:var(--text);line-height:1.72}

/* details / FAQ */
details{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-sm);
  padding:0 22px;margin-bottom:10px;transition:border-color .18s}
details[open]{border-color:var(--line-2)}
summary{padding:18px 0;font-weight:700;font-size:15px;cursor:pointer;list-style:none;
  display:flex;justify-content:space-between;gap:14px;align-items:center}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";color:var(--g1);font-weight:800;font-size:18px;flex-shrink:0}
details[open] summary::after{content:"\\2212"}
details p{padding-bottom:18px;font-size:14px;line-height:1.72}

/* 테이블 */
.table-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:var(--radius-sm)}
table{width:100%;border-collapse:collapse;font-size:14px;min-width:480px}
th,td{padding:14px 16px;border-bottom:1px solid var(--line);text-align:left}
tr:last-child td{border-bottom:none}
th{color:var(--g1);font-weight:700;background:rgba(255,255,255,.02);font-size:13px;letter-spacing:.01em}

/* 폼 */
.field{margin-bottom:18px}
.field label{display:block;font-size:13px;font-weight:700;margin-bottom:8px}
.field label .req{color:var(--g1);margin-left:3px}
.field input,.field textarea,.field select{width:100%;background:var(--surface-2);
  border:1px solid var(--line-2);border-radius:11px;padding:13px 15px;color:var(--text);font-size:14.5px;
  font-family:inherit;transition:border-color .15s,box-shadow .15s}
.field input::placeholder,.field textarea::placeholder{color:var(--dim)}
.field input:focus,.field textarea:focus,.field select:focus{outline:none;border-color:var(--g2);
  box-shadow:0 0 0 3px rgba(230,200,148,.12)}
.hp{position:absolute;left:-9999px;opacity:0}

/* 본문 가독(article) */
.prose{max-width:760px;font-size:17px}
.prose h2{font-size:clamp(21px,2.6vw,26px);margin:0 0 16px;color:#ffffff;letter-spacing:-.02em;line-height:1.3}
.prose p{font-size:17px;line-height:1.95;margin-bottom:18px;color:#f1eef8;font-weight:400;word-break:keep-all}
.prose p:last-child{margin-bottom:0}
.prose strong{color:#fff;font-weight:700}
.prose a{color:var(--g1);text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px;text-decoration-color:rgba(230,200,148,.45)}
.prose a:hover{text-decoration-color:var(--g1)}
.prose section{margin-bottom:30px!important}
.prose section:last-child{margin-bottom:0!important}

/* 블로그/안전센터 글: 밝은 읽기 시트 (다크 사이트 + 라이트 본문) */
.reading{max-width:900px;margin:0 auto;padding:36px 18px 56px}
.reading-sheet{
  --text:#1c1b24;--muted:#57545f;--dim:#7c7886;--g1:#9a6a10;--g2:#7c5410;
  --line:rgba(20,18,30,.12);--line-2:rgba(20,18,30,.2);
  --surface:#ffffff;--surface-2:#f5f1e9;--surface-3:#efe9dd;
  --grad-soft:linear-gradient(150deg,#f7efdd,#f1e6cc);
  --shadow:0 8px 24px -16px rgba(0,0,0,.25);
  background:#fbf9f4;color:#26242e;border-radius:22px;
  padding:clamp(26px,5vw,56px);border:1px solid rgba(0,0,0,.06);
  box-shadow:0 26px 70px -34px rgba(0,0,0,.7)}
.reading-sheet h1{color:#17161d}
.reading-sheet .lead{color:#57545f}
.reading-sheet .prose{font-size:17px}
.reading-sheet .prose h2{color:#191820}
.reading-sheet .prose p{color:#333039}
.reading-sheet .prose strong{color:#000}
.reading-sheet .prose a{text-decoration-color:rgba(154,106,16,.45)}
.reading-sheet .prose a:hover{text-decoration-color:#9a6a10}
.reading-sheet .toc-card{background:#f3eee2}
.reading-sheet .notice-box{border-color:#e7d4a3}
.reading-sheet .card{box-shadow:0 8px 22px -14px rgba(0,0,0,.22)}
@media(max-width:680px){.reading{padding:18px 10px 40px}}
.toc-card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius-sm);padding:20px 24px}
.toc-card strong{font-size:13px;letter-spacing:.04em;color:var(--g1);text-transform:uppercase}
.toc-card ul{margin-top:12px;padding-left:18px}
.toc-card li{margin-bottom:7px;color:var(--muted);font-size:14.5px}
.toc-card a:hover{color:var(--g1)}

/* 푸터 */
.site-footer{border-top:1px solid var(--line);background:#070709;margin-top:24px}
.footer-in{max-width:var(--maxw);margin:0 auto;padding:60px 24px 36px;
  display:grid;grid-template-columns:1.5fr 1fr 1.3fr;gap:40px}
.footer-in h4{font-size:12px;color:var(--g1);margin-bottom:16px;letter-spacing:.08em;text-transform:uppercase}
.footer-in a{display:block;color:var(--muted);font-size:13.5px;padding:5px 0;transition:.13s}
.footer-in a:hover{color:var(--g1)}
.foot-info{font-size:12.5px;color:var(--dim);line-height:1.95}
.foot-bottom{border-top:1px solid var(--line);padding:22px 24px;text-align:center;
  font-size:12px;color:var(--dim);max-width:var(--maxw);margin:0 auto;line-height:1.7}
.foot-age{display:inline-block;border:1px solid rgba(230,200,148,.3);border-radius:999px;
  padding:4px 13px;color:var(--g1);font-weight:700;font-size:12px;margin-bottom:12px}

/* 섹션 리듬 — .wrap 자체 패딩으로 일관 간격(이중 마진 제거) */
section{margin:0}
/* CWV: 화면 밖 큰 블록만 렌더 스킵(카드 그리드는 스크롤 끊김 방지 위해 제외) */
.site-footer{content-visibility:auto;contain-intrinsic-size:auto 360px}
@media(max-width:1100px){
  .nav-main,.nav-right{display:none}
  .hamburger{display:flex}
  .footer-in{grid-template-columns:1fr 1fr;gap:28px}
  .wrap{padding:52px 22px}
  .hero{padding-top:60px;padding-bottom:36px}
}
@media(max-width:900px){
  .ad-banner-grid,.vvip-grid,.vip-grid{grid-template-columns:repeat(2,1fr)}
}
@media(max-width:680px){
  .g2,.g3,.footer-in,.ad-banner-grid,.vvip-grid,.vip-grid{grid-template-columns:1fr}
  .wrap{padding:48px 18px}
  .note-card{padding:22px;gap:16px}
  .note-num{font-size:34px;width:36px}
}
@media(hover:none){.site-header{backdrop-filter:none}}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important;scroll-behavior:auto}}
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
         "telephone": c["tel"], "taxID": c["biz_no"],
         "founder": {"@type": "Person", "name": c["ceo"]},
         "address": {"@type": "PostalAddress", "addressCountry": "KR",
                     "streetAddress": c["address"]},
         "foundingDate": "2026",
         "knowsAbout": ["호빠", "호스트바", "호빠알바", "선수 채용", "남성 호스트 구인구직", "구직자 안전"],
         "contactPoint": {"@type": "ContactPoint", "contactType": "customer service",
                          "telephone": c["tel"], "email": c["email"], "availableLanguage": "Korean"}},
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
            '<span>호빠클럽 채용광고 등록 · VVIP/VIP/Special · 만 19세 이상 검수 게재</span>'
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
            f'상호 {c["legal_name"]} ({c["name"]}) · 대표 {c["ceo"]}<br>'
            f'사업자등록번호 {c["biz_no"]}<br>'
            f'직업정보제공사업 신고 {c["job_report_no"]}<br>'
            f'{c["address"]}<br>'
            f'고객센터 {c["tel"]} ({c["tel_hours"]})<br>'
            f'이메일 {c["email"]} · 개인정보책임자 {c["privacy_officer"]}</div></div>')
    return f"""<footer class="site-footer"><div class="footer-in">{col_html}{info}</div>
<div class="foot-bottom"><span class="foot-age">19+ 만 19세 이상 이용</span><br>
{AGE_NOTICE}<br><br>© {c['name']}. All rights reserved.</div></footer>"""


def age_gate():
    return (
        '<div id="agegate" class="agegate" role="dialog" aria-modal="true" aria-label="성인 인증">'
        '<div class="agegate-box"><div class="agegate-badge">19+</div>'
        '<h2>성인 인증이 필요합니다</h2>'
        '<p>본 사이트는 만 19세 이상만 이용하는 호빠·호스트바 선수(남성 호스트) 채용정보 플랫폼입니다.</p>'
        '<p>만 19세 이상만 이용할 수 있으며, 휴대폰 본인인증 후 입장할 수 있습니다.</p>'
        '<div class="agegate-actions">'
        '<button class="btn btn-gold" onclick="window.__ageEnter()">휴대폰 본인인증하고 입장</button>'
        '<button class="btn btn-ghost" onclick="window.__ageExit()">나가기</button></div>'
        '<p class="agegate-note">만 19세 미만은 이용할 수 없습니다.</p></div></div>'
        '<script>(function(){try{if(localStorage.getItem("hobba_adult")==="1")return}catch(e){}'
        'var g=document.getElementById("agegate");if(g){g.style.display="flex";'
        'document.documentElement.style.overflow="hidden"}})();</script>')


JS = """
window.__om=function(){document.getElementById('mp').classList.add('open');document.getElementById('mov').classList.add('open')};
window.__cm=function(){document.getElementById('mp').classList.remove('open');document.getElementById('mov').classList.remove('open')};
window.__ageClose=function(){try{localStorage.setItem('hobba_adult','1')}catch(e){}var g=document.getElementById('agegate');if(g)g.style.display='none';document.documentElement.style.overflow=''};
window.__ageEnter=function(){if(typeof window.__kcpCert==='function'){window.__kcpCert();return}window.__ageClose()};
window.__ageExit=function(){location.href='https://www.google.com'};
(window.requestIdleCallback||function(f){setTimeout(f,1)})(function(){document.querySelectorAll('#mp a').forEach(function(a){a.addEventListener('click',window.__cm)})});
"""


def page(title, desc, path, body, **kw):
    return (head(title, desc, path, **kw) + "<body>" + age_gate() + promo_bar() + header_html() +
            "<main>" + body + "</main>" + footer_html() +
            f"<script>{JS}</script></body></html>")
