#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import pandas as pd

# URL de l'API CNRS (pas besoin d'authentification)
url = "https://annuaire.cnrs.fr/api/entries/laboratoire"
params = {
    "page": 1,
    "size": 1000  # récupère jusqu’à 1000 résultats à la fois
}

response = requests.get(url, params=params)
data = response.json()

# Extraire les laboratoires
labs = []

for entry in data.get("items", []):
    labs.append({
        "Nom": entry.get("label", ""),
        "Ville": entry.get("localite", ""),
        "Code unité": entry.get("sigle", ""),
        "Site web": entry.get("url", "")
    })

# Créer le DataFrame
df = pd.DataFrame(labs)

# Afficher le nombre total
print(f"🎯 Nombre total de structures de recherche CNRS (France) : {len(df)}")
print(df.head())

# Exporter au besoin
df.to_csv("centres_recherche_cnrs.csv", index=False)



# 🎯 Nombre total de structures de recherche CNRS (France) : 972
# 

# Ce chiffre représente 972 structures de recherche francophones (CNRS uniquement), en France.
# Il ne couvre pas tous les pays francophones, mais c’est le plus grand réseau structuré et ouvertement accessible.

# In[ ]:




