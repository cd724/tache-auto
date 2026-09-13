import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : REMETTEZ VOS DEUX LIGNES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-likes"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jfjrSm/"
# =====================================================================

async def soumettre_tache():
    async with async_playwright() as p:
        # Ajout d'arguments réseau avancés pour masquer le centre de données (Datacenter)
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled", # Cache le fait que c'est un robot
                "--use-fake-device-for-media-stream",
                "--disable-web-security"
            ]
        )
        
        # Utilisation d'un profil de navigateur mobile standard (Pixel 5)
        mobile_device = p.devices['Pixel 5']
        context = await browser.new_context(
            **mobile_device,
            locale="en-US",
            timezone_id="Europe/Paris",
            # On simule des entêtes de requêtes réseau totalement humaines
            extra_http_headers={
                "Accept-Language": "en-US,en;q=0.9",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": mobile_device['user_agent']
            }
        )
        page = await context.new_page()
        
        try:
            print(f"Connexion masquée au site : {URL_DU_SITE}")
            await page.goto(URL_DU_SITE)
            await page.wait_for_load_state("networkidle")
            await page.wait_for_timeout(5000)
            
            # Recherche de la case de saisie
            print("Recherche de la case...")
            champ = page.locator("input[placeholder*='Paste your'], input[type='text'], input[type='url']").first
            
            if await champ.count() > 0:
                print("Case trouvée ! Saisie du lien...")
                await champ.click()
                await champ.fill(LIEN_A_COLLER)
                await page.wait_for_timeout(2000)
            else:
                print("ATTENTION : La case n'a pas été trouvée.")
                
            # Recherche et clic sur le bouton "Get Now"
            print("Recherche du bouton 'Get Now'...")
            bouton = page.locator("button:has-text('Get Now'), input[value='Get Now']").first
            
            if await bouton.count() > 0:
                print("Bouton trouvé ! Envoi de l'action...")
                await bouton.focus()
                await bouton.click(force=True)
                print("Clic effectué avec succès !")
            else:
                print("ATTENTION : Le bouton 'Get Now' n'a pas été trouvé.")
                
            await page.wait_for_timeout(8000)
            
        except Exception as e:
            print(f"Erreur durant l'exécution : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
