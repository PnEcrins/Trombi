# TROMBI

Trombi est une application permettant de générer un trombinoscope à partir d'un annuaire LDAP.
Il permet aussi d'afficher l'agenda de chaque personne du trombinoscope grâce à un agenda compatible Ical/CALDAV.

## Technologies

Backend : Flask
Frontend : VueJS

## Installation

- Télécharger le zip du dépot dans le /home de votre utilisateur. Dézippé le et renommé le "trombi"
- Désampler les fichier de configuration et les éditer
  ::

      cp settings.sample.ini settings.ini
      cp ldaptrombipy/config.sample.py ldaptrombipy/config.py
      cp ldaptrombipy/static/app/public/config.sample.json cp ldaptrombipy/static/app/public/config.json

- Lancer le script d'installation `install_app.sh`
- L'API est lancée sur le port 5006 par défault

## Configuration Apache

sudo a2enmod proxy
sudo a2enmod proxy_http

Voir les fichiers exemples: conf_apache.template
