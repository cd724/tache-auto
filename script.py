import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : RECOPIEZ BIEN VOS DEUX LIGNES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-likes"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jSSMu2/"
# =====================================================================

async def soumettre_tache():
    async with async_playwright() as p:
        # Configuration en français pour le navigateur
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(locale="fr-FR", timezone_id="Europe/Paris")
        page = await context.new_page()
        
        try:
            print(f"Connexion à : {URL_DU_SITE}...")
            await page.goto(URL_DU_SITE)
            await page.wait_for_load_state("networkidle")
            
            print("Insertion du lien...")
            champ_texte = page.locator("input[type='text'], input[type='url'], textarea").first
            await champ_texte.fill(LIEN_A_COLLER)
            
            # Recherche uniquement le bouton "Get now"
            print("Clic sur le bouton Get now...")
            bouton = page.locator("button:has-text('Get now'), input[value='Get now']").first
            await bouton.click()
            
            print("Tâche exécutée avec succès !")
            await page.wait_for_timeout(5000)
            
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
