import json
import google.generativeai as genai
from config.settings import settings
from agents.story_schema import StoryResponse

# 1. 綁定你的 AIza 金鑰 (原生套件不需要 base_url)
genai.configure(api_key=settings.STORY_API_KEY)

# 2. 系統提示詞
SYSTEM_PROMPT = """
你是兒童故事創作家。
請務必輸出 JSON。
格式如下：
{
  "title":"月球貓咪大冒險",
  "scenes":[
    {
      "story":"..."
    },
    {
      "story":"..."
    },
    {
      "story":"..."
    }
  ]
}
"""

def generate_story(topic: str) -> StoryResponse:
    # 3. 建立原生模型，並直接在底層強制鎖定 JSON 輸出格式
    model = genai.GenerativeModel(
        model_name=settings.STORY_MODEL,
        system_instruction=SYSTEM_PROMPT,
        generation_config={
            "response_mime_type": "application/json"
        }
    )

    print(f"☁️ 正在透過 Google 原生 API 撰寫故事 (主題: {topic})...")
    
    # 直接呼叫生成
    response = model.generate_content(topic)

    # 4. 讀取並驗證 JSON
    data = json.loads(response.text)
    
    print("✅ 故事劇本生成完畢！")
    return StoryResponse.model_validate(data)