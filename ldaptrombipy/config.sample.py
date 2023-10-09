API_PORT = 5006
# LDAP CONFIG
SERVER = "192.168.20.230"
PORT = 389
# SERVER = "ldap://192.168.20.230"
DN = "MY_DN"
PASSWORD = "lalala"
EXCLUDED_GROUPS = ["Utilisateurs Partis"]
# the location in the DIT where the search will start
BASE_QUERY = "dc=bidule,dc=dom"

# default filters = l'élément du ldap doit avoir un nom de famille (sn)
# tout les élément du ldap sans "sn" ne remonteront pas dans le trombi
SEARCH_FILTERS = {"sn": "*"}

# CALDAV CONFIG
CALDAV_SERVER = ""
CALDAV_USERNAME = ""
CALDAV_PASSWORD = ""
