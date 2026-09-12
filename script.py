import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : REMETTEZ VOS DEUX LIGNES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-likes"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jSd3bf/"
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
            
            print("Insertion du lien...")
            champ_texte = page.locator("input[type='text'], input[type='url'], textarea").first
            await champ_texte.fill(LIEN_A_COLLER)
            
            # SOLUTION RAPIDE : Simule l'appui sur la touche Entrée du clavier
            print("Validation par la touche Entrée...")
            await champ_texte.press("Enter")
            
            # Solution de secours : Clic sur le bouton si Entrée n'a pas suffi
            print("Clic de sécurité sur le bouton...")
            bouton = page.locator("button:has-text('Get now'), input[value='Get now']").first
            await bouton.click(force=True)
            
            print("Tâche exécutée !")
            await page.wait_for_timeout(5000)
            
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
