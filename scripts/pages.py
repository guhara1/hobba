# -*- coding: utf-8 -*-
"""페이지 빌더: 각 함수는 (path, html)를 반환."""
from data import (COMPANY, HOME_ADS, JOBS_FAQ, AD_PRODUCTS, AD_FAQ, AD_INQUIRY_TEL,
                  AGE_NOTICE, EDITORIAL, TRUST_SOURCES, LAST_UPDATED)
from content import MAGAZINE, SAFETY, SAFETY_SOURCES, NOTICES, SUPPORT_FAQ, POLICIES
from templates import page, breadcrumb, faq_ld, webpage_ld

C = COMPANY


def _note(num, title, paras):
    ps = "".join(f"<p>{p}</p>" for p in paras)
    return (f'<div class="note-card"><div class="note-num">{num:02d}</div>'
            f'<div><h3 class="note-title">{title}</h3><div class="note-text">{ps}</div></div></div>')


def _hero(kicker, h1, sub, ctas="", byline=""):
    cta = f'<div class="hero-cta">{ctas}</div>' if ctas else ""
    bl = f'<div class="hero-byline">{byline}</div>' if byline else ""
    return (f'<section class="wrap hero"><span class="kicker">{kicker}</span>'
            f'<h1>{h1}</h1><p class="hero-sub note-text">{sub}</p>{cta}{bl}</section>')


def _faq_section(pairs, title="자주 묻는 질문"):
    items = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in pairs)
    return f'<section class="wrap" style="padding-top:0"><h2>{title}</h2>{items}</section>'


# ─────────────────────────────────────────────────────────────
def _byline():
    return (f'<p style="font-size:13px;color:var(--dim)">'
            f'작성·검수 <a href="/about/" style="color:var(--g1)">{EDITORIAL["byline"]}</a>'
            f' · 최종 업데이트 {LAST_UPDATED}</p>')


def _promo_entries():
    """배너 → 샘플 홍보 상세 페이지 항목. (id, 등급, 데이터)"""
    A = HOME_ADS
    out = []
    for i, b in enumerate(A["vvip"]):
        out.append((f"vvip-{i+1}", "VVIP", b))
    for i, b in enumerate(A["vip"]):
        out.append((f"vip-{i+1}", "VIP", b))
    for i, b in enumerate(A["premium"]):
        out.append((f"prem-{i+1}", "프리미엄", b))
    return out


def _ad_showcase():
    A = HOME_ADS
    vvip = "".join(
        f'<a class="vvip-banner" href="/promo/vvip-{i+1}/"><span class="vvip-rank">{b["rank"]}</span>'
        f'<span class="vvip-badge">VVIP</span>'
        f'<span class="t">{b["title"]}</span><span class="a">{b["area"]} · {b["tag"]}</span>'
        f'<span class="c">{b["copy"]} →</span></a>' for i, b in enumerate(A["vvip"]))
    vip = "".join(
        f'<a class="vip-banner" href="/promo/vip-{i+1}/"><span class="vip-badge">VIP</span>'
        f'<span class="t">{b["title"]}</span><span class="a">{b["area"]}</span>'
        f'<span class="c">{b["copy"]}</span></a>' for i, b in enumerate(A["vip"]))
    pin = ('<svg width="11" height="11" viewBox="0 0 24 24" fill="currentColor">'
           '<path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5z"/></svg>')
    prem = '<div class="linead">' + "".join(
        f'<a href="/promo/prem-{i+1}/"><span class="nm">{b["name"]}</span>'
        f'<span class="cp">{b["copy"]}</span>'
        f'<span class="ar">{pin}{b["area"]}</span>'
        f'<span class="u {"tc" if b["unit"]=="TC" else "hr"}">{b["unit"]}</span>'
        f'<span class="pr">{b["price"]}</span></a>'
        for i, b in enumerate(A["premium"])) + '</div>'
    return (
        '<section class="wrap" style="padding-top:0">'
        '<div class="ad-row-head"><span class="lbl vvip"><span class="ic">👑</span>'
        '<span class="tx-vvip">VVIP 추천 광고</span></span>'
        '<a href="/advertising/">광고 게재 안내 →</a></div>'
        f'<div class="vvip-grid">{vvip}</div>'
        '<div class="ad-row-head" style="margin-top:32px"><span class="lbl vip"><span class="ic">💎</span>'
        '<span class="tx-vip">VIP 광고</span></span></div>'
        f'<div class="vip-grid">{vip}</div>'
        '<div class="ad-row-head" style="margin-top:32px"><span class="lbl prem"><span class="ic">✨</span>'
        '<span class="tx-prem">프리미엄 광고 · 한줄광고</span></span></div>'
        f'{prem}'
        '<p style="font-size:12px;color:var(--dim);margin-top:16px">※ 위 배너는 게재 형식을 보여주는 샘플입니다. '
        '실제 광고는 매장의 광고 등록 후 등급(VVIP·VIP·프리미엄)별로 차등 노출됩니다.</p>'
        '</section>')


