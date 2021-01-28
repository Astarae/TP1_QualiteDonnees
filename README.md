# TP1 - Qualité des données

## Sujet du TP
Comparer deux jeux de données de climat pour déterminer la capitale européenne dont les données de température sont fournies dans le fichier Climat.xlsx
On se servira du fichier Savukoskikirkonkyla.xlsx issu de l’open data pour servir de référence.

Objectifs :
• Mettre en oeuvre un environnement de traitement graphique de données issues de sources plus ou moins fiables.
• Corriger un jeu de données mal formé
• proposer un candidat potentiel pour l’origine des données.

Déroulement :
• Pour l’ échanllon SI, calculez :
    • moyenne par mois
    • écart type par mois
    • min /max par mois et par année
• uliser par Python Scipy pour les pares mathémaques.
• tracer les courbes de chaque mois avec une bibliothèque graphique python Matplotlib, 12 vues mensuelles 
• Assembler les courbes sur un seul graphique (J1 -> J365) : vue annuelle
• Présenter la valeur lue en parcourant la courbe à l'aide du pointeur,
• Présenter les valeurs précédentes par mois glissant de 30 jours centré sur la valeur lue
• Recommencez avec le jeu SI-erreur après avoir corrigé les valeurs en erreur. Précisez vos méthodes.
• Les données corrigées sont elles proches des valeurs sans erreur ?
• A partir de données opendata du second fichier, retrouver le type de climat
    • reprendre les données typiques de la localisaon proche fournies en complément , comparer les écarts. 
    • Qu'en concluez vous ?
    • De quelle la capitale européenne avez vous eu les données.

Outils : à utiliser Python + matplotlib, Jupyter éventuellement. Pas de R ni d’autre langage autorisés Evaluation:
Démonstration des solutions techniques et argumentation sur les méthodes utilisées

-----------------

## Explications de notre méthode pour corriger les valeurs du jeu SI-erreur

Dans la fonction __read_climat_file()__ du fichier mainSI-erreur.py, nous avons décidé de corriger les valeurs de la façon suivante : 

- Lire notre fichier en créant un dataframe.
- Parcourir notre fichier.
- Identifier si la valeur est bien de type String.
- Faire la moyenne de la valeur supérieur et inférieur de la valeur sur laquelle nous allons nous arrêter car c'est un type String.
- Remplacer cette dites valeur par la moyenne précédemment calculée.
- Ajoutée valeur à une tableau.
- Dans ce tableau nous allons avoir toutes les données de notre fichier.
<!-- - Nous allons donc parcourir ce tableau et calculer la moyenne et l'écart-type de chaque mois.
- Pour déterminer si celle-ci est supérieure à la moyenne et l'écart-typa additionnées.
- Nous affectons à cette valeur, la moyenne précédemment calculée. -->

Nous avons décidé de mettre une moyenne à la place des valeurs erronées pour avoir des graphiques cohérents.

-----------------

## Comparaison des données corrigées et des valeurs sans erreur du fichier

Nous avons constaté que les données corrigées sont proches des valeurs sans erreurs, par exemple pour les mois de mars et juin :

Moyenne : 
- MARS : 
    - Valeur sans erreur : 1.1935483870967742
    - Valeur corrigée : 1.2419354838709677

- JUIN : 
    - Valeur sans erreur : 17.033333333333335
    - Valeur corrigée : 17.0

-----------------
## Analyse des données opendata du second fichier


-----------------

TP réalisé par __Amélie LUNEAU__ et __Pablo COLSON__.