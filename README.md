# TROMBI

Trombi est une application permettant de générer un trombinoscope à partir d'un annuaire LDAP.
Il permet aussi d'afficher l'agenda de chaque personne du trombinoscope grâce à un agenda compatible Ical/CALDAV.

## Technologies

Backend : Flask
Frontend : VueJS

## Installation

- Télécharger le zip du dépot dans le /home de votre utilisateur. Dézippé le et renommé le "trombi"
- Lancer le script d'installation `install_app.sh`
- L'API est lancée sur le port 5006 par défault

## Configuration Apache

Voir les fichiers exemples: conf_apache.template
