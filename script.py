import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : VOS DEUX LIGNES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-likes"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jff3B6/"
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
            await page.wait_for_timeout(5000)
            
            # --- FORCE UNLOCK (DÉVERROUILLAGE FORCE DE LA PAGE) ---
            print("Suppression des verrous et blocages sur la page...")
            await page.evaluate("""
                // Ce code cherche partout les attributs 'disabled' ou verrouillés et les détruit
                document.querySelectorAll("input, button").forEach(el => {
                    el.removeAttribute("disabled");
                    el.removeAttribute("readonly");
                    el.style.pointerEvents = "auto";
                    el.style.opacity = "1";
                });
            """)
            
            # 1. Insertion du lien
            print("Recherche de la case...")
            champ = page.locator("input[placeholder*='Paste your'], input[type='text']").first
            await champ.click()
            await champ.fill(LIEN_A_COLLER)
            await page.wait_for_timeout(2000)
            
            # 2. Clic forcé sur le bouton
            print("Recherche et clic forcé sur 'Get Now'...")
            bouton = page.locator("button:has-text('Get Now'), input[value='Get Now']").first
            
            # On force le clic par le code pour ignorer l'état "locked" visuel
            await bouton.evaluate("node => node.click()")
            print("Clic forcé envoyé au serveur !")
            
            await page.wait_for_timeout(8000)
            
        except Exception as e:
            print(f"Erreur durant l'exécution : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
