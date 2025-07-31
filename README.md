# bam-bdt-scraper
Lib Python pour télécharger automatiquement les taux BAM BDT
# bam-bdt-scraper

**Librairie Python pour télécharger automatiquement les taux moyens pondérés publiés par Bank Al-Maghrib (BAM) – Marché des bons du Trésor (BDT)**.

---

## 📥 Fonctionnalités

- Accès au site officiel de la BAM
- Téléchargement automatique du fichier CSV contenant les taux
- Enregistrement local pour analyse ultérieure (courbe ZC, valorisation de portefeuille...)

---

## 🛠️ Installation

```bash
pip install selenium requests webdriver-manager
from bam_bdt_downloader import setup_driver, download_csv_file

driver = setup_driver()
download_csv_file(driver, "./bdt_files")
driver.quit()
