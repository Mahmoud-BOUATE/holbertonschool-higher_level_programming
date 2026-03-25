def generate_invitations(template, attendees):
    # Vérifier que template est une string
    if not isinstance(template, str):
        print(f"Erreur: template doit être un texte (string), reçu {type(template)}")
        return

    # Vérifier que attendees est une liste
    if not isinstance(attendees, list):
        print(f"Erreur: attendees doit être une liste, reçu {type(attendees)}")
        return

    # Vérifier chaque élément de la liste
    for person in attendees:
        if not isinstance(person, dict):
            print("Erreur: chaque élément de la liste doit être un dictionnaire")
            return

    # Vérifier si le template est vide
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Vérifier si la liste d'invités est vide
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Parcourir chaque invité
    for idx, person in enumerate(attendees, start=1):
        invitation = template  # copier le template

        # Remplacer les placeholders avec .get() pour gérer les absences
        name = person.get("name", "N/A") or "N/A"
        event_title = person.get("event_title", "N/A") or "N/A"
        event_date = person.get("event_date", "N/A") or "N/A"
        event_location = person.get("event_location", "N/A") or "N/A"

        invitation = invitation.replace("{name}", name)
        invitation = invitation.replace("{event_title}", event_title)
        invitation = invitation.replace("{event_date}", event_date)
        invitation = invitation.replace("{event_location}", event_location)

        # Créer le fichier de sortie
        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, "w") as f:
                f.write(invitation)
            print(f"{output_filename} créé avec succès.")
        except Exception as e:
            print(f"Erreur lors de l'écriture du fichier {output_filename}: {e}")

