chaine = "I can see that you're giving up It should not mean that much to me"

dic = {}
for c in chaine:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1
print(dic)


recette = {
    "nom": "Tartine Fraise-Moutarde",
    "instructions": [
        "Laver et couper les fraises.",
        "Étaler le beurre sur une tartine.",
        "Ajouter les fraises.",
    ],
    "ingredients": {"Fraise": 5, "Beurre": "100g"},
}

recette["note"] = 18

recette["ingredients"]["moutarde"] = "5g"
recette["ingredients"]["Beurre"] = "200g"

recette["instructions"].append("Assaisonner légèrement avec la moutarde.")

for k, v in recette["ingredients"].items():
    print(f"ingrédient {k}, quantité {v}")
