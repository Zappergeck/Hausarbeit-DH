import xml.etree.ElementTree as ET
import os
from collections import defaultdict

# Datei einlesen
def split_xml_file(file_path, output_dir):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    count_dict = defaultdict(int)  # Dictionary zur Speicherung der Zähler pro Person
    
    for text_elem in root.findall("text"):
        person = text_elem.get("person", "Unknown").replace(" ", "_")
        rohtext_elem = text_elem.find("rohtext")
        
        if rohtext_elem is not None:
            content = rohtext_elem.text.strip() if rohtext_elem.text else ""
            
            count_dict[person] += 1  # Zähler für diese Person erhöhen
            filename = f"{person}_{count_dict[person]}.txt"
            
            with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as file:
                file.write(content)
            
            # Lösche <text> Element nach Speicherung
            root.remove(text_elem)
    
    # Aktualisierte XML-Datei ohne die verarbeiteten Texte speichern
    new_file_path = os.path.join(output_dir, "remaining.xml")
    tree.write(new_file_path, encoding="utf-8", xml_declaration=True)

# aufruf
split_xml_file("Ich-Bin-Ein-Dateipfad-Zu-Einer-XML-Datei-:D", "Ich-Bin-Ein-Dateipfad-Zu-Einem-Ordner-Indem-Die-Unterteilten-Reden-Gespeichert-Werden-Sollen")