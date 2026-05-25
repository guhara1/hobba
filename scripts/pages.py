# -*- coding: utf-8 -*-
"""페이지 빌더: 각 함수는 (path, html)를 반환."""
from data import (COMPANY, JOBS, AD_PRODUCTS, AD_FAQ, AGE_NOTICE,
                  EDITORIAL, TRUST_SOURCES, LAST_UPDATED)
from content import MAGAZINE, SAFETY, NOTICES, SUPPORT_FAQ, POLICIES
from templates import page, breadcrumb, faq_ld, webpage_ld

C = COMPANY


def _note(num, title, paras):
    ps = "".join(f"<p>{p}</p>" for p in paras)
    return (f'<div class="note-card"><div class="note-num">{num:02d}</div>'
            f'<div><h3 class="note-title">{title}</h3><div class="note-text">{ps}</div></div></div>')


def _hero(kicker, h1, sub, ctas=""):
    return (f'<section class="wrap" style="padding-bottom:32px"><span class="kicker">{kicker}</span>'
            f'<h1 style="margin:16px 0 18px">{h1}</h1>'
            f'<p class="note-text" style="font-size:17px">{sub}</p>'
            f'<div style="margin-top:26px;display:flex;gap:12px;flex-wrap:wrap">{ctas}</div></section>')


def _faq_section(pairs, title="자주 묻는 질문"):
    items = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in pairs)
    return f'<section class="wrap" style="padding-top:0"><h2>{title}</h2>{items}</section>'


# ─────────────────────────────────────────────────────────────
def _byline():
    return (f'<p style="margin-top:18px;font-size:13px;color:var(--dim)">'
            f'작성·검수 <a href="/about/" style="color:var(--g1)">{EDITORIAL["byline"]}</a>'
            f' · 최종 업데이트 {LAST_UPDATED}</p>')


def home():
    job_cards = "".join(
        f'<a class="card" href="/jobs/" style="display:block"><span class="tag">{j["tag"]}</span>'
        f'<h3 style="margin:12px 0 8px">{j["title"]}</h3>'
        f'<p style="font-size:13.5px">{j["area"]} · {j["type"]} · {j["pay"]}</p></a>'
        for j in JOBS[:6])
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
              '안전하게 시작하는 <span class="gradtext">호빠알바 채용정보</span>',
              "호빠클럽은 만 19세 이상 성인 구직자를 위한 채용정보 플랫폼입니다. 운영·편집팀이 직접 검수한 공고와 안전 가이드로 더 안심하고 일자리를 찾으세요.",
              '<a class="btn btn-gold" href="/jobs/">채용정보 보기</a>'
              '<a class="btn btn-ghost" href="/safety/">안전센터 둘러보기</a>') +
        f'<section class="wrap" style="padding-top:0;margin-top:-32px">{_byline()}</section>'
        f'<section class="wrap" style="padding-top:0"><h2>최근 채용정보</h2>'
        f'<div class="grid g3">{job_cards}</div></section>'
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
    ld = [webpage_ld("/", f'{C["name"]} | 만 19세 이상 호빠알바 채용정보 플랫폼',
                     '만 19세 이상 성인 구직자를 위한 호빠알바 채용정보 플랫폼.',
                     published="2026-01-01", modified=LAST_UPDATED),
          {"@type": "CollectionPage", "name": C["name"], "url": C["url"] + "/"},
          faq_ld(SUPPORT_FAQ[:5])]
    return "/index.html", page(
        f'{C["name"]} | 만 19세 이상 호빠알바 채용정보 플랫폼',
        '만 19세 이상 성인 구직자를 위한 호빠알바 채용정보. 운영·편집팀이 직접 검수한 공고와 안전 가이드, 투명한 근무조건 정보를 제공하는 호빠클럽.',
        "/", body, jsonld=ld, verification=True, modified=LAST_UPDATED)