def home():
    ad_showcase = _ad_showcase()
    steps = [("01", "공고 탐색", "지역·형태별로 검수된 채용정보를 살펴봅니다."),
             ("02", "조건 확인", "업무·급여·정산 방식을 가이드와 함께 확인합니다."),
             ("03", "안전 점검", "안전센터 체크리스트로 위험 신호를 거릅니다."),
             ("04", "지원·문의", "공고 안내에 따라 지원하거나 문의합니다.")]
    step_html = "".join(_note(int(n), t, [d]) for n, t, d in steps)

    # Who / How / Why (E-E-A-T, 2025.12 가이드라인)
    whw = "".join(_note(i + 1, t, [d]) for i, (t, d) in enumerate([
        ("누가 만드나요 (Who)", EDITORIAL["who"]),
        ("어떻게 만드나요 (How)", EDITORIAL["how"]),
        ("왜 만드나요 (Why)", EDITORIAL["why"])]))

    # 외부 권위 출처(신뢰 신호)
    src = "".join(
        f'<a class="card" href="{u}" target="_blank" rel="nofollow noopener" style="display:block">'
        f'<h3 style="font-size:16px">{n}</h3><p style="font-size:13px;margin-top:6px">{d}</p></a>'
        for n, d, u in TRUST_SOURCES)

    body = (
        _hero("HOBBA CLUB",
              '안전하게 시작하는 <span class="gradtext">호빠·호스트바 선수 채용</span>',
              "호빠클럽은 만 19세 이상 호빠·호스트바 선수(남성 호스트) 채용정보 플랫폼입니다. 호빠알바 구인구직, 운영·편집팀이 직접 검수한 선수 모집 공고와 안전 가이드로 더 안심하고 일자리를 찾으세요.",
              '<a class="btn btn-gold" href="/jobs/">채용정보 보기</a>'
              '<a class="btn btn-ghost" href="/safety/">안전센터 둘러보기</a>',
              byline=_byline()) +
        ad_showcase +
        f'<section class="wrap" style="padding-top:0"><span class="kicker">HOW IT WORKS</span>'
        f'<h2 style="margin:12px 0 24px">이렇게 이용하세요</h2>{step_html}</section>'
        f'<section class="wrap" style="padding-top:0"><span class="kicker">누가·어떻게·왜</span>'
        f'<h2 style="margin:12px 0 12px">호빠클럽은 이렇게 만듭니다</h2>'
        f'<p class="note-text" style="margin-bottom:24px">콘텐츠를 누가, 어떻게, 왜 만드는지 투명하게 공개합니다. '
        f'자세한 편집 원칙은 <a href="/about/" style="color:var(--g1)">운영 정보</a>에서 확인하세요.</p>{whw}</section>'
        f'<section class="wrap" style="padding-top:0"><span class="kicker">신뢰할 수 있는 도움</span>'
        f'<h2 style="margin:12px 0 8px">공식 신고·상담 창구</h2>'
        f'<p class="note-text" style="margin-bottom:20px">위급하거나 불법 요구를 받았다면 아래 공식 기관에서 도움을 받을 수 있습니다.</p>'
        f'<div class="grid g2">{src}</div></section>'
        f'<section class="wrap" style="padding-top:0"><div class="notice-box">{AGE_NOTICE}</div></section>' +
        _faq_section(SUPPORT_FAQ[:5])
    )
    ld = [webpage_ld("/", f'{C["name"]} | 호빠·호스트바 선수 채용정보 (호빠알바 구인구직)',
                     '만 19세 이상 호빠·호스트바 선수(남성 호스트) 채용정보 플랫폼.',
                     published="2026-01-01", modified=LAST_UPDATED),
          {"@type": "CollectionPage", "name": C["name"], "url": C["url"] + "/"},
          faq_ld(SUPPORT_FAQ[:5])]
    return "/index.html", page(
        f'{C["name"]} | 호빠·호스트바 선수 채용 (호빠알바 구인구직)',
        '만 19세 이상 호빠·호스트바 선수(남성 호스트) 채용정보. 검수된 공고와 안전 가이드를 제공하는 호빠알바 구인구직.',
        "/", body, jsonld=ld, verification=True, modified=LAST_UPDATED)


def jobs():
    # 상단: 메인과 동일한 3등급 광고 쇼케이스
    banner_section = _ad_showcase()

    # 하단: 콘텐츠 글
    checklist = [("01", "일의 성격", "무슨 일을 하는지 구체적으로 적혀 있는지 봅니다. 설명을 피하는 공고는 주의합니다."),
                 ("02", "수입 구조", "‘예상 수입’이 아닌 보장급이 얼마인지, TC·인센티브 산정을 확인합니다."),
                 ("03", "정산 주기", "일·주·월 중 언제, 어떤 방식으로 정산하는지 확인합니다."),
                 ("04", "근무 시간", "출퇴근 시간과 휴게, 야간 비중을 따져 봅니다."),
                 ("05", "계약 여부", "근로조건을 서면으로 남기는지 확인합니다.")]
    chk = "".join(_note(int(n), t, [d]) for n, t, d in checklist)

    content = (
        '<article class="wrap" style="max-width:840px;padding-top:0">'
        '<span class="kicker">채용정보 가이드</span>'
        '<h2>호빠·호스트바 선수 채용, 시작 전에 알아두기</h2>'
        '<div class="prose">'
        '<p>호빠·호스트바 선수(남성 호스트)는 매장을 방문한 손님을 응대하며 대화와 서비스로 즐거운 시간을 만드는 일입니다. '
        '경험이 없어도 교육을 통해 시작할 수 있고, 경력에 따라 단골 관리와 매출 기여로 더 높은 수입을 기대할 수 있습니다. '
        '호빠클럽은 만 19세 이상만 이용하는 채용정보 플랫폼으로, 검수 정책에 따라 게재된 공고만 노출합니다.</p>'
        '<p>매장마다 업무 범위·근무 형태·수입 구조가 다르므로, 지원 전에 공고를 정확히 읽고 면접에서 조건을 확인하는 것이 가장 중요합니다. '
        '신입·경력 등 어떤 단계든 확인할 핵심은 같습니다 — 보장급·정산·근무 조건을 기록으로 남기세요.</p>'
        '</div>'
        '<h3 style="margin:30px 0 18px;font-size:19px">채용정보, 이 5가지를 먼저 확인하세요</h3>'
        f'{chk}'
        '<div class="prose" style="margin-top:30px">'
        '<h2 style="font-size:24px">‘예상 수입’과 ‘보장급’은 다릅니다</h2>'
        '<p>호스트 수입은 보통 보장급(일급)·TC(테이블 차지)·인센티브로 구성됩니다. 공고에 적힌 ‘예상 수입’은 최대치인 경우가 많으니, '
        '보장급이 얼마인지와 TC·인센티브 산정 방식, 정산 주기·공제 항목을 기준으로 판단하세요. '
        '자세한 내용은 <a href="/magazine/work-conditions/" style="color:var(--g1)">수입·정산 정보</a>에서 확인할 수 있습니다.</p>'
        '<h2 style="font-size:24px;margin-top:28px">안전하게 지원하기</h2>'
        '<p>정상적인 채용은 구직자에게 선불금·보증금을 먼저 요구하지 않습니다. 성매매를 암시하거나 불법 행위를 전제로 하는 제안은 '
        '응할 의무가 없으며 즉시 신고할 수 있습니다. 지원 전 '
        '<a href="/safety/interview-safety/" style="color:var(--g1)">안전한 면접 체크</a>와 '
        '<a href="/magazine/interview-guide/" style="color:var(--g1)">지원·면접 가이드</a>를 함께 읽어 보세요.</p>'
        '</div>'
        f'<div class="notice-box" style="margin-top:24px">{AGE_NOTICE}</div>'
        '</article>')

    body = (
        _hero("채용정보", "호빠·호스트바 선수 채용",
              "검수 정책에 따라 게재되는 호빠·호스트바 선수(남성 호스트) 채용정보입니다. 호빠알바 구인구직, 지원 전 알아둘 점을 정리했습니다.",
              '<a class="btn btn-gold" href="/advertising/contact/">매장 광고 문의</a>'
              '<a class="btn btn-ghost" href="/magazine/interview-guide/">지원·면접 가이드</a>',
              byline=_byline()) +
        banner_section + content +
        _faq_section(JOBS_FAQ) +
        f'<section class="wrap" style="padding-top:0">{_author_box()}</section>'
    )
    ld = [webpage_ld("/jobs/", "호빠·호스트바 선수 채용", "호빠·호스트바 선수 채용정보와 지원 가이드",
                     modified=LAST_UPDATED),
          breadcrumb([("홈", "/"), ("채용정보", "/jobs/")]),
          {"@type": "CollectionPage", "name": "채용정보", "url": C["url"] + "/jobs/"},
          faq_ld(JOBS_FAQ)]
    return "/jobs/index.html", page(
        "호빠·호스트바 선수 채용 — 호빠알바 구인구직 | 호빠클럽",
        "호빠·호스트바 선수(남성 호스트) 채용정보. 공고 읽는 법, 수입 구조, 안전하게 지원하는 법을 안내하는 호빠알바 구인구직. 만 19세 이상 대상.",
        "/jobs/", body, jsonld=ld, modified=LAST_UPDATED)


# 섹션별 내부 링크 강화(롱테일 H2 + 맥락 링크). 현재 글은 제외해 중복 회피.
_LONGTAIL = {
    "/magazine/": ("호빠알바, 안전하게 시작하려면 무엇부터 확인해야 할까", [
        ("안전센터 — 위험 신호 거르기", "/safety/"),
        ("지원·면접 가이드", "/magazine/interview-guide/"),
        ("근무조건·정산 정보 제대로 읽기", "/magazine/work-conditions/"),
        ("안전한 구직 — 사기 거르는 기준", "/magazine/safe-job-search/"),
        ("채용정보 보기", "/jobs/")]),
    "/safety/": ("불법 요구·허위공고를 만났을 때 어디에 알리고 어떻게 대처할까", [
        ("불법 요구 대처 절차", "/safety/illegal-demands/"),
        ("허위공고 신고 방법", "/safety/report-fake/"),
        ("안전한 면접 체크리스트", "/safety/interview-safety/"),
        ("안전한 구직 가이드(매거진)", "/magazine/safe-job-search/"),
        ("문의·신고하기", "/support/contact/")]),
}


def _author_box():
    return (f'<div class="card" style="margin-top:28px"><span class="kicker">작성·검수</span>'
            f'<h3 style="margin:8px 0">{EDITORIAL["byline"]}</h3>'
            f'<p style="font-size:13.5px">{EDITORIAL["who"]}</p>'
            f'<div style="margin-top:14px;display:flex;gap:10px;flex-wrap:wrap">'
            f'<a class="btn btn-ghost" href="/about/">편집 원칙 보기</a>'
            f'<a class="btn btn-ghost" href="/support/contact/">정정·제보 요청</a></div></div>')


def _internal_links(base, slug):
    h2, links = _LONGTAIL[base]
    ls = "".join(f'<li style="margin-bottom:8px"><a href="{h}" style="color:var(--g1)">{n}</a></li>'
                 for n, h in links if h.rstrip("/") != (base + slug).rstrip("/"))
    return (f'<section style="margin-top:40px"><h2 style="font-size:20px">{h2}</h2>'
            f'<ul style="margin-top:12px;padding-left:18px">{ls}</ul></section>')


def _article_pages(store, base, label, ld_breadcrumb_label):
    out = []
    items = list(store.items())
    is_safety = base == "/safety/"
    for i, (slug, a) in enumerate(items):
        toc = "".join(f'<li><a href="#s{j}">{t}</a></li>' for j, t in enumerate(a["toc"]))
        secs = ""
        for j, (h, paras) in enumerate(a["body"]):
            ps = "".join(f"<p>{p}</p>" for p in paras)
            secs += f'<section id="s{j}"><h2>{h}</h2>{ps}</section>'
        others = [(s, aa) for s, aa in items if s != slug]
        if others:
            r = i % len(others)
            others = others[r:] + others[:r]
        rel = "".join(
            f'<a class="rel-item" href="{base}{s}/"><span class="tag">{aa["tag"]}</span>'
            f'<span class="rt">{aa["title"]}</span><span class="ra">→</span></a>'
            for s, aa in others[:5])

        # YMYL 안전 글: 글별 맞춤 공식 출처 인용 블록(중복 회피)
        cite_block = ""
        srcs = SAFETY_SOURCES.get(slug, TRUST_SOURCES) if is_safety else []
        if is_safety:
            cards = "".join(
                f'<a class="card" href="{u}" target="_blank" rel="nofollow noopener" style="display:block">'
                f'<h3 style="font-size:16px">{n}</h3><p style="font-size:13px;margin-top:6px">{d}</p></a>'
                for n, d, u in srcs)
            cite_block = (f'<section style="margin-top:40px"><h2 style="font-size:20px">공식 상담·신고 창구</h2>'
                          f'<p style="margin:8px 0 16px">이 글의 안전 안내는 아래 공식 기관 정보를 참고했습니다.</p>'
                          f'<div class="grid g2">{cards}</div></section>')

        body = (
            f'<article class="wrap article" style="max-width:780px">'
            f'<a href="{base}" style="color:var(--g1);font-size:13px;font-weight:600">← {label}</a>'
            f'<span class="tag" style="margin:20px 0 16px;display:inline-block">{a["tag"]} · 읽기 {a["read"]}</span>'
            f'<h1 style="font-size:clamp(28px,4vw,42px)">{a["title"]}</h1>'
            f'<p class="lead" style="margin:18px 0 10px">{a["desc"]}</p>'
            f'<p style="font-size:13px;color:var(--dim);margin-bottom:30px">'
            f'작성·검수 <a href="/about/" style="color:var(--g1)">{EDITORIAL["byline"]}</a>'
            f' · 발행 {a["date"]} · 최종 업데이트 {LAST_UPDATED}</p>'
            f'<div class="toc-card" style="margin-bottom:36px"><strong>목차</strong><ul>{toc}</ul></div>'
            f'<div class="prose">{secs}</div>'
            f'<div class="notice-box" style="margin-top:24px">{AGE_NOTICE}</div>'
            f'{cite_block}'
            f'{_internal_links(base, slug)}'
            f'{_author_box()}'
            f'<section style="margin-top:46px"><h2 style="font-size:20px;margin-bottom:18px">함께 보기</h2>'
            f'<div class="rel-list">{rel}</div></section></article>'
        )
        art = {"@type": "Article", "headline": a["title"], "description": a["desc"],
               "author": {"@type": "Organization", "@id": C["url"] + "/#org", "name": EDITORIAL["byline"]},
               "publisher": {"@id": C["url"] + "/#org"},
               "reviewedBy": {"@type": "Organization", "@id": C["url"] + "/#org", "name": EDITORIAL["byline"]},
               "image": {"@id": C["url"] + "/#primaryimage"},
               "articleSection": a["tag"],
               "datePublished": a["date"], "dateModified": LAST_UPDATED,
               "inLanguage": "ko-KR",
               "mainEntityOfPage": C["url"] + f"{base}{slug}/"}
        if is_safety:
            art["citation"] = [{"@type": "CreativeWork", "name": n, "url": u}
                               for n, _, u in srcs]
        ld = [breadcrumb([("홈", "/"), (ld_breadcrumb_label, base), (a["title"], f"{base}{slug}/")]), art]
        out.append((f"{base}{slug}/index.html", page(
            f'{a["title"]} | {C["name"]} {label}', a["desc"], f"{base}{slug}/",
            body, og_type="article", jsonld=ld, modified=LAST_UPDATED)))
    return out


