#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convertit un fichier CSV en fichier JSON nommé data.json
    Retourne True si réussi, False en cas d'erreur
    """
    try:
        """Lire le CSV et transformer chaque ligne en dictionnaire"""
        with open(csv_filename, "r") as f_csv:
            reader = csv.DictReader(f_csv)
            data_list = list(reader)

        """Écrire les données en JSON dans data.json"""
        with open("data.json", "w") as f_json:
            json.dump(data_list, f_json, indent=4)

        return True

    except Exception:
        """Si le fichier n'existe pas ou une erreur se produit"""
        return False
