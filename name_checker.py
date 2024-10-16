
#
# small helper that uses spacy to identify personal information in first column of an Excel file
#
from openpyxl import load_workbook
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")


wb = load_workbook(filename='allcomp.xlsx', read_only=True, keep_vba=False)
ws = wb.worksheets[0]

apps_with_names = []

for i, row in enumerate(ws):
    if i == 0:
        continue
    
    app_name = row[0].value
    info = "NO INFO"
    doc = nlp(app_name)
    if doc.ents is not None and len(doc.ents) > 0:
        # info = ", ".join([f"{ent.text} -> {ent.label_}" for ent in doc.ents]) # all entities
        persons = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
        if persons is not None and len(persons) > 0:
            info = ", ".join(persons) # persons
            apps_with_names.append(f"{i} - {app_name}: {info}")

    print(f"App {i:6}: '{row[0].value}' || {info}")

    if i > 1000:
        break

for a in apps_with_names:
    print(a)