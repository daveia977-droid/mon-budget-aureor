# Mon Budget AŪREOR

Application web mobile de gestion de budget professionnel : dépenses, charges/factures, clients, projets et bilan. 100% locale, aucune API, aucune dépendance (fichier unique `index.html`, police Lobster via Google Fonts).

**🌐 Application en ligne :** https://daveia977-droid.github.io/mon-budget-aureor/

## Structure du dépôt

- `index.html` — l'application complète (HTML + CSS + JS dans un seul fichier)
- `apple-touch-icon.PNG` — icône pour l'installation sur écran d'accueil iPhone
- `README.md` — ce fichier

## Fonctionnalités

- **Espace local sécurisé** : code PIN 4 à 8 chiffres, écran de verrouillage, verrouillage automatique après 15 min d'inactivité ou au retour d'arrière-plan
- **5 onglets** : Accueil, Dépenses, Clients, Projets, Bilan
- **Dépenses** : catégories, historique, budget mensuel avec barre de progression
- **Charges/Factures** : échéances, détection des retards, export PNG individuel
- **Clients** : tableau Client / Dû / Encaissé / Reste / Statut, versements partiels mémorisés, récapitulatif PNG par client
- **Projets** : enveloppe budgétaire, dépenses et activités liées, % consommé, alerte
- **Bilan** : période Mois / 6 mois / 12 mois, CA encaissé, charges, bénéfice net, objectif de marge, graphique SVG, rapport PNG exportable
- **Sauvegarde JSON** : export (jamais le code PIN) et import avec vérification, limite 2 Mo

## Installer sur téléphone (iPhone / Android)

1. Ouvrir l'URL dans Safari (iOS) ou Chrome (Android).
2. Menu Partager > **Sur l'écran d'accueil**.
3. L'app s'ouvre en plein écran comme une application native.

## Données et sécurité

- Stockage **local** au navigateur (clé `aureor_local_space_v3`) : les données ne quittent jamais l'appareil.
- Le code PIN est un verrou d'accès, **pas un chiffrement** : ne pas stocker d'informations bancaires sensibles.
- **Exporter régulièrement la sauvegarde JSON** (profil > Exporter) : vider le cache du navigateur effacerait les données.

## Maintenance

- L'application est déployée automatiquement par GitHub Pages depuis la branche `main`.
- Ne pas modifier `index.html` directement sur `main` : passer par une branche + pull request.
- Ne jamais résoudre les conflits de `index.html` à la main dans l'éditeur web : demander une vérification après résolution (un mauvais découpage du bloc `<script>` peut bloquer toute l'application).
