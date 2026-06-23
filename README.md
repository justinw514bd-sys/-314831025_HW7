# 兒童故事繪本生成器 (HW7)

## 📖 專題說明
本專題為一個自動化兒童故事與繪本生成系統。使用者只需輸入感興趣的「主題」，系統便會自動發想並產出完整的分鏡劇本，同時為每一個場景生成對應的精美插圖，打造出圖文並茂的專屬繪本。

## 🏗️ 系統架構說明
本專案採用混合式 API 架構，將前端介面與雲端生成模型進行整合：
* **前端互動介面 (UI)**：使用 `Gradio` 打造直覺的網頁操作介面。
* **故事與劇本生成 (Story Agent)**：整合 Google 原生套件 `google-generativeai`，呼叫最新世代的 **Gemini 2.5 Flash** 模型。負責將使用者的簡短主題，擴寫為包含場景描述與對白的結構化 JSON 劇本。
* **插圖生成 (Image Agent)**：透過 Hugging Face API 介接 **Stable Diffusion XL (SDXL)** (`stabilityai/stable-diffusion-xl-base-1.0`) 模型，根據 Gemini 生成的場景描述，自動繪製出對應的繪本圖片。

## 🚀 本地端執行詳細步驟

### 1. 安裝環境依賴套件
請確保你的電腦已安裝 Python 3.8 以上版本。開啟終端機並切換至專案資料夾，執行以下指令安裝必備套件：
```bash
pip install -r requirements.txt

# Story LLM (填入 Google AI Studio 的金鑰，如 AQ. 開頭)
STORY_API_KEY=你的_Google_API_Key
STORY_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
STORY_MODEL=gemini-2.5-flash

# Prompt LLM (同上)
PROMPT_API_KEY=你的_Google_API_Key
PROMPT_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
PROMPT_MODEL=gemini-2.5-flash

# HuggingFace (填入你的 HF Token)
HF_TOKEN=你的_HuggingFace_Token

# SDXL 模型設定 (維持預設即可)
SD_MODEL=stabilityai/stable-diffusion-xl-base-1.0

python app.py
