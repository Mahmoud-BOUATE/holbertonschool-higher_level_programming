from task_00_intro import generate_invitations

# Lire le template depuis le fichier
with open("template.txt", "r") as f:
    template_content = f.read()

# Liste d'invités
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Appeler la fonction
generate_invitations(template_content, attendees)