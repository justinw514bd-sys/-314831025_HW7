from pathlib import Path
import uuid
from huggingface_hub import InferenceClient
from config.settings import settings

# 建立雲端連線客戶端，帶入你的 HF Token
client = InferenceClient(token=settings.HF_TOKEN)

OUTPUT_DIR = Path("outputs/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def generate_image(prompt: str) -> str:
    print(f"☁️ 正在透過 Hugging Face 雲端生成圖片 (Prompt: {prompt[:30]}...)")
    
    # 呼叫雲端 API 算圖，不吃本地端顯卡資源
    image = client.text_to_image(
        prompt,
        model=settings.SD_MODEL
    )

    filename = f"{uuid.uuid4().hex}.png"
    filepath = OUTPUT_DIR / filename
    
    image.save(filepath)
    print(f"✅ 圖片生成完畢: {filepath}")

    return str(filepath)