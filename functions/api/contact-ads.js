// Cloudflare Pages Function: 광고문의/일반문의 폼 → Telegram 봇 전송
// 환경변수: TELEGRAM_BOT_TOKEN_1, TELEGRAM_CHAT_ID_1 (필수)
//           TELEGRAM_BOT_TOKEN_2, TELEGRAM_CHAT_ID_2 (선택)
//           ALLOWED_ORIGIN (선택, 기본 *)

function clamp(v, max) {
  return (v == null ? "" : String(v)).trim().slice(0, max);
}

async function sendTelegram(token, chatId, text) {
  if (!token || !chatId) return;
  await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ chat_id: chatId, text, parse_mode: "HTML" }),
  });
}

export async function onRequestPost(context) {
  const { request, env } = context;
  const origin = env.ALLOWED_ORIGIN || "*";
  const cors = {
    "Access-Control-Allow-Origin": origin,
    "Content-Type": "application/json; charset=utf-8",
  };

  try {
    const ct = request.headers.get("content-type") || "";
    let data = {};
    if (ct.includes("application/json")) {
      data = await request.json();
    } else {
      const form = await request.formData();
      for (const [k, v] of form.entries()) data[k] = v;
    }

    // honeypot: 봇이 채우는 숨김 필드
    if (clamp(data.website, 100)) {
      return new Response(JSON.stringify({ ok: true }), { headers: cors });
    }

    const company = clamp(data.company || data.name, 80);
    const manager = clamp(data.manager, 60);
    const phone = clamp(data.phone || data.contact, 60);
    const email = clamp(data.email, 120);
    const placement = clamp(data.placement, 60);
    const period = clamp(data.period, 40);
    const type = clamp(data.type, 40);
    const message = clamp(data.message, 2000);

    // 서버측 최소 검증
    if (message.length < 5 || (!phone && !email && !company)) {
      return new Response(JSON.stringify({ ok: false, error: "입력값을 확인해 주세요." }), {
        status: 400,
        headers: cors,
      });
    }

    const lines = [
      "<b>📩 호빠클럽 문의 접수</b>",
      type && `유형: ${type}`,
      company && `상호/이름: ${company}`,
      manager && `담당자: ${manager}`,
      phone && `연락처: ${phone}`,
      email && `이메일: ${email}`,
      placement && `희망 위치: ${placement}`,
      period && `희망 기간: ${period}`,
      "",
      message,
    ].filter(Boolean);
    const text = lines.join("\n");

    await sendTelegram(env.TELEGRAM_BOT_TOKEN_1, env.TELEGRAM_CHAT_ID_1, text);
    await sendTelegram(env.TELEGRAM_BOT_TOKEN_2, env.TELEGRAM_CHAT_ID_2, text);

    return new Response(JSON.stringify({ ok: true }), { headers: cors });
  } catch (e) {
    return new Response(JSON.stringify({ ok: false, error: "처리 중 오류가 발생했습니다." }), {
      status: 500,
      headers: cors,
    });
  }
}

export async function onRequestOptions(context) {
  const origin = context.env.ALLOWED_ORIGIN || "*";
  return new Response(null, {
    headers: {
      "Access-Control-Allow-Origin": origin,
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    },
  });
}
