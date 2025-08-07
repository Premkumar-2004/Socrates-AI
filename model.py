import os
import asyncio
from browser_use import Agent, Browser, BrowserConfig
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

# ✅ Set API Key
api_key = "AIzaSyBnDf1W6kbFd7wldJY2oeSmM0dv3HNkICc"
if not api_key:
    raise ValueError('GEMINI_API_KEY is not set')

# ✅ Configure Browser (Chrome with UI)
browser = Browser(
    config=BrowserConfig(
        chrome_instance_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
       
    )
)

# ✅ Create Agent
agent = Agent(
    task=(
        "1. Navigate to https://www.stytch.com/ "
        "2. Wait until the page loads fully "
        "3. Click 'Dashboard' "
        "4. Click 'User management' "
        "5. Click 'Create new user'"
    ),
    llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key)),
    browser=browser,
)

async def main():
    # ✅ Open Browser and Navigate
    await agent.run()
    
    # ✅ Ensure Page is Loaded
    await asyncio.sleep(5)  # Wait for the page to load
    print("✅ Page Loaded Successfully!")

    # ✅ Manual Exit
    input('Press Enter to close the browser...')
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

    
'''
import os
import sys
from pathlib import Path

from browser_use.agent.views import ActionResult
#from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from pydantic import SecretStr
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio


from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
	raise ValueError('GEMINI_API_KEY is not set')

browser = Browser(
    config=BrowserConfig(
        chrome_instance_path='/usr/bin/google-chrome', 
    )
)

async def main():
	task = 'Browser agent result: 1. Navigate to https://www.stytch.com/ 2. Click "Log in" 3. Click "Continue With Google" 4. Type "mohanavamsi991" 5. Click "next" 6. Type "vamsi99999" 7. Click backspace 8. Click "next" 9. Click "Continue" 10. Select First Organization if prompted 11. Click "User management" 12. Click "Create new user" 13. Click the "Email address" field. 14. Type "bob@example.com" 15. Click the "Phone number" field. 16. Type "+15555555555" 17. Click the "First name" field. 18. Type "Bob" 19. Click the "Last name" field. 20. Type "User" 21. Click "Save" 22. Click "Save changes"'
	#model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(str(api_key)))
	llm = ChatAnthropic(model_name='claude-3-7-sonnet-20250219', temperature=0.0, timeout=30, stop=None)
	agent = Agent(
		task=task,
		llm=llm,
	)

	await agent.run()
	await browser.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())
 
 '''