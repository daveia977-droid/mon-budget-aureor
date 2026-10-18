# Mon Quotidien

Application web mobile-first de gestion du quotidien : dépenses, budget mensuel, factures, tâches et graphiques par catégorie.

## Utiliser l'application

- En local : ouvrir `index.html` dans un navigateur.
- En ligne : activer GitHub Pages (voir ci-dessous).

## Activer GitHub Pages

1. Aller dans **Settings > Pages** du dépôt.
2. Section **Build and deployment** : choisir **Deploy from a branch**.
3. Branch : `main`, dossier : `/ (root)`.
4. Cliquer **Save** et attendre 1-2 minutes.
5. Le site sera disponible sur : `https://daveia977-droid.github.io/mon-budget-aureor/`

## Installer sur téléphone (PWA-like)

1. Ouvrir l'URL du site dans Safari (iOS) ou Chrome (Android).
2. Menu Partager > **Sur l'écran d'accueil**.
3. L'app s'ouvrira en plein écran comme une application.

## Données

- Stockage local du navigateur (localStorage), aucune API, 100% gratuit.
- Export/import de sauvegarde JSON intégré (onglet Sauvegarde).
- Ne pas stocker d'informations bancaires sensibles.

## Fonctionnalités

- Dépenses avec validation, 7 catégories, historique par mois
- Budget mensuel avec barre de progression (vert / orange / rouge)
- Factures : échéances, détection des retards, statut payée
- Tâches avec compteur
- Graphique donut par catégorie + tendance sur 6 mois (SVG natif, aucune dépendance)
