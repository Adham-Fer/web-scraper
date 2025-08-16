# Wiki Article Scraper (Random Walk)

Ce script Python permet de parcourir des articles Wikipédia de manière aléatoire.  
En partant d’un article initial, il extrait son titre puis choisit au hasard un lien interne pour continuer la navigation, et ainsi de suite.

## Fonctionnalités

- Récupère le contenu d’un article Wikipédia.
- Affiche le titre de l’article courant.
- Sélectionne un lien interne au hasard et continue la navigation récursive.
- Explore ainsi Wikipédia en "marche aléatoire".

## Prérequis

Avant d'exécuter le script, installe les dépendances suivantes :

```bash
pip install requests beautifulsoup4
