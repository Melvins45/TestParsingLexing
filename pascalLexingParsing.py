import tkinter as tk
from tkinter import scrolledtext, messagebox
import re

# Mots réservés Pascal
mots_reserves_pascal = {
    "and", "array", "begin", "case", "char", "const", "div", "do", "downto",
    "else", "end", "file", "for", "function", "goto", "if", "in", "integer",
    "label", "mod", "nil", "not", "of", "or", "packed", "procedure", "program",
    "record", "repeat", "set", "then", "to", "type", "until", "var", "while",
    "with", "boolean", "real", "string"
}

types_pascal = {"integer", "real", "char", "boolean", "string"}

# Analyseur lexical
def analyser_lexical(code):
    tokens = []
    lignes = code.splitlines()
    for ligne in lignes:
        ligne = ligne.strip()
        if not ligne:
            continue
        mots = re.findall(r'\w+|:=|;|:|\.', ligne)
        for mot in mots:
            if mot.lower() in mots_reserves_pascal:
                tokens.append((mot, "mot réservé"))
            elif mot == ":=":
                tokens.append((mot, "opérateur d'affectation"))
            elif mot == ";":
                tokens.append((mot, "séparateur"))
            elif mot == ":":
                tokens.append((mot, "déclaration"))
            elif mot == ".":
                tokens.append((mot, "fin de programme"))
            else:
                tokens.append((mot, "identifiant"))
    return tokens

# Vérification syntaxique
def verifier_structure(tokens):
    erreurs = []
    has_begin = any(tok[0].lower() == "begin" for tok in tokens)
    has_end = any(tok[0].lower() == "end" for tok in tokens)

    if not has_begin:
        erreurs.append("Erreur : bloc 'begin' manquant.")
    if not has_end:
        erreurs.append("Erreur : bloc 'end' manquant.")

    return erreurs

# Vérification des types
def verifier_declarations(code):
    erreurs = []
    lignes = code.splitlines()
    for ligne in lignes:
        if ligne.strip().startswith("var"):
            match = re.search(r'var\s+(\w+)\s*:\s*(\w+)', ligne)
            if match:
                nom_var, type_var = match.groups()
                if type_var.lower() not in types_pascal:
                    erreurs.append(f"Type inconnu pour la variable '{nom_var}': '{type_var}'")
            else:
                erreurs.append(f"Déclaration incorrecte : {ligne}")
    return erreurs

# Fonction principale d’analyse
def analyser_code():
    code = text_editor.get("1.0", tk.END)
    tokens = analyser_lexical(code)
    erreurs = verifier_structure(tokens) + verifier_declarations(code)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "🔍 Tokens reconnus :\n")
    for tok in tokens:
        output_box.insert(tk.END, f"{tok[0]:<10} → {tok[1]}\n")

    if erreurs:
        output_box.insert(tk.END, "\n🚨 Erreurs détectées :\n")
        for err in erreurs:
            output_box.insert(tk.END, f"- {err}\n")
    else:
        output_box.insert(tk.END, "\n✅ Aucune erreur détectée.\n")

# Interface graphique
fenetre = tk.Tk()
fenetre.title("Mini Compilateur Pascal")
fenetre.geometry("800x600")

# Éditeur de texte
label_code = tk.Label(fenetre, text="Éditeur de code Pascal :")
label_code.pack(anchor="w", padx=10, pady=5)

text_editor = scrolledtext.ScrolledText(fenetre, width=100, height=20, font=("Courier", 12))
text_editor.pack(padx=10, pady=5)

# Bouton d’analyse
btn_analyser = tk.Button(fenetre, text="Analyser le code", command=analyser_code, bg="#4CAF50", fg="white")
btn_analyser.pack(pady=10)

# Zone de sortie
label_output = tk.Label(fenetre, text="Résultats de l’analyse :")
label_output.pack(anchor="w", padx=10)

output_box = scrolledtext.ScrolledText(fenetre, width=100, height=15, font=("Courier", 11), bg="#f0f0f0")
output_box.pack(padx=10, pady=5)

fenetre.mainloop()
