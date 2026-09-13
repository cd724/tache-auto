import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : REMETTEZ VOS DEUX LIGNES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-likes"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jDuTbY/"
# =====================================================================

async def soumettre_tache():
    async with async_playwright() as p:
        # On simule un vrai téléphone (Pixel 5) en mode tactile pour tromper le site
        browser = await p.chromium.launch(headless=True)
        iphone = p.devices['Pixel 5']
        context = await browser.new_context(**iphone, locale="en-US")
        page = await context.new_page()
        
        try:
            print(f"Connexion au site en mode mobile : {URL_DU_SITE}")
            await page.goto(URL_DU_SITE)
            await page.wait_for_load_state("networkidle")
            await page.wait_for_timeout(2000)
            
            # 1. On cherche la case et on simule un vrai clic physique dessus
            print("Ciblage et clic humain sur la case...")
            champ = page.locator("input[placeholder^='Paste your'], textarea[placeholder^='Paste your']").first
            
            # On utilise 'tap' au lieu de 'click' pour imiter un doigt sur un écran
            await champ.tap()
            await page.wait_for_timeout(1000)
            
            # On vide le champ et on tape le lien
            await champ.fill("")
            await champ.type(LIEN_A_COLLER, delay=100) # Tape lentement comme un humain
            await page.wait_for_timeout(1000)
            
            # 2. On cherche le bouton 'Get Now' et on fait une pression tactile forcée
            print("Pression tactile sur le bouton 'Get Now'...")
            bouton = page.get_by_text("Get Now", exact=True).first
            
            # On force le focus et on tape avec le doigt virtuel
            await bouton.focus()
            await bouton.tap()
            
            print("Action envoyée de manière forcée !")
            await page.wait_for_timeout(5000)
            
        except Exception as e:
            print(f"Erreur technique rencontrée : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
