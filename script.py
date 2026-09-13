import asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : REMETTEZ VOS DEUX LIGNES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-likes"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jADpqW/"
# =====================================================================

async def soumettre_tache():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(locale="fr-FR", timezone_id="Europe/Paris")
        page = await context.new_page()
        
        try:
            print(f"Connexion à : {URL_DU_SITE}...")
            await page.goto(URL_DU_SITE)
            # Attend que le réseau soit calme
            await page.wait_for_load_state("networkidle")
            # Petite pause de sécurité pour le chargement des éléments visuels
            await page.wait_for_timeout(3000)
            
            # 1. Trouve la case en ignorant la faute de frappe (cherche juste "Paste your")
            print("Ciblage de la case TikTok...")
            champ = page.locator("input[placeholder*='Paste your'], input[placeholder*='TikTok']").first
            await champ.click()
            await champ.fill(LIEN_A_COLLER)
            
            # 2. Clic sur le bouton exact "Get Now" (insensible aux majuscules/minuscules)
            print("Clic sur le bouton 'Get Now'...")
            bouton = page.get_by_role("button", name=r"get now", exact=False).first
            if not await bouton.count():
                bouton = page.locator("text=/Get Now/i").first
                
            await bouton.click(force=True)
            
            print("Tâche exécutée avec succès !")
            # Laisse le temps au site de traiter la demande
            await page.wait_for_timeout(5000)
            
        except Exception as e:
            print(f"Erreur : {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(soumettre_tache())
