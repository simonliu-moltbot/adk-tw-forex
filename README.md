# Taiwan Forex Bot (匯率小幫手) 🇹🇼

An AI Agent built with Google ADK that provides real-time exchange rates from the Bank of Taiwan (台灣銀行).

## Features
- Check real-time Buying/Selling rates for major currencies (USD, JPY, EUR, etc.).
- Distinguishes between Cash (現金) and Spot (即期) rates.
- Conversational interface in Traditional Chinese.

## Setup

1. **Clone the repo**
   ```bash
   git clone <your-repo-url>
   cd adk-tw-forex
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set API Key**
   Create a `.env` file or export the variable:
   ```bash
   export GOOGLE_API_KEY="your-gemini-api-key"
   ```

## Usage

Run the agent:
```bash
python src/main.py
```

### Example Queries
- "現在日幣匯率多少？" (What is the JPY rate?)
- "我想去日本玩，要換現金" (I want to go to Japan, need cash.)
- "美金現在銀行買入價是多少？" (What is the USD buying rate?)

## Data Source
- Bank of Taiwan Open Data (CSV): `https://rate.bot.com.tw/xrt/flcsv/0/day`