def magazine_hub():
    cards = "".join(
        f'<a class="card" href="/magazine/{s}/" style="display:block"><span class="tag">{a["tag"]}</span>'
        f'<h3 style="margin:12px 0 8px">{a["title"]}</h3><p style="font-size:13.5px">{a["desc"]}</p></a>'
        for s, a in MAGAZINE.items())
    body = (_hero("매거진", "호빠·호스트바 선수, 제대로 알고 시작하기",
                  "입문부터 면접·수입·후기까지. 호빠알바(호스트바) 선수에게 필요한 실용 정보를 정리한 호빠클럽 매거진입니다.") +
            f'<section class="wrap" style="padding-top:0"><div class="grid g2">{cards}</div></section>')
    ld = [breadcrumb([("홈", "/"), ("매거진", "/magazine/")])]
    return "/magazine/index.html", page(
        "호빠클럽 매거진 — 호빠·호스트바 선수 가이드 (호빠알바)",
        "선수 입문 가이드, 지원·면접, 수입·정산 정보, 후기·인터뷰까지. 호빠·호스트바(호빠알바) 구직에 필요한 정보를 담은 호빠클럽 매거진.",
        "/magazine/", body, jsonld=ld)


def safety_hub():
    cards = "".join(
        f'<a class="card" href="/safety/{s}/" style="display:block"><span class="tag">{a["tag"]}</span>'
        f'<h3 style="margin:12px 0 8px">{a["title"]}</h3><p style="font-size:13.5px">{a["desc"]}</p></a>'
        for s, a in SAFETY.items())
    hot = ('<div class="notice-box" style="margin-bottom:24px"><strong style="color:var(--g1)">긴급 도움</strong><br>'
           '신변 위협 112 · 여성긴급전화 1366 · 노동 문제 1350 · 개인정보침해 118')
    body = (_hero("안전센터", "안전하게 일할 권리를 지키세요",
                  "허위공고 신고부터 불법 요구 대처까지, 구직 과정에서 자신을 보호하는 방법을 안내합니다.") +
            f'<section class="wrap" style="padding-top:0">{hot}</div><div class="grid g2">{cards}</div></section>')
    ld = [breadcrumb([("홈", "/"), ("안전센터", "/safety/")])]
    return "/safety/index.html", page(
        "안전센터 — 허위공고 신고·불법 요구 대처 | 호빠클럽",
        "허위공고 신고, 개인정보 보호, 안전한 면접 체크, 불법 요구 대처 등 구직자 보호 정보를 제공하는 호빠클럽 안전센터.",
        "/safety/", body, jsonld=ld)


def support_hub():
    links = [("공지사항", "/support/notice/", "서비스 운영·안전 관련 공지"),
             ("자주 묻는 질문", "/support/faq/", "이용·신고·광고에 대한 답변"),
             ("문의하기", "/support/contact/", "허위공고 신고·일반 문의"),
             ("이용약관", "/policy/terms/", "서비스 이용 조건"),
             ("개인정보처리방침", "/policy/privacy/", "개인정보 수집·이용 안내"),
             ("청소년 보호정책", "/policy/youth/", "청소년 보호 조치")]
    cards = "".join(
        f'<a class="card" href="{h}" style="display:block"><h3>{n}</h3>'
        f'<p style="font-size:13.5px;margin-top:8px">{d}</p></a>' for n, h, d in links)
    body = (_hero("고객센터", "무엇을 도와드릴까요",
                  f'고객센터 {C["tel"]} ({C["tel_hours"]}) · {C["email"]}') +
            f'<section class="wrap" style="padding-top:0"><div class="grid g3">{cards}</div></section>')
    ld = [breadcrumb([("홈", "/"), ("고객센터", "/support/")])]
    return "/support/index.html", page(
        "고객센터 — 공지·FAQ·문의 | 호빠클럽",
        "호빠클럽 고객센터. 공지사항, 자주 묻는 질문, 문의하기와 이용약관·개인정보처리방침·청소년 보호정책을 안내합니다.",
        "/support/", body, jsonld=ld)


def notice_page():
    items = "".join(
        f'<div class="note-card"><div class="note-num">{i+1:02d}</div><div>'
        f'<span class="tag">{n["level"]}</span> <span style="color:var(--dim);font-size:12.5px">{n["date"]}</span>'
        f'<h3 style="margin:8px 0">{n["title"]}</h3>'
        + "".join(f'<p style="margin-bottom:8px">{p}</p>' for p in n["body"]) + '</div></div>'
        for i, n in enumerate(NOTICES))
    body = _hero("공지사항", "공지사항", "호빠클럽 운영·안전 관련 안내를 확인하세요.") + \
        f'<section class="wrap" style="padding-top:0">{items}</section>'
    ld = [breadcrumb([("홈", "/"), ("고객센터", "/support/"), ("공지사항", "/support/notice/")])]
    return "/support/notice/index.html", page(
        "공지사항 | 호빠클럽 고객센터",
        "호빠클럽 운영 정책, 사기 주의, 개인정보처리방침 개정 등 주요 공지사항을 안내합니다.",
        "/support/notice/", body, jsonld=ld)


