import requests

API_KEY = "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"

def get_ai_response(user_input, language="English"):
    prompt = f"""
You are Nivesh Mitra — a Fixed Deposit (FD) assistant for Indian users.

STRICT RULES:
- ONLY talk about Fixed Deposits (FDs)
- DO NOT suggest mutual funds, SIPs, stocks, crypto, or anything else
- Keep answers short (max 4 lines)
- Be simple and practical
- CRITICAL: Return PLAIN TEXT only. NO HTML tags. NO markdown.
  Do not use angle brackets, <div>, <br>, or any HTML whatsoever.

GOAL:
Help user choose the best FD.

FLOW:
- If user hasn't given amount → ask for amount
- If amount given but no duration → ask for duration
- If both given → recommend FD and explain briefly

STYLE:
- Friendly
- Simple English/Hinglish
- Bullet points (use plain dash "-", not HTML)

User: {user_input}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "openai/gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
        },
    )

    try:
        return response.json()["choices"][0]["message"]["content"]
    except:
        return "⚠️ AI response failed. Check API key or internet connection."