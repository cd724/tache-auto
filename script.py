import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : METTEZ VOS DEUX LIGNES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-likes"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jAEjsT/"
# =====================================================================

async def soumettre_tache():
    async with async_playwright() as p:
        # On lance le navigateur du serveur en mode anglais natif
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(locale="en-US")
        page = await context.new_page()
        
        try:
            print(f"Connexion au site : {URL_DU_SITE}")
            await page.goto(URL_DU_SITE)
            await page.wait_for_load_state("networkidle")
            
            # 1. Trouve la case qui commence par "Paste your TikTok link"
            print("Recherche de la case de saisie...")
            champ = page.locator("input[placeholder^='Paste your'], textarea[placeholder^='Paste your']").first
            await champ.click()
            await champ.fill(LIEN_A_COLLER)
            
            # 2. Clic sur le bouton exact "Get Now"
            print("Clic sur le bouton Get Now...")
            bouton = page.get_by_text("Get Now", exact=True).first
            await bouton.click()
            
            print("Action envoyée avec succès au site !")
            await page.wait_for_timeout(4000)
            
        except Exception as e:
            print(f"Erreur technique : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