def faq_page():
    body = _hero("자주 묻는 질문", "자주 묻는 질문", "이용·신고·광고에 대해 자주 묻는 질문을 모았습니다.") + \
        _faq_section(SUPPORT_FAQ, title="전체 FAQ")
    ld = [breadcrumb([("홈", "/"), ("고객센터", "/support/"), ("자주 묻는 질문", "/support/faq/")]),
          faq_ld(SUPPORT_FAQ)]
    return "/support/faq/index.html", page(
        "자주 묻는 질문(FAQ) | 호빠클럽",
        "호빠클럽 이용 방법, 허위공고 신고, 선불금 사기 대처, 연령 기준, 광고 문의 등 자주 묻는 질문에 답합니다.",
        "/support/faq/", body, jsonld=ld)


def support_contact():
    fhtml = (
        '<div class="field"><label>이름 또는 닉네임<span class="req">*</span></label><input name="name" required></div>'
        '<div class="field"><label>연락처 또는 이메일<span class="req">*</span></label><input name="contact" required></div>'
        '<div class="field"><label>문의 유형<span class="req">*</span></label>'
        '<select name="type" required>'
        '<option>VVIP 광고문의</option><option>VIP 광고문의</option><option>Special 광고문의</option>'
        '<option>불법 요구 제보</option><option>일반 문의</option></select></div>'
        '<div class="field"><label>내용<span class="req">*</span></label>'
        '<textarea name="message" rows="6" required placeholder="광고문의 시 매장명·희망 위치·기간을, 제보 시 근거를 함께 적어 주세요."></textarea></div>'
        '<div class="field"><label><input type="checkbox" required style="width:auto;margin-right:8px">'
        '개인정보 수집·이용에 동의합니다.</label></div>'
        '<input class="hp" name="website" tabindex="-1" autocomplete="off">'
        '<button class="btn btn-gold" type="submit">문의 보내기</button>')
    body = (_hero("문의하기", "문의하기", "광고문의(VVIP·VIP·Special)나 제보·일반 문의를 남겨 주세요. 접수된 내용은 내부 검토 후 순차적으로 답변드립니다.") +
            f'<section class="wrap" style="padding-top:0;max-width:720px">'
            f'<form class="card" method="post" action="/api/contact-ads">{fhtml}</form>'
            f'<div class="notice-box" style="margin-top:20px">긴급 상황은 112, 여성긴급전화 1366으로 즉시 도움을 받으세요. {AGE_NOTICE}</div></section>')
    ld = [breadcrumb([("홈", "/"), ("고객센터", "/support/"), ("문의하기", "/support/contact/")])]
    return "/support/contact/index.html", page(
        "문의하기 — 광고문의·제보·일반 문의 | 호빠클럽",
        "호빠클럽 문의하기. VVIP·VIP·Special 광고문의와 불법 요구 제보, 일반 문의를 접수합니다. 내부 검토 후 순차 답변드립니다.",
        "/support/contact/", body, jsonld=ld)


def policy_pages():
    out = []
    for slug, p in POLICIES.items():
        secs = "".join(f'<section style="margin-bottom:26px"><h2 style="font-size:20px">{h}</h2>'
                       f'<p style="margin-top:8px">{t}</p></section>' for h, t in p["sections"])
        body = (_hero(p["title"], p["title"], p["desc"]) +
                f'<section class="wrap" style="padding-top:0;max-width:820px">{secs}</section>')
        ld = [breadcrumb([("홈", "/"), ("고객센터", "/support/"), (p["title"], f"/policy/{slug}/")])]
        out.append((f"/policy/{slug}/index.html", page(
            f'{p["title"]} | {C["name"]}', p["desc"], f"/policy/{slug}/", body, jsonld=ld)))
    return out


def about_page():
    whw = "".join(f'<section style="margin-bottom:28px"><h2 style="font-size:22px">{t}</h2>'
                  f'<p style="margin-top:8px">{d}</p></section>'
                  for t, d in [("누가 만드나요 (Who)", EDITORIAL["who"]),
                               ("어떻게 만드나요 (How)", EDITORIAL["how"]),
                               ("왜 만드나요 (Why)", EDITORIAL["why"])])
    policy = "".join(_note(i + 1, t, [d]) for i, (t, d) in enumerate(EDITORIAL["policy"]))
    contact = (f'<div class="card"><h3>운영·연락처</h3>'
               f'<p style="margin-top:10px;font-size:14px">{C["name"]} · 대표 {C["ceo"]}<br>'
               f'고객센터 {C["tel"]} ({C["tel_hours"]})<br>이메일 {C["email"]}<br>'
               f'개인정보책임자 {C["privacy_officer"]}</p>'
               f'<div style="margin-top:14px"><a class="btn btn-ghost" href="/support/contact/">문의하기</a></div></div>')
    body = (
        _hero("운영 정보", "운영 정보·편집 원칙",
              f'호빠클럽 콘텐츠를 누가, 어떻게, 왜 만드는지 투명하게 공개합니다.') +
        f'<section class="wrap" style="padding-top:0;max-width:840px">{_byline()}{whw}</section>'
        f'<section class="wrap" style="padding-top:0"><h2>편집 원칙</h2>{policy}</section>'
        f'<section class="wrap" style="padding-top:0;max-width:840px">{contact}'
        f'<div class="notice-box" style="margin-top:20px">{AGE_NOTICE}</div></section>'
    )
    ld = [webpage_ld("/about/", "운영 정보·편집 원칙", "호빠클럽 운영 주체와 편집 원칙 안내",
                     modified=LAST_UPDATED),
          breadcrumb([("홈", "/"), ("운영 정보", "/about/")]),
          {"@type": "AboutPage", "name": "운영 정보·편집 원칙", "url": C["url"] + "/about/",
           "publisher": {"@id": C["url"] + "/#org"}}]
    return "/about/index.html", page(
        "운영 정보·편집 원칙 — 누가·어떻게·왜 | 호빠클럽",
        "호빠클럽 운영·편집팀, 콘텐츠 검수 방식, 편집 독립성·정정 정책과 연락처를 안내합니다. 누가·어떻게·왜 만드는지 투명하게 공개합니다.",
        "/about/", body, jsonld=ld, modified=LAST_UPDATED)


