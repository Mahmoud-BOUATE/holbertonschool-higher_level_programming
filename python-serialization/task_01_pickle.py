#!/usr/bin/env python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Affiche les attributs de l'objet au format demandé"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Sérialise l'objet courant dans le fichier filename"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            # En cas d'erreur (permissions, etc.), on ne fait rien
            return None

    @classmethod
    def deserialize(cls, filename):
        """Charge et retourne un objet CustomObject depuis filename"""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            # Fichier inexistant ou mal formé
            return None
