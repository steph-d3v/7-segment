# Afficheur numérique à sept segments

Défi relevé sur le Discord de [Docstring][docstring].

L'enjeu consistait à afficher l'heure dans le Terminal avec des chiffres "à sept segments" :

```
     a            Exemples:
     ▼ 
    ####          #  ####     ####  ####        #  #     ####  ####
f ▶ #  # ◀ b      #     #  #     #  #           #  #  #  #  #  #  #
    #### ◀ g      #     #     ####  ####   ou   ####     #  #  ####
e ▶ #  # ◀ c      #     #  #  #     #  #           #  #  #  #  #  #
    ####          #     #     ####  ####           #     ####  ####
     ▲
     d
```

Je souhaitais proposer une implémentation originale avec un code astucieux et concis.

### Exécution du script

```
python3 7-segment.py
```

<img src="assets/7-segment.png" width="600px" height="256px" alt="Démo">


[docstring]: https://www.docstring.fr