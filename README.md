# Taiwan Forex Bot (匯率小幫手) 🇹🇼

[English](#english) | [繁體中文](#繁體中文)

---

<a name="english"></a>
## 🇬🇧 English

An AI Agent built with Google ADK (Agent Development Kit) that provides real-time exchange rates from the Bank of Taiwan.

### Features
- **Real-time Rates**: Fetches Buying/Selling rates for major currencies (USD, JPY, EUR, etc.).
- **Rate Types**: Distinguishes between Cash (現金) and Spot (即期) rates.
- **Bilingual Interface**: The agent communicates in Traditional Chinese, but the project supports standard ADK tooling.

### Prerequisites
- Python 3.10+
- Google Cloud Project with Gemini API enabled.
- `GOOGLE_API_KEY` set in `.env` file.

### Quick Start

1. **Setup Environment**
   ```bash
   pip install -r requirements.txt
   echo "GOOGLE_API_KEY=your_key_here" > .env
   ```

2. **Run with Web UI (Recommended)**
   Using Makefile:
   ```bash
   make dev
   ```
   Or directly with ADK CLI:
   ```bash
   adk web .
   ```
   Then open `http://localhost:8000` to interact with the agent.

3. **Run with Docker**
   ```bash
   make build
   make run
   ```

4. **Run CLI (Legacy)**
   ```bash
   python tw_forex/main.py
   ```

### Project Structure
- `tw_forex/`: Agent source code.
- `Dockerfile`: Production-ready container config.
- `Makefile`: Shortcut commands for build and run.

---

<a name="繁體中文"></a>
## 🇹🇼 繁體中文

這是一個使用 Google ADK 構建的 AI 代理，提供台灣銀行即時匯率查詢服務。

### 功能
- **即時匯率**：查詢主要貨幣（美元、日圓、歐元等）的買入/賣出匯率。
- **匯率類型**：區分現金匯率（Cash）與即期匯率（Spot）。
- **中文對話**：專為繁體中文使用者設計的對話介面。

### 系統需求
- Python 3.10+
- 已啟用 Gemini API 的 Google Cloud 專案。
- 在 `.env` 檔案中設定 `GOOGLE_API_KEY`。

### 快速開始

1. **環境設定**
   ```bash
   pip install -r requirements.txt
   echo "GOOGLE_API_KEY=your_key_here" > .env
   ```

2. **啟動網頁介面（推薦）**
   使用 Makefile：
   ```bash
   make dev
   ```
   或直接使用 ADK CLI：
   ```bash
   adk web .
   ```
   瀏覽器打開 `http://localhost:8000` 即可使用。

3. **使用 Docker 執行**
   ```bash
   make build
   make run
   ```

4. **執行命令行介面（舊版）**
   ```bash
   python tw_forex/main.py
   ```

### 專案結構
- `tw_forex/`: 代理程式原始碼。
- `Dockerfile`: Docker 容器設定檔。
- `Makefile`: 常用指令集。
