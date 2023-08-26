# projet-3-diginamic

Concevoir un système d’intelligence artificielle et d’apprentissage automatique

## Contexte

Nous sommes mandatés par la socièté **Beer Recipes Enthusiasts Workshop**, qui nous a demandé de développer de nouvelles recettes de bières via Machine Learning. Nous devons concevoir et fournir une **interface web fonctionnelle, facile d'utilisation qui prédira l'amertume et la teneur en alcool d'une recette donnée** dans un délai d'une semaine, avec une **livraison intermédiaire relative à l'analyse exploratoire des données**.

L'équipe de BREW n'ayant pas d'informaticien, nous devons utiliser Python pour le développement car c'est le seul langage de programmation connu par le responsable RH. Cependant, lors de nos échanges sur le cahier des charges, nous avons remarqué que le domaine du Machine Learning lui était plutôt inconnu : il nous faudra être clair dans nos développement, commentaires et échanges.

Nous utiliserons le format .ipynb pour toute la partie de développement hors application Web, pour faciliter la compréhension du code pour notre client.

## Données :

Les données sont disponibles à l'adresse suivante : https://www.kaggle.com/datasets/jtrofe/beer-recipes

Ce jeu contient 73 861 recettes, et 23 observables qui vont du nom de la bière en question jusqu'au type de bière en passant par le taux d'alcool, l'echelle de teinte ou la méthode de brassage.

Elles proviennent d'individus qui partagent leurs recettes de bières artisanales, voir brassées à la maison.

La documentation fournie est peu explicite, nous la préciserons par des échanges avec le maître brasseur.

Nous effectuerons des analyses exploratoires sur ce jeu de données, le traiterons en conséquence; entraînerons, optimiserons et évaluerons des modèles de Machine Learning de manière à fournir la solution la plus précise et fiable possible.


## Documentation

**BeerID**: Un identifiant unique pour chaque bière enregistrée.

**Name**: Le nom de la bière.

**URL**: L'URL associée à la bière, peut-être un lien vers plus d'informations ou une source.

**Style**: Le style de la bière, c'est-à-dire la catégorie ou le type auquel la bière appartient (par exemple : Pale Ale, Stout, IPA, etc.).

**StyleID**: L'identifiant unique du style de bière.

**Size(L)**: La taille du brassin en litres.

**OG** (Original Gravity): La densité initiale du moût avant la fermentation, généralement mesurée en points de densité.

**FG** (Final Gravity): La densité finale du moût après la fermentation, généralement mesurée en points de densité.

**ABV** (Alcohol by Volume): Le pourcentage d'alcool par volume dans la bière, que l'on cherche à prédire.

**IBU** (International Bitterness Units): Une mesure de l'amertume de la bière, influencée par la quantité de houblon utilisée, que l'on cherche à prédire

**Color**: La couleur de la bière, généralement mesurée en unités de couleur.

**BoilSize**: La quantité d'eau nécessaire pour l'ébullition du moût.

**BoilTime**: La durée de l'ébullition du moût en minutes.

**BoilGravity**: La densité du moût au début de l'ébullition.

**Efficiency**: L'efficacité du processus de brassage.

**MashThickness**: L'épaisseur du mélange d'empâtage.

**SugarScale**: L'échelle de mesure utilisée pour le sucre.

**BrewMethod**: La méthode de brassage utilisée.

**PitchRate**: Le taux d'ensemencement, c'est-à-dire la quantité de levure ajoutée par rapport au volume du moût.

**PrimaryTemp**: La température de fermentation primaire.

**PrimingMethod**: La méthode utilisée pour la refermentation en bouteille.

**PrimingAmount**: La quantité de sucre ajoutée pour la refermentation en bouteille.

**UserId**: L'identifiant de l'utilisateur qui a soumis la recette de la bière.