def advertising():
    def price_rows(p):
        return "".join(
            f'<div style="display:flex;justify-content:space-between;gap:12px;'
            f'border-top:1px solid var(--line);padding:8px 0">'
            f'<span style="color:var(--dim);font-size:13px">{per}</span>'
            f'<span style="color:var(--g1);font-weight:800;font-size:15px">{amt}</span></div>'
            for per, amt in p["prices"])

    prod_cards = "".join(
        f'<div class="card card-h">'
        f'<span class="tag">{p["tier"]}</span>'
        f'<h3 style="margin:12px 0 4px">{p["slot"]}</h3>'
        f'<div style="margin:12px 0 16px">{price_rows(p)}</div>'
        f'<ul style="padding-left:18px;color:var(--muted);font-size:13px;line-height:1.6">'
        + "".join(f'<li style="margin-bottom:5px">{ft}</li>' for ft in p["features"])
        + '</ul></div>'
        for p in AD_PRODUCTS)

    def sec(id_, title, inner):
        return f'<section id="{id_}" class="wrap" style="padding-top:0"><h2>{title}</h2>{inner}</section>'

    body = (
        _hero("광고안내", "신뢰받는 매장을 위한 광고안내",
              "호빠클럽은 검수된 공고만 노출하는 채용정보 플랫폼입니다. 건전하게 운영되는 매장을 위한 광고 상품과 기준을 안내합니다.",
              '<a class="btn btn-gold" href="/advertising/contact/">광고문의 하기</a>') +
        sec("products", "광고 상품 안내",
            f'<div class="grid g3">{prod_cards}</div>'
            f'<p style="margin-top:16px;font-size:13px;color:var(--dim)">표시 금액은 부가세 별도입니다. '
            f'선착순 예약 상품은 고객센터로 별도 문의해 주세요. · 문의 전화 {AD_INQUIRY_TEL}</p>') +
        sec("placement", "노출 위치 안내",
            '<p>VVIP는 메인 최상단에 박스 형태로 고정 노출되며 VIP·일반 줄광고 서비스가 함께 포함됩니다. '
            'VIP·Special 광고는 VIP 광고와 일반 광고 사이에 줄광고 형태로 랜덤 노출되고, 모바일 급구정보 카테고리에 단독 노출됩니다. '
            '같은 등급 내에서는 선등록 순으로 배치됩니다.</p>') +
        sec("process", "광고 등록 절차",
            "".join(_note(i + 1, t, [d]) for i, (t, d) in enumerate([
                ("광고문의 접수", "광고문의 페이지에서 매장 정보와 희망 위치·기간을 남깁니다."),
                ("내부 검토·심사", "검수 기준에 따라 공고 내용과 표현을 확인합니다."),
                ("게재·노출", "심사를 통과한 광고를 선택한 위치에 게재합니다."),
                ("운영·관리", "수정·연장·중단 요청을 처리하고 노출 현황을 관리합니다.")]))) +
        sec("standard", "등록 기준 · 등록 제한 업종 및 표현",
            f'<div class="notice-box">{AGE_NOTICE}</div>'
            '<p style="margin-top:14px">다음에 해당하는 광고는 등록이 제한됩니다 — 허위·과장 공고, 성매매를 암시하는 표현, '
            '불법 행위 알선, 과장된 급여 문구, 미성년자 대상 채용, 선불금·보증금을 전제로 한 모집.</p>') +
        sec("review", "광고 심사 기준",
            '<p>모든 광고는 게재 전 내부 심사를 거칩니다. 업무 설명의 구체성, 급여 표현의 적정성, 법령·정책 위반 여부를 확인하며, '
            '기준에 맞지 않으면 보완을 요청하거나 게재를 제한합니다.</p>') +
        sec("price", "광고비 안내",
            '<div class="grid g3">' +
            "".join(
                f'<div class="card"><span class="tag">{p["tier"]}</span>'
                + "".join(f'<div style="display:flex;justify-content:space-between;gap:12px;'
                          f'border-top:1px solid var(--line);padding:9px 0;font-size:14px">'
                          f'<span style="color:var(--muted)">{per}</span>'
                          f'<span style="color:var(--g1);font-weight:800">{amt}</span></div>'
                          for per, amt in p["prices"])
                + '</div>' for p in AD_PRODUCTS) + '</div>'
            f'<p style="margin-top:14px;font-size:13px;color:var(--dim)">표시 금액은 부가세 별도이며, 프로모션에 따라 변동될 수 있습니다. · 문의 전화 {AD_INQUIRY_TEL}</p>') +
        sec("refund", "환불 및 수정 정책",
            '<p>게재 전 취소 시 전액 환불됩니다. 게재 후에는 잔여 기간을 기준으로 환불 금액이 산정되며, '
            '광고 소재 수정은 운영 시간 내 요청 시 처리됩니다. 정책 위반으로 게재가 중단된 경우 환불이 제한될 수 있습니다.</p>') +
        _faq_section(AD_FAQ, title="광고 자주 묻는 질문") +
        '<section class="wrap" style="padding-top:0;text-align:center">'
        '<a class="btn btn-gold" href="/advertising/contact/" style="font-size:15px;padding:15px 30px">광고문의 하기 →</a></section>'
    )
    ld = [breadcrumb([("홈", "/"), ("광고안내", "/advertising/")]),
          {"@type": "Service", "name": "호빠클럽 채용광고", "provider": {"@id": C["url"] + "/#org"},
           "areaServed": "KR", "description": "검수 기준에 따른 채용광고 게재 서비스",
           "offers": [{"@type": "Offer", "name": p["tier"],
                       "price": p["prices"][0][1].replace(",", "").replace("원", ""),
                       "priceCurrency": "KRW"} for p in AD_PRODUCTS]},
          faq_ld(AD_FAQ)]
    return "/advertising/index.html", page(
        "광고안내 — 채용광고 상품·노출 위치·심사 기준 | 호빠클럽",
        "호빠클럽 채용광고 안내. 광고 상품과 노출 위치, 등록 절차, 심사 기준, 광고비, 환불·수정 정책을 한 곳에서 확인하세요.",
        "/advertising/", body, jsonld=ld)


