# TROMBI

TROMBI est une application web permettant de générer un trombinoscope à partir d'un annuaire LDAP.
Elle permet aussi d'afficher l'agenda de chaque personne du trombinoscope en se connectant à un agenda compatible iCalendar/CALDAV.

Inspiré de l'outil https://github.com/noelmartinon/webagenda-viewer.

## Fonctionnalités

- Liste des utilisateurs présents dans l'annuaire
- Regroupement des utilisateurs par Service (Department) de l'annuaire
- Affichage d'une fiche par utilisateur avec sa photo, son nom, sa description, son email, ses numéros de téléphone et son agenda (si son email est renseigné dans l'annuaire LDAP)
- Possibilité d'ajouter ou modifier les photos des utilisateurs (stockés sur le serveur applicatif)

![Screenshot HOME](https://github.com/PnEcrins/Trombi/blob/main/docs/trombi-home.jpg)

![Screenshot FICHE](https://github.com/PnEcrins/Trombi/blob/main/docs/trombi-fiche.jpg)

## Technologies

- Backend : Python / Flask
- Frontend : VueJS

## Installation

- Télécharger le zip du dépôt dans le répertoire `/home` de votre utilisateur. Dézippez le et renommez le "trombi"
- Désampler les fichiers de configuration et les modifier
  ```
  cp settings.sample.ini settings.ini
  cp ldaptrombipy/config.sample.py ldaptrombipy/config.py
  cp ldaptrombipy/static/app/public/config.sample.json cp ldaptrombipy/static/app/public/config.json
  ```

  Le fichier `ldaptrombipy/config.py` contient la connexion au LDAP et au Caldav. Il permet aussi d'exclure des utilisateurs ou des groupes d'utilisateurs.
  Le fichier `ldaptrombipy/static/app/public/config.json` est utilisé par le frontend pour connaitre l'API et définir si les utilisateurs peuvent ajouter ou modifier eux-mêmes les photos

- Lancer le script d'installation `install_app.sh`
- L'API est lancée sur le port 5006 par défault

## Configuration Apache

```
sudo a2enmod proxy
sudo a2enmod proxy_http
```

Voir le fichier d'exemple : `conf_apache.template`

## Licence

* OpenSource - GPLv3
* Auteur : Théo Lechémia / Parc national des Écrins / 2021

[![Logo PNE](http://geonature.fr/img/logo-pne.jpg)](https://www.ecrins-parcnational.fr)
