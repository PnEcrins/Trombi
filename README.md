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

- OS : Debian 10
- Backend : Python / Flask
- Frontend : VueJS

## Installation

- Télécharger le zip de la version souhaitée (X.Y.Z) dans le répertoire `/home` de votre utilisateur. Dézippez le et renommez le "trombi"

  ```
  cd /home/`whoami`
  wget https://github.com/PnEcrins/Trombi/archive/X.Y.Z.zip
  unzip X.Y.Z.zip
  mv Trombi-X.Y.Z trombi
  rm X.Y.Z.zip
  sudo apt-get install -y python3-pip

  ```

- Désampler les fichiers de configuration et les modifier

  ```
  cp settings.sample.ini settings.ini
  cp ldaptrombipy/config.sample.py ldaptrombipy/config.py
  cp ldaptrombipy/static/app/dist/config.sample.json ldaptrombipy/static/app/dist/config.json
  ```

  Le fichier `ldaptrombipy/config.py` contient la connexion au LDAP et au Caldav. Il permet aussi d'exclure des utilisateurs ou des groupes d'utilisateurs.
  Le fichier `ldaptrombipy/static/app/public/config.json` est utilisé par le frontend pour connaitre l'API et définir si les utilisateurs peuvent ajouter ou modifier eux-mêmes les photos

- Lancer le script d'installation `install_app.sh`
- Réaliser une configuration Apache : Créer un fichier `/etc/apache2/sites-available/trombi.conf` et copier le contenu du fichier https://github.com/PnEcrins/Trombi/blob/main/cong_apache.template (en adaptant les chemins). Activer la configuration et redémarrer Apache 
```
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo a2ensite trombi
sudo apachectl restart
```

## Fonctionnement

- Le trombinoscope n'affiche que les personnes ayant un nom et un prénom dans l'AD

## Développement

### Backend


- Créer un fichier .env à la dans le répertoire `ldaptrombipy` et y mettre les variables suivantes :

 ```
FLASK_RUN_PORT=5004
FLASK_ENV=development
 ```
- Activer le virtualenv `source venv/bin/activate`

Lancer le backend : `flask run`
 
 ### Frontend

Le frontend utilise `vue-cli` comme structure d'application, ainsi que ses outils de build.

Depuis `ldaptrombipy/static`:
- Installer nvm : https://github.com/nvm-sh/nvm
- Installer node et npm : `nvm install`
- Installer les dépendances : `npm install`

Lancer le frontend `npm run serve`

Voir le fichier d'exemple : `conf_apache.template`

## Licence

- OpenSource - GPLv3
- Auteur : Théo Lechémia / Parc national des Écrins / 2021

[![Logo PNE](http://geonature.fr/img/logo-pne.jpg)](https://www.ecrins-parcnational.fr)
