import os
import datetime
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class BAMBDTDownloader:
    def __init__(self, download_dir=None, headless=True):
        self.download_dir = download_dir or os.path.join(os.getcwd(), "bdt_files")
        os.makedirs(self.download_dir, exist_ok=True)
        self.headless = headless
        self.driver = self._setup_driver()

    def _setup_driver(self):
        options = Options()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def download_latest_csv(self):
        url = "https://www.bkam.ma/Marches/Principaux-indicateurs/Marche-obligataire/Marche-des-bons-de-tresor/Marche-secondaire/Taux-de-reference-des-bons-du-tresor"
        print(f"Ouverture de la page BAM : {url}")
        self.driver.get(url)

        try:
            wait = WebDriverWait(self.driver, 15)
            # Trouver le lien CSV, ici on prend l'exemple d'un lien avec une classe CSS "link-CSV"
            link = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "link-CSV")))
            href = link.get_attribute("href")
            file_url = href if href.startswith("http") else "https://www.bkam.ma" + href
            print(f"Lien CSV trouvé : {file_url}")

            today = datetime.datetime.today().strftime("%Y-%m-%d")
            filename = f"bdt_{today}.csv"
            filepath = os.path.join(self.download_dir, filename)

            # Télécharger le fichier
            response = requests.get(file_url)
            if response.status_code == 200:
                with open(filepath, "wb") as f:
                    f.write(response.content)
                print(f"Fichier téléchargé avec succès : {filepath}")
                return filepath
            else:
                print(f"Erreur HTTP {response.status_code} lors du téléchargement.")
                return None
        except Exception as e:
            print(f"Erreur lors du téléchargement : {e}")
            return None
        finally:
            self.driver.quit()

if __name__ == "__main__":
    downloader = BAMBDTDownloader()
    downloader.download_latest_csv()
