import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : REMETTEZ VOS DEUX LIGNES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-likes"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jUPnMe/"
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
            
            # Vérification de la présence de la case
            champ = page.locator("input[placeholder^='Paste your'], textarea[placeholder^='Paste your']").first
            if await champ.count() > 0:
                print("Case 'Paste your link' trouvée. Insertion du lien...")
                await champ.click()
                await champ.fill(LIEN_A_COLLER)
            else:
                print("ATTENTION : La case de saisie n'a pas été trouvée sur la page.")
            
            # Vérification de la présence du bouton
            bouton = page.get_by_text("Get Now", exact=True).first
            if await bouton.count() > 0:
                print("Bouton 'Get Now' trouvé. Clic en cours...")
                await bouton.click()
                print("Clic effectué avec succès !")
            else:
                print("ATTENTION : Le bouton 'Get Now' n'a pas été trouvé.")
            
            # Enregistre une image témoin pour voir ce que le robot voit
            await page.screenshot(path="resultat.png")
            print("Capture d'écran de contrôle enregistrée sous le nom 'resultat.png'.")
            await page.wait_for_timeout(4000)
            
        except Exception as e:
            print(f"Erreur durant l'exécution : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