def advertising_contact():
    fhtml = (
        '<div class="field"><label>상호명<span class="req">*</span></label><input name="company" required></div>'
        '<div class="field"><label>담당자명<span class="req">*</span></label><input name="manager" required></div>'
        '<div class="field"><label>연락처<span class="req">*</span></label><input name="phone" required></div>'
        '<div class="field"><label>이메일<span class="req">*</span></label><input name="email" type="email" required></div>'
        '<div class="field"><label>광고 희망 상품<span class="req">*</span></label>'
        '<select name="placement" required><option>VVIP — 메인 최상단 고정</option><option>VIP</option>'
        '<option>Special</option><option>상담 후 결정</option></select></div>'
        '<div class="field"><label>광고 희망 기간<span class="req">*</span></label>'
        '<select name="period" required><option>1개월</option><option>2개월</option><option>3개월</option><option>6개월</option><option>상담 후 결정</option></select></div>'
        '<div class="field"><label>문의 내용<span class="req">*</span></label>'
        '<textarea name="message" rows="5" required placeholder="매장 소개와 문의 사항을 적어 주세요."></textarea></div>'
        '<div class="field"><label><input type="checkbox" required style="width:auto;margin-right:8px">'
        '개인정보 수집·이용에 동의합니다.</label></div>'
        '<input class="hp" name="website" tabindex="-1" autocomplete="off">'
        '<button class="btn btn-gold" type="submit">광고문의 보내기</button>')
    body = (_hero("광고문의", "광고문의",
                  "매장 정보와 희망 위치·기간을 남겨 주세요. 접수된 광고 문의는 내부 검토 후 순차적으로 답변드립니다.") +
            f'<section class="wrap" style="padding-top:0;max-width:720px">'
            f'<form class="card" method="post" action="/api/contact-ads">{fhtml}</form>'
            f'<div class="notice-box" style="margin-top:20px">접수된 광고 문의는 내부 검토 후 순차적으로 답변드립니다. '
            f'등록 기준에 맞지 않는 광고는 게재가 제한될 수 있습니다.<br><br>{AGE_NOTICE}</div>'
            f'<p style="margin-top:16px;text-align:center"><a href="/advertising/" style="color:var(--g1)">← 광고안내로 돌아가기</a></p></section>')
    ld = [breadcrumb([("홈", "/"), ("광고안내", "/advertising/"), ("광고문의", "/advertising/contact/")])]
    return "/advertising/contact/index.html", page(
        "광고문의 — 매장 채용광고 신청 | 호빠클럽",
        "호빠클럽 광고문의. 상호명·담당자·희망 위치·기간을 남기면 내부 검토 후 순차적으로 안내드립니다. 등록 기준 검수 후 게재.",
        "/advertising/contact/", body, jsonld=ld)


