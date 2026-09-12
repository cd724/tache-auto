import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : REMETTEZ VOS DEUX LIGNES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-saves"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jSq1xQ/"
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
            
            # METHODE FORCEE : Injecte directement le lien dans la case par le code du site
            print("Injection directe du lien...")
            await page.evaluate(f"""
                let champ = document.querySelector("input[type='text'], input[type='url'], textarea");
                if (champ) {{
                    champ.value = "{LIEN_A_COLLER}";
                    champ.dispatchEvent(new Event('input', {{ bubbles: true }}));
                }}
            """)
            
            # METHODE FORCEE : Recherche et clique sur le bouton de manière absolue
            print("Validation forcée de la tâche...")
            await page.evaluate("""
                let bouton = document.querySelector("button:has-text('Get now'), button, input[type='submit']");
                if (bouton) bouton.click();
            """)
            
            print("Tâche envoyée au site !")
            await page.wait_for_timeout(5000)
            
        except Exception as e:
            print(f"Erreur rencontrée : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
