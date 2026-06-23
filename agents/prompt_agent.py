from openai import OpenAI
from config.settings import settings

client = OpenAI(
    api_key=settings.PROMPT_API_KEY,
    base_url=settings.PROMPT_BASE_URL
)

SYSTEM_PROMPT = """
你是 Stable Diffusion Prompt Engineer。

請根據故事內容產生高品質英文 Prompt。

不要解釋。
只輸出 Prompt。
"""

def generate_prompt(scene_text: str) -> str:

    response = client.chat.completions.create(
        model=settings.PROMPT_MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": scene_text
            }
        ]
    )

    return response.choices[0].message.content.strip()