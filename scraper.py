import requests
from bs4 import BeautifulSoup
import datetime

def run_scraper():
    url = "https://datascientest.com/blog-data-ia-actualites" # Remplacez par l'URL à scraper
    try:
        response = requests.get(url)
        response.raise_for_status() # Lève une exception pour les codes d'état HTTP d'erreur

        soup = BeautifulSoup(response.text, 'html.parser')

        # Exemple : récupérer le titre de la page
        title = soup.find('title').get_text() if soup.find('title') else "Titre non trouvé"
        print(f"[{datetime.datetime.now()}] Scraper executed. Page title: {title}")

        # Ajoutez ici votre logique de scraping spécifique
        # Par exemple, enregistrer les données dans un fichier, les envoyer par e-mail, etc.

    except Exception as e:
        print(f"Error during scraping: {e}")

if __name__ == "__main__":
    run_scraper()