def promo_pages():
    """배너 클릭 시 보이는 샘플 홍보 상세 페이지 (noindex — 데모/기만 색인 방지)."""
    BEN = {
        "VVIP": ["메인 최상단 고정 노출로 높은 방문·문의", "신입 선수 환영 · 1:1 멘토링과 체계적 교육",
                 "보장급 + TC·인센티브 (면접 협의)", "단골 多 · 안정적인 매출 기반",
                 "자유 출근 · 개인 스케줄 조율 가능", "용모·자기관리 지원(의상·헤어 등)"],
        "VIP": ["검증된 운영 매장 · 안정적인 단골층", "초보 가능 · 적응 교육 지원",
                "TC·인센티브 + 보장급 협의", "유연한 근무 형태(정규·파트)",
                "동료와 함께하는 팀 분위기"],
        "프리미엄": ["성실 근무 환영 · 부담 없는 시작", "근무 조건 면접에서 투명하게 협의",
                  "자유로운 출근 · 본인 페이스 존중", "기본기부터 차근차근 교육"],
    }
    LOOKING = {
        "VVIP": ["밝고 적극적인 대화·소통이 가능한 분", "단정한 용모와 꾸준한 자기관리가 되는 분",
                 "성실한 근태로 단골을 만들 의지가 있는 분"],
        "VIP": ["처음이라도 배우려는 의지가 있는 분", "사람과의 대화를 즐기는 분", "야간 근무에 적응 가능한 분"],
        "프리미엄": ["성실하게 출근할 수 있는 분", "기본 매너와 밝은 태도를 갖춘 분", "만 19세 이상 성인"],
    }
    PAY = {"VVIP": "보장급 + TC·인센티브 (면접 협의)",
           "VIP": "TC·인센티브 + 보장급 협의", "프리미엄": "면접 시 협의"}
    promo_faq = [
        ("경험이 없어도 지원할 수 있나요?", "네, 신입 선수를 환영하며 매장 교육과 선배의 도움을 받아 시작할 수 있습니다. 다만 보장급·정산 조건은 면접에서 꼭 확인하세요."),
        ("수입은 어떻게 되나요?", "보장급에 TC·인센티브가 더해지는 구조이며, 정확한 금액은 면접에서 안내됩니다. 공고의 ‘예상 수입’은 최대치인 경우가 많으니 보장급 기준으로 판단하세요."),
        ("근무 시간과 출근은 어떻게 되나요?", "야간 근무가 중심이며 정규·파트 형태를 협의할 수 있습니다. 출근 일수와 시간은 면접 시 조율합니다."),
        ("안전하게 일할 수 있나요?", "본 매장 정보는 검수 정책에 따라 게재됩니다. 선불금·보증금 요구나 불법적인 요구가 있으면 응하지 말고 안전센터로 신고해 주세요."),
    ]
    steps = [("01", "전화상담", "궁금한 점을 전화로 편하게 문의합니다. (샘플 페이지에서는 연결되지 않습니다)"),
             ("02", "면접", "매장 방문 면접에서 업무·수입·근무 조건을 확인합니다."),
             ("03", "조건 확정", "보장급·정산·출근 조건을 서면으로 확정합니다."),
             ("04", "근무 시작", "교육을 받고 적응 기간을 거쳐 근무를 시작합니다.")]
    out = []
    for pid, tier, b in _promo_entries():
        name = b.get("title") or b.get("name")
        area = b["area"].replace("-", " ")
        copy = b["copy"]
        pay = (f'{b["unit"]} 기준 {b["price"]} (샘플)' if b.get("price") else PAY[tier])
        ben = "".join(f"<li style='margin-bottom:7px'>{x}</li>" for x in BEN[tier])
        look = "".join(f"<li style='margin-bottom:7px'>{x}</li>" for x in LOOKING[tier])
        info = [("광고 등급", tier), ("지역", area), ("모집", "선수(남성 호스트)"),
                ("근무 형태", "야간 (정규·파트 협의)"), ("수입 구조", pay),
                ("정산", "면접 시 안내"), ("지원 자격", "만 19세 이상")]
        rows = "".join(
            f'<div style="display:flex;justify-content:space-between;gap:12px;'
            f'border-top:1px solid var(--line);padding:11px 0">'
            f'<span style="color:var(--dim);font-size:13.5px">{k}</span>'
            f'<span style="font-weight:600;font-size:14px;text-align:right">{v}</span></div>' for k, v in info)
        step_html = "".join(_note(int(n), t, [d]) for n, t, d in steps)
        faq_html = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in promo_faq)
        # 다른 매장 추천 (최대 5)
        rel = "".join(
            f'<a class="rel-item" href="/promo/{rp}/"><span class="tag">{rt}</span>'
            f'<span class="rt">{rb.get("title") or rb.get("name")}</span><span class="ra">→</span></a>'
            for rp, rt, rb in [e for e in _promo_entries() if e[0] != pid][:5])
        body = (
            '<section class="wrap" style="max-width:860px">'
            '<a href="/jobs/" style="color:var(--g1);font-size:13px;font-weight:600">← 채용정보</a>'
            f'<div style="display:flex;gap:8px;align-items:center;margin:18px 0 10px">'
            f'<span class="tag">{tier} 광고</span>'
            f'<span class="tag" style="background:none;border-color:var(--line-2);color:var(--dim)">샘플</span></div>'
            f'<h1 style="font-size:clamp(28px,4.5vw,44px)">{name}</h1>'
            f'<p class="lead" style="margin:14px 0 10px">{area} · {copy}</p>'
            '<div style="margin:20px 0 8px;display:flex;gap:10px;flex-wrap:wrap">'
            '<button class="btn btn-gold" type="button">📞 전화상담</button>'
            '<a class="btn btn-ghost" href="#info">모집 정보 보기</a></div>'
            '<p style="font-size:12.5px;color:var(--dim)">※ 본 페이지는 광고 게재 형식을 보여주는 '
            '<strong style="color:var(--muted)">샘플</strong>입니다. 실제 연락처·상세 조건은 매장의 광고 등록 후 노출됩니다.</p>'
            # 본문 2열
            '<div class="grid g2" style="margin-top:30px;align-items:start">'
            f'<div><h2 style="font-size:21px;margin-bottom:12px">매장 소개</h2>'
            f'<p style="color:var(--muted);line-height:1.9;margin-bottom:14px">{name}은(는) {area} 권역에서 운영되는 호스트바로, '
            f'함께할 선수(남성 호스트)를 모집합니다. 손님을 맞이하고 대화와 분위기 메이킹으로 즐거운 시간을 만드는 것이 주 업무이며, '
            f'경험이 없어도 매장 교육과 선배의 도움을 받아 시작할 수 있습니다.</p>'
            f'<p style="color:var(--muted);line-height:1.9">“{copy}” — 지원 전 근무 조건과 수입 구조를 면접에서 충분히 확인하시고, '
            f'본인에게 맞는 환경인지 살펴보세요.</p>'
            f'<h2 style="font-size:21px;margin:28px 0 12px">이런 분을 찾습니다</h2>'
            f'<ul style="padding-left:18px;color:var(--muted)">{look}</ul>'
            f'<h2 style="font-size:21px;margin:28px 0 12px">근무 환경·혜택</h2>'
            f'<ul style="padding-left:18px;color:var(--muted)">{ben}</ul>'
            f'<h2 style="font-size:21px;margin:28px 0 12px">위치·상권</h2>'
            f'<p style="color:var(--muted);line-height:1.9">{area} 권역에 위치해 접근성이 좋은 편입니다. '
            f'정확한 위치와 교통편은 면접 시 안내되며, 야간 근무 특성상 출퇴근 동선도 함께 확인하시길 권합니다.</p></div>'
            # 우측 정보 카드(sticky 느낌)
            f'<div class="card" id="info"><h3 style="font-size:15px;margin-bottom:4px">모집 정보</h3>{rows}'
            f'<div style="margin-top:16px"><button class="btn btn-gold" type="button" style="width:100%;justify-content:center">📞 전화상담</button></div>'
            f'<p style="font-size:11.5px;color:var(--dim);margin-top:10px;text-align:center">샘플 페이지 — 연결되지 않습니다</p></div>'
            '</div>'
            # 지원 절차
            f'<section style="margin-top:40px"><h2 style="font-size:21px;margin-bottom:18px">지원·상담 절차</h2>{step_html}</section>'
            # FAQ
            f'<section style="margin-top:36px"><h2 style="font-size:21px;margin-bottom:14px">자주 묻는 질문</h2>{faq_html}</section>'
            # 안전 고지
            f'<div class="notice-box" style="margin-top:24px">{AGE_NOTICE} 선불금·보증금 요구나 불법적인 요구가 있으면 응하지 말고 '
            '<a href="/safety/" style="color:var(--g1)">안전센터</a>를 통해 신고하세요. 본 매장 정보는 검수 정책에 따라 게재됩니다.</div>'
            # 다른 매장
            f'<section style="margin-top:40px"><h2 style="font-size:20px;margin-bottom:16px">다른 매장 광고</h2>'
            f'<div class="rel-list">{rel}</div></section>'
            '</section>')
        ld = [breadcrumb([("홈", "/"), ("채용정보", "/jobs/"), (f"{name} (샘플)", f"/promo/{pid}/")])]
        out.append((f"/promo/{pid}/index.html", page(
            f'[{tier}] {name} — {area} 호스트바 선수 모집 (샘플) | 호빠클럽',
            f'{name}({area}) 호스트바 선수 채용 샘플 광고. {copy} 광고 게재 형식을 보여주는 호빠클럽 샘플 페이지입니다.',
            f"/promo/{pid}/", body, jsonld=ld, noindex=True)))
    return out


def not_found():
    body = (
        '<section class="wrap" style="text-align:center;min-height:48vh">'
        '<div class="serif" style="font-size:96px;color:var(--g2);line-height:1">404</div>'
        '<h1 style="margin:8px 0 16px">페이지를 찾을 수 없습니다</h1>'
        '<p class="note-text" style="margin:0 auto 26px">요청하신 페이지가 이동되었거나 존재하지 않습니다. 아래에서 원하시는 메뉴로 이동해 주세요.</p>'
        '<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">'
        '<a class="btn btn-gold" href="/">홈으로</a>'
        '<a class="btn btn-ghost" href="/jobs/">채용정보</a>'
        '<a class="btn btn-ghost" href="/safety/">안전센터</a>'
        '<a class="btn btn-ghost" href="/support/contact/">문의하기</a></div></section>')
    return "/404.html", page(
        "페이지를 찾을 수 없습니다 (404) | 호빠클럽",
        "요청하신 페이지를 찾을 수 없습니다. 호빠클럽 홈·채용정보·안전센터로 이동해 주세요.",
        "/404.html", body)


def all_pages():
    pages = [home(), jobs(), magazine_hub(), safety_hub(), support_hub(),
             notice_page(), faq_page(), support_contact(), about_page(),
             advertising(), advertising_contact(), not_found()]
    pages += policy_pages()
    pages += promo_pages()
    pages += _article_pages(MAGAZINE, "/magazine/", "매거진", "매거진")
    pages += _article_pages(SAFETY, "/safety/", "안전센터", "안전센터")
    return pages
