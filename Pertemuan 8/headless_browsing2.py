import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.w3schools.com/python/')
    
    # Mengekstrak teks dari elemen tertentu
    element = await page.querySelector('h1')
    text = await page.evaluate('(element) => element.textContent', element)
    
    print(f"Teks yang diekstrak: {text}")
    
    await browser.close()

asyncio.run(main())
