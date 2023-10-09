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

# default filters
# tout les éléments remontent avec cette config
SEARCH_FILTERS = {"objectClass": "*"}
# Ne remonter que les éléments avec l'élément sn (surname)
# SEARCH_FILTERS = {"sn": "*"}

# CALDAV CONFIG
CALDAV_SERVER = ""
CALDAV_USERNAME = ""
CALDAV_PASSWORD = ""
