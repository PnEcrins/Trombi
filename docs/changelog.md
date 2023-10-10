# Changelog

1.2.0 (2023-10-10)
------------------

**✨ Améliorations**

* Améliorations graphiques et ergonomiques
* Passage des filtres du LDAP en paramètres

**🐛 Corrections**

* Correction des évènements récurrents (#3)
* Suppression des images sous copyright (#4)

**⚠️ Notes de version**

* Il est nécessaire d'ajouter le paramètre `SEARCH_FILTERS` qui correspond aux filtres appliquées par défaut à chaque requête au LDAP.

1.1.1 (2021-07-30)
------------------

**✨ Fonctionnalités**

* Support de tous les formats d'image et plus uniquement du ``.jpg``

**🐛 Corrections**

* Correction du script ``install_app.sh`` (à tester)

1.1.0 (2021-07-23)
------------------

**✨ Fonctionnalités**

* Modification des icônes des boutons
* Nom des utilisateurs cliquable
* Complément des infos sur les évenements de l'agenda
* Correction du script ``install_app.sh``

1.0.0 (2021-07-21)
------------------

Première version stable et fonctionnelle.

**✨ Fonctionnalités**

* Connexion à un annuaire LDAP
* Connexion à un agenda iCalendar/CALDAV
* Liste des utilisateurs présents dans l'annuaire
* Regroupement des utilisateurs par Service (Department) de l'annuaire
* Affichage d'une fiche par utilisateur avec sa photo, son nom, sa fonction, sa description, son email, ses numéros de téléphone et son agenda (si son email est renseigné dans l'annuaire LDAP)
* Possibilité d'ajouter ou modifier les photos des utilisateurs (stockés sur le serveur applicatif)
