import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : REMETTEZ VOS DEUX LIGNES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-likes"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jyN7Ne/"
# =====================================================================

async def soumettre_tache():
    async with async_playwright() as p:
        # Configuration avancée pour imiter un vrai téléphone et éviter le blocage
        browser = await p.chromium.launch(headless=True)
        # On simule un profil de smartphone moderne (Samsung Galaxy S22)
        device = p.devices['Galaxy S22 Ultra']
        context = await browser.new_context(
            **device,
            locale="en-US",
            timezone_id="Europe/Paris"
        )
        page = await context.new_page()
        
        try:
            print(f"Connexion au site en mode masqué : {URL_DU_SITE}")
            await page.goto(URL_DU_SITE)
            # Attend que le site charge ses protections en arrière-plan
            await page.wait_for_load_state("networkidle")
            await page.wait_for_timeout(4000)
            
            # 1. Recherche de la case en utilisant les attributs exacts de Zefame
            print("Recherche de la case de saisie...")
            champ = page.locator("input[placeholder*='Paste your'], input[type='text'], input[type='url']").first
            
            if await champ.count() > 0:
                print("Case trouvée ! Remplissage du lien...")
                await champ.click()
                await champ.fill(LIEN_A_COLLER)
                await page.wait_for_timeout(1000)
            else:
                print("ATTENTION : La case n'a pas été trouvée avec cette configuration.")
                
            # 2. Clic sur le bouton exact "Get Now"
            print("Recherche du bouton 'Get Now'...")
            bouton = page.locator("button:has-text('Get Now'), input[value='Get Now']").first
            
            if await bouton.count() > 0:
                print("Bouton trouvé ! Validation de la tâche...")
                await bouton.click(force=True)
                print("Clic effectué avec succès !")
            else:
                print("ATTENTION : Le bouton 'Get Now' n'a pas été trouvé.")
                
            # Attente de sécurité pour laisser le site enregistrer l'action
            await page.wait_for_timeout(5000)
            
        except Exception as e:
            print(f"Erreur durant l'exécution : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
