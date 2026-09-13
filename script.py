import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : REMETTEZ VOS DEUX LIGNES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-likes"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jUgah6/"
# =====================================================================

async def soumettre_tache():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(locale="en-US")
        page = await context.new_page()
        
        try:
            print(f"Connexion au site : {URL_DU_SITE}")
            await page.goto(URL_DU_SITE)
            await page.wait_for_load_state("networkidle")
            await page.wait_for_timeout(3000)
            
            # METHODE ABSOLUE : On prend le tout premier champ de saisie de la page, peu importe son nom
            champ = page.locator("input").first
            
            if await champ.count() > 0:
                print("Case de saisie principale trouvée. Insertion du lien...")
                await champ.click()
                await champ.fill(LIEN_A_COLLER)
                await page.wait_for_timeout(1000)
                
                # Appui sur Entrée pour valider au cas où le bouton échoue
                await champ.press("Enter")
                await page.wait_for_timeout(1000)
            else:
                print("ATTENTION : Aucun champ de saisie 'input' trouvé sur la page.")
            
            # Recherche et clic sur le bouton
            bouton = page.get_by_text("Get Now", exact=True).first
            if await bouton.count() > 0:
                print("Bouton 'Get Now' trouvé. Clic en cours...")
                await bouton.click(force=True)
                print("Clic effectué avec succès !")
            else:
                print("ATTENTION : Le bouton 'Get Now' n'a pas été trouvé.")
            
            await page.wait_for_timeout(5000)
            
        except Exception as e:
            print(f"Erreur durant l'exécution : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
