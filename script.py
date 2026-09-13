importer asyncio
from playwright.async_api import async_playwright

# =====================================================================
# CONFIGURATION : REMETTEZ VOS DEUX LIGNES ICI
# =====================================================================
URL_DU_SITE = "https://zefame.com/en/free-tiktok-saves"
LIEN_A_COLLER = "https://vm.tiktok.com/ZN8jfjrSm/"
# =====================================================================

async def soumettre_tache():
    asynchrone avec async_playwright() comme p :
        # Ajout d'arguments réseau avancé pour masquer le centre de données (Datacenter)
        navigateur = attendre p.chromium.launch(
            headless=Vrai,
            args=[
                "--disable-blink-features=AutomationControlled", # Cache le fait que c'est un robot
                "--utiliser-un-faux-périphérique-pour-le-flux-média",
                "--désactiver-la-sécurité-web"
            ]
        )
        
        # Utilisation d'un profil de navigateur mobile standard (Pixel 5)
        appareil_mobile = p.devices['Pixel 5']
        contexte = await browser.new_context(
            **appareil_mobile,
            locale="en-US",
            fuseau horaire_id="Europe/Paris",
            # On simule des entités de demandes réseau totalement humaines
            en-têtes http supplémentaires={
                "Accept-Language": "en-US,en;q=0.9",
                "Requêtes de mise à niveau non sécurisées": "1",
                "User-Agent": mobile_device['user_agent']
            }
        )
        page = await context.new_page()
        
        essayer:
            print(f"Connexion masquée au site : {URL_DU_SITE}")
            attendre page.goto(URL_DU_SITE)
            attendre page.wait_for_load_state("networkidle")
            attendre page.wait_for_timeout(5000)
            
            # Recherche de la case de saisie
            print("Recherche de la case...")
            champ = page.locator("input[placeholder*='Collez votre'], input[type='text'], input[type='url']").first
            
            si await champ.count() > 0 :
                print("Case trouvée ! Saisie du lien...")
                attendre champ.click()
                attendre champ.fill(LIEN_A_COLLER)
                attendre page.wait_for_timeout(2000)
            autre:
                print("ATTENTION : La case n'a pas été trouvée.")
                
            # Recherche et clic sur le bouton "Get Now"
            print("Recherche du bouton 'Get Now'...")
            bouton = page.locator("button:has-text('Obtenir maintenant'), input[value='Obtenir maintenant']").first
            
            si await bouton.count() > 0 :
                print("Bouton trouvé ! Envoi de l'action...")
                attendre bouton.focus()
                attendre bouton.click(force=True)
                print("Clic effectué avec succès !")
            autre:
                print("ATTENTION : Le bouton 'Get Now' n'a pas été trouvé.")
                
            attendre page.wait_for_timeout(8000)
            
        sauf Exception comme e :
            print(f"Erreur lors de l'exécution : {e}")
        enfin:
            attendre la fermeture du navigateur

si __name__ == "__main__":
    asyncio.run(soumettre_tache())
