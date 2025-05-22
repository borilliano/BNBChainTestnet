import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False, args=['--start-maximized'])
    page = await browser.newPage()
    await page.goto('https://faucets.chain.link/', {'waitUntil': 'networkidle2'})

    # Wait for page to load
    await page.waitForSelector('input[type="text"]', timeout=15000)

    # Example: Enter wallet address (replace with your testnet address)
    wallet_address = '0xYourTestnetWalletAddress'
    await page.type('input[type="text"]', wallet_address)

    # Select BNB Chain (may need to adjust selector based on UI changes)
    await page.click('label[for="bnbChain"]')  # Adjust selector as needed

    # Click the "Send Request" or equivalent button
    await page.click('button[type="submit"]')  # Adjust selector as needed

    # Wait for confirmation or result
    await page.waitFor(5000)  # Wait 5 seconds for demonstration

    print("Faucet request sent (if all went well).")
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
