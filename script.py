import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : REMETTEZ SOS DEUX LIGNES EXACTES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-likes"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jf6sNM/"
# =====================================================================

async def soumettre_tache():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        mobile_device = p.devices['Pixel 5']
        context = await browser.new_context(
            **mobile_device,
            locale="en-US",
            timezone_id="Europe/Paris"
        )
        page = await context.new_page()
        
        try:
            print(f"Connexion au site : {URL_DU_SITE}")
            await page.goto(URL_DU_SITE)
            await page.wait_for_load_state("networkidle")
            # Attente pour s'assurer que tous les éléments du site sont stables
            await page.wait_for_timeout(5000)
            
            # Recherche de la case de saisie
            print("Recherche de la case...")
            champ = page.locator("input[placeholder*='Paste your'], input[type='text'], input[type='url']").first
            
            if await champ.count() > 0:
                print("Case trouvée ! Nettoyage et focus...")
                await champ.click()
                await champ.focus()
                
                # Tape le lien lentement (150 millisecondes de pause entre chaque lettre)
                # Cela empêche le site d'abréger ou de bloquer le lien
                print(f"Écriture humaine du lien complet...")
                await champ.type(LIEN_A_COLLER, delay=150)
                await page.wait_for_timeout(2000)
                
                # Option de sécurité : simule un appui sur Entrée
                await champ.press("Enter")
                await page.wait_for_timeout(1000)
            else:
                print("ATTENTION : La case n'a pas été trouvée.")
                
            # Recherche et clic sur le bouton "Get Now"
            print("Recherche du bouton 'Get Now'...")
            bouton = page.locator("button:has-text('Get Now'), input[value='Get Now']").first
            
            if await bouton.count() > 0:
                print("Bouton trouvé ! Clic forcé...")
                await bouton.focus()
                await bouton.click(force=True)
                print("Clic effectué avec succès !")
            else:
                print("ATTENTION : Le bouton 'Get Now' n'a pas été trouvé.")
                
            # Laisse 8 secondes au site pour traiter la validation après le clic
            await page.wait_for_timeout(8000)
            
        except Exception as e:
            print(f"Erreur durant l'exécution : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
