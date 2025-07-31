from setuptools import setup

setup(
    name="bam-bdt-scraper",
    version="0.1",
    py_modules=["bam_bdt_downloader"],  # remplace par le nom de ton fichier .py sans l'extension
    install_requires=[
        "selenium",
    ],
    author="Hiba Hib",
    description="Un scraper pour BAM BDT",
    url="https://github.com/Hiba-Hib231/bam-bdt-scraper",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
