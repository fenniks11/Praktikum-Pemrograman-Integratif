import asyncio
from pyppeteer import launch

async def main():
    print("Meluncurkan browser...")
    browser = await launch()
    print("Membuka halaman baru...")
    page = await browser.newPage()
    print("Menuju ke URL...")
    await page.goto('https://www.w3schools.com/python/')
    print("Mengambil tangkapan layar...")
    await page.screenshot({'path': 'example.png'})
    print("Menutup browser...")
    await browser.close()
    print("Tangkapan layar berhasil disimpan sebagai example.png")

asyncio.run(main())
