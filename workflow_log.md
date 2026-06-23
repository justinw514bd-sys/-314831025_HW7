# Agent 協作紀錄 (Workflow Log)

本文件完整記錄開發「兒童故事繪本生成器」過程中，開發者與 AI Agent 的協作歷程，包含關鍵 Prompt、工具架構及除錯紀錄。

---

## 🛠️ 使用的工具組合

本專案在 Agent 的建議與輔助下，確立了以下混合式雲端架構：
* **前端與介面**：`Gradio` (快速建立可互動的 Web UI)
* **大語言模型 (Story Agent)**：`Google Gemini 2.5 Flash` (使用官方原生套件 `google-generativeai` 進行 API 呼叫)
* **圖像生成 (Image Agent)**：`Hugging Face API` + `Stable Diffusion XL (SDXL)`
* **資料驗證**：`Pydantic` (嚴格定義 JSON 輸出的資料結構，防止前後端介接崩潰)

---

## 💬 開發過程中的關鍵 Prompt 紀錄

在發想與實作階段，開發者透過以下關鍵 Prompt 引導 Agent 協助建構系統：

**1. 系統架構與觀念釐清**
* **開發者 Prompt**：`用gemma4 呢` / `那他是給網路上去跑嗎？不是我電腦去跑模型`
* **Agent 協作**：Agent 釐清了開源模型版本資訊，並解釋了「本地端運算 (GPU)」與「雲端 API 運算」的差異。為符合期末專題的穩定性與效能考量，確立了「本地端架設 Gradio，將沉重運算交由 Google 伺服器」的混合架構策略。

**2. 核心功能實作 (System Prompt)**
* **開發者 Prompt** (定義於程式碼中)：
  ```text
  你是兒童故事創作家。請務必輸出 JSON 格式。格式包含 title 與 scenes 陣列，每個 scene 需有 story 欄位描述場景。
  使用者輸入主題：八月去北海道的五天冒險之旅。
  Agent 協作：協助將此 Prompt 整合進 Python 程式碼，並加入強制的 JSON MIME type 設定，確保模型輸出的格式能被 Pydantic 完美解析。

3. 錯誤排除與 Debug

開發者 Prompt：直接貼上終端機的錯誤追蹤碼 (Traceback)，例如：

openai.AuthenticationError: Error code: 401 - {'error': {'message': 'Missing Authentication header'}}

google.api_core.exceptions.NotFound: 404 models/gemini-1.5-flash is not found for API version v1beta

Agent 協作：Agent 根據錯誤碼精準定位問題（如金鑰未綁定、API 相容性問題、模型版本退役），並提供具體的修改步驟。

🐛 Agent 協助解決之技術問題
在實作與測試階段，遭遇了多次嚴重的連線與系統阻礙，皆透過 Agent 協作成功排除：

1. 跨越 401 憑證與 OpenAI 相容層障礙

問題：初期試圖以 OpenAI SDK 相容格式呼叫 Google 模型，卻持續遭遇 401 Missing Authentication header 錯誤。

解決方案：Agent 協助排查環境變數，並果斷建議放棄不穩定的第三方轉接層，全面改寫為 Google 官方原生套件 google-generativeai，從根本解決憑證無法正確傳遞的問題。

2. 繞過複雜的 Google Cloud 企業級權限陷阱

問題：在申請 API 金鑰時，誤入 Google Cloud 的「服務帳戶 (Service Account)」與「專案權限限制」的複雜介面，導致金鑰被鎖死在 Analytics Hub API，無法呼叫生成模型。

解決方案：Agent 指引開發者避開企業級後台，轉由開發者專屬的「Google AI Studio」快速通道重新申請 AQ. 開頭的萬能金鑰，免除所有不必要的權限設定綁定。

3. 解決 500 JSON 解析崩潰與 404 模型退役問題

問題：伺服器頻繁拋出 500 Internal Server Error (因舊版相容層無法處理強制 JSON 格式) 以及 404 Not Found (因 gemini-1.5-flash 模型近期退役)。

解決方案：Agent 協助修改程式邏輯，利用原生 SDK 的 generation_config 強制鎖定 JSON 輸出，並將環境變數更新為最新世代的 gemini-2.5-flash，最終打通任督二脈，實現系統的穩定運行。
