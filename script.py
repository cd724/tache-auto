import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : REMETTEZ VOS DEUX LIGNES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-likes"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jDW3HB/"
# =====================================================================

async def soumettre_tache():
    async with async_playwright() as p:
        # On force la langue anglaise pour correspondre à l'affichage "Get Now"
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(locale="en-US")
        page = await context.new_page()
        
        try:
            print(f"Connexion au site : {URL_DU_SITE}")
            await page.goto(URL_DU_SITE)
            await page.wait_for_load_state("networkidle")
            
            # 1. Sélection de la case qui commence par "Paste your"
            print("Insertion du lien dans le formulaire...")
            champ = page.locator("input[placeholder^='Paste your'], textarea[placeholder^='Paste your']").first
            await champ.click()
            await champ.fill(LIEN_A_COLLER)
            
            # 2. Clic strict sur le bouton d'action "Get Now"
            print("Validation par clic sur 'Get Now'...")
            bouton = page.get_by_text("Get Now", exact=True).first
            await bouton.click()
            
            print("Action envoyée avec succès !")
            await page.wait_for_timeout(4000)
            
        except Exception as e:
            print(f"Erreur durant l'exécution : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
