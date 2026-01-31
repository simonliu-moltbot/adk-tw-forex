import asyncio
import os
import sys
from dotenv import load_dotenv

# Ensure we can import from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from google.adk.runners import Runner
from google.adk.services import InMemorySessionService
from tw_forex.agent import create_agent

async def main():
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in environment variables.")
        print("Please set it in .env or export it.")
        return

    # Initialize Agent
    agent = create_agent(model_name="gemini-2.5-flash")
    
    # Initialize Service and Runner
    session_service = InMemorySessionService()
    runner = Runner(agent=agent, session_service=session_service)
    
    session_id = "session_001"
    
    print("🇹🇼 匯率小幫手 (Taiwan Forex Bot) 已啟動！ (按 Ctrl+C 退出)")
    print("你可以問：'現在日幣匯率多少？' 或 '我想買美金'")
    
    while True:
        try:
            user_input = input("\nUse > ")
            if not user_input:
                continue
                
            if user_input.lower() in ["exit", "quit"]:
                break
            
            # Run the agent
            # ADK Runner.run takes (session_id, input)
            # It returns a result object or stream
            # Let's assume generic run usage
            result = await runner.run(session_id=session_id, input=user_input)
            
            # Print response
            print(f"Agent > {result.output.text}")
            
        except KeyboardInterrupt:
            print("\nBye!")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    asyncio.run(main())
