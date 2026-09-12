import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : CHANGEZ CES DEUX LIGNES AVEC VOS INFOS
# =====================================================================
URL_DU_SITE = "https://zefame.com/free-tiktok-likes"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jMk7oe/"
# =====================================================================

async def soumettre_tache():
    async with async_playwright() as p:
        # Sur le serveur, le navigateur doit obligatoirement être invisible (headless=True)
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        try:
            print(f"Connexion à : {URL_DU_SITE}...")
            await page.goto(URL_DU_SITE)
            await page.wait_for_load_state("networkidle")
            
            print("Insertion du lien...")
            champ_texte = page.locator("input[type='text'], input[type='url'], textarea").first
            await champ_texte.fill(LIEN_A_COLLER)
            
            print("Clic sur le bouton 'Obtenir'...")
            bouton = page.locator("button:has-text('Obtenir'), input[value='Obtenir']").first
            await bouton.click()
            
            print("Tâche exécutée avec succès sur le serveur !")
            await page.wait_for_timeout(5000)
            
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
