from setuptools import setup

setup(
    name="bam-bdt-scraper",
    version="0.1",
    py_modules=["bam_bdt_downloader"],  # nom de ton fichier Python sans .py
    install_requires=[
        "selenium",
        "webdriver_manager",
    ],
    author="Hiba Hib",
    description="Un scraper pour BAM BDT",
    url="https://github.com/Hiba-Hib231/bam-bdt-scraper",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
