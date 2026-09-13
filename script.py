import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : REMETTEZ VOS DEUX LIGNES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-likes"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jAGdMq/"
# =====================================================================

async def soumettre_tache():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(locale="fr-FR", timezone_id="Europe/Paris")
        page = await context.new_page()
        
        try:
            print(f"Connexion à : {URL_DU_SITE}...")
            await page.goto(URL_DU_SITE)
            await page.wait_for_load_state("networkidle")
            
            # 1. Trouve la case "Paste your link" et colle le lien
            print("Ciblage de la case 'Paste your link'...")
            champ = page.locator("input[placeholder*='Paste your link'], input[placeholder*='link']").first
            await champ.click()
            await champ.fill(LIEN_A_COLLER)
            
            # 2. Clic STRICT sur le bouton "Get now" (grâce à exact=True)
            print("Clic précis sur le bouton exact 'Get now'...")
            bouton = page.get_by_text("Get now", exact=True).first
            await bouton.click()
            
            print("Tâche exécutée avec succès !")
            await page.wait_for_timeout(5000)
            
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