def jobs():
    cards = "".join(
        f'<div class="card"><span class="tag">{j["tag"]}</span>'
        f'<h3 style="margin:12px 0 8px">{j["title"]}</h3>'
        f'<p style="font-size:13.5px">{j["area"]} · {j["type"]} · {j["pay"]}</p>'
        f'<div style="margin-top:14px"><a class="btn btn-ghost" href="/advertising/contact/">매장 광고 문의</a></div></div>'
        for j in JOBS)
    body = (
        _hero("채용정보", "지역·형태별 호빠알바 채용정보",
              "검수 정책에 따라 게재된 채용정보입니다. 지원 전 ‘지원·면접 가이드’와 ‘안전한 면접 체크’를 함께 확인하세요.",
              '<a class="btn btn-gold" href="/magazine/interview-guide/">지원·면접 가이드</a>') +
        f'<section class="wrap" style="padding-top:0"><div class="grid g2">{cards}</div></section>'
        f'<section class="wrap" style="padding-top:0"><div class="notice-box">{AGE_NOTICE}</div></section>'
    )
    ld = [breadcrumb([("홈", "/"), ("채용정보", "/jobs/")]),
          {"@type": "CollectionPage", "name": "채용정보", "url": C["url"] + "/jobs/"}]
    return "/jobs/index.html", page(
        "호빠알바 채용정보 — 지역·형태별 모집 공고 | 호빠클럽",
        "전국 호빠알바 채용정보. 지역·근무형태별 모집 공고를 검수 정책에 따라 제공합니다. 만 19세 이상 성인 구직자 대상.",
        "/jobs/", body, jsonld=ld)


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
            ps = "".join(f"<p style='margin-bottom:12px'>{p}</p>" for p in paras)
            secs += f'<section id="s{j}" style="margin-bottom:34px"><h2 style="font-size:24px">{h}</h2>{ps}</section>'
        rel = "".join(f'<a class="card" href="{base}{s}/" style="display:block">'
                      f'<span class="tag">{aa["tag"]}</span><h3 style="margin-top:10px">{aa["title"]}</h3></a>'
                      for s, aa in items if s != slug)

        # YMYL 안전 글: 공식 출처 인용 블록
        cite_block = ""
        if is_safety:
            cards = "".join(
                f'<a class="card" href="{u}" target="_blank" rel="nofollow noopener" style="display:block">'
                f'<h3 style="font-size:16px">{n}</h3><p style="font-size:13px;margin-top:6px">{d}</p></a>'
                for n, d, u in TRUST_SOURCES)
            cite_block = (f'<section style="margin-top:40px"><h2 style="font-size:20px">공식 상담·신고 창구</h2>'
                          f'<p style="margin:8px 0 16px">이 글의 안전 안내는 아래 공식 기관 정보를 참고했습니다.</p>'
                          f'<div class="grid g2">{cards}</div></section>')

        body = (
            f'<article class="wrap"><a href="{base}" style="color:var(--g1);font-size:13px">← {label}</a>'
            f'<span class="tag" style="margin:18px 0 14px;display:inline-block">{a["tag"]} · 읽기 {a["read"]}</span>'
            f'<h1>{a["title"]}</h1>'
            f'<p style="margin:16px 0 8px">{a["desc"]}</p>'
            f'<p style="font-size:13px;color:var(--dim);margin-bottom:26px">'
            f'작성·검수 <a href="/about/" style="color:var(--g1)">{EDITORIAL["byline"]}</a>'
            f' · 발행 {a["date"]} · 최종 업데이트 {LAST_UPDATED}</p>'
            f'<div class="card" style="margin-bottom:32px"><strong>목차</strong>'
            f'<ul style="margin-top:10px;padding-left:18px;color:var(--muted)">{toc}</ul></div>'
            f'{secs}'
            f'<div class="notice-box" style="margin-top:20px">{AGE_NOTICE}</div>'
            f'{cite_block}'
            f'{_internal_links(base, slug)}'
            f'{_author_box()}'
            f'<section style="margin-top:44px"><h2 style="font-size:22px">함께 보기</h2>'
            f'<div class="grid g3" style="margin-top:16px">{rel}</div></section></article>'
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
                               for n, _, u in TRUST_SOURCES]
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
    body = (_hero("매거진", "호빠알바, 제대로 알고 시작하기",
                  "입문부터 면접·정산·후기까지. 구직자에게 필요한 실용 정보를 정리한 호빠클럽 매거진입니다.") +
            f'<section class="wrap" style="padding-top:0"><div class="grid g2">{cards}</div></section>')
    ld = [breadcrumb([("홈", "/"), ("매거진", "/magazine/")])]
    return "/magazine/index.html", page(
        "호빠클럽 매거진 — 호빠알바 입문·면접·정산·후기 가이드",
        "호빠알바 시작하기, 지원·면접 가이드, 근무조건·정산 정보, 후기·인터뷰까지. 구직에 필요한 정보를 담은 호빠클럽 매거진.",
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
        '<select name="type" required><option>허위공고 신고</option><option>불법 요구 제보</option>'
        '<option>일반 문의</option><option>개인정보 관련</option></select></div>'
        '<div class="field"><label>내용<span class="req">*</span></label>'
        '<textarea name="message" rows="6" required placeholder="신고 시 매장명·지역·캡처 등 근거를 함께 적어 주세요."></textarea></div>'
        '<div class="field"><label><input type="checkbox" required style="width:auto;margin-right:8px">'
        '개인정보 수집·이용에 동의합니다.</label></div>'
        '<input class="hp" name="website" tabindex="-1" autocomplete="off">'
        '<button class="btn btn-gold" type="submit">문의 보내기</button>')
    body = (_hero("문의하기", "문의하기", "허위공고 신고나 일반 문의를 남겨 주세요. 접수된 내용은 내부 검토 후 순차적으로 답변드립니다.") +
            f'<section class="wrap" style="padding-top:0;max-width:720px">'
            f'<form class="card" method="post" action="/api/contact-ads">{fhtml}</form>'
            f'<div class="notice-box" style="margin-top:20px">긴급 상황은 112, 여성긴급전화 1366으로 즉시 도움을 받으세요. {AGE_NOTICE}</div></section>')
    ld = [breadcrumb([("홈", "/"), ("고객센터", "/support/"), ("문의하기", "/support/contact/")])]
    return "/support/contact/index.html", page(
        "문의하기 — 허위공고 신고·일반 문의 | 호빠클럽",
        "호빠클럽 문의하기. 허위공고 신고, 불법 요구 제보, 일반 문의를 접수합니다. 내부 검토 후 순차 답변드립니다.",
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
    # 상품 표
    rows = "".join(
        f'<tr><td><strong>{p["tier"]}</strong></td><td>{p["slot"]}</td><td>{p["limit"]}</td>'
        f'<td>{p["m1"]}</td><td>{p["m6"]}</td><td>{p["m12"]}</td></tr>' for p in AD_PRODUCTS)
    prod_cards = "".join(
        f'<div class="card"><span class="tag">{p["tier"]}</span>'
        f'<h3 style="margin:12px 0 8px">{p["slot"]}</h3><p style="font-size:13.5px">{p["desc"]}</p>'
        f'<p style="margin-top:10px;color:var(--g1);font-weight:700">1개월 {p["m1"]}원~</p></div>'
        for p in AD_PRODUCTS)

    def sec(id_, title, inner):
        return f'<section id="{id_}" class="wrap" style="padding-top:0"><h2>{title}</h2>{inner}</section>'

    body = (
        _hero("광고안내", "신뢰받는 매장을 위한 광고안내",
              "호빠클럽은 검수된 공고만 노출하는 채용정보 플랫폼입니다. 건전하게 운영되는 매장을 위한 광고 상품과 기준을 안내합니다.",
              '<a class="btn btn-gold" href="/advertising/contact/">광고문의 하기</a>') +
        sec("products", "광고 상품 안내",
            f'<div class="grid g3" style="margin-bottom:18px">{prod_cards}</div>'
            f'<table><thead><tr><th>등급</th><th>노출 위치</th><th>슬롯</th><th>1개월</th><th>6개월</th><th>12개월</th></tr></thead>'
            f'<tbody>{rows}</tbody></table>') +
        sec("placement", "노출 위치 안내",
            '<p>VVIP는 메인 히어로 직하 최상단, VIP는 주요 콘텐츠 상단, 프리미엄은 목록 하단에 노출됩니다. '
            '같은 등급 내에서는 선등록 순으로 배치되며, 지역·형태별로 노출이 분산됩니다.</p>') +
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
            f'<table><thead><tr><th>등급</th><th>1개월</th><th>6개월</th><th>12개월</th></tr></thead><tbody>' +
            "".join(f'<tr><td>{p["tier"]}</td><td>{p["m1"]}원</td><td>{p["m6"]}원</td><td>{p["m12"]}원</td></tr>'
                    for p in AD_PRODUCTS) + '</tbody></table>'
            '<p style="margin-top:10px;font-size:13px;color:var(--dim)">표시 금액은 부가세 별도이며, 프로모션에 따라 변동될 수 있습니다.</p>') +
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
           "offers": [{"@type": "Offer", "name": p["tier"], "price": p["m1"].replace("만", "0000"),
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
        '<div class="field"><label>광고 희망 위치<span class="req">*</span></label>'
        '<select name="placement" required><option>VVIP — 메인 최상단</option><option>VIP — 콘텐츠 상단</option>'
        '<option>프리미엄 — 목록 하단</option><option>상담 후 결정</option></select></div>'
        '<div class="field"><label>광고 희망 기간<span class="req">*</span></label>'
        '<select name="period" required><option>1개월</option><option>6개월</option><option>12개월</option><option>상담 후 결정</option></select></div>'
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


def all_pages():
    pages = [home(), jobs(), magazine_hub(), safety_hub(), support_hub(),
             notice_page(), faq_page(), support_contact(), about_page(),
             advertising(), advertising_contact()]
    pages += policy_pages()
    pages += _article_pages(MAGAZINE, "/magazine/", "매거진", "매거진")
    pages += _article_pages(SAFETY, "/safety/", "안전센터", "안전센터")
    return pages
