#!/usr/bin/python3
def ma_fonction(f):
    return f()

def dire_bonjour():
    return "Bonjour !"

print(ma_fonction(dire_bonjour))  # On passe la fonction comme objet
