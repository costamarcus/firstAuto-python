from playwright.sync_api import  sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) # headless
    pagina = navegador.new_page()
    pagina.goto("https://www.google.com.br")
    pagina.fill('xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input', 'Cataguases')
    pagina.locator('xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
    time.sleep(5)