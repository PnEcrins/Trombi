from functools import wraps
from flask import g
from ldaptrombipy.config import PASSWORD, SERVER, DN, PORT
import ldap3


def connect():
    ldap_srv = ldap3.Server(SERVER, port=PORT, get_info=ldap3.ALL)
    ldap_cnx = ldap3.Connection(ldap_srv, user=DN, password=PASSWORD)
    ldap_cnx.bind()
    g.ldap_cnx = ldap_cnx
    return ldap_cnx


def ldap_connect(view):
    """
    Décorateur pour les vues qui nécéssitent une connexion au LDAP.
    """

    @wraps(view)
    def _require_ldap_conn(*args, **kwargs):
        conn = connect()
        kwargs["ldap_cnx"] = conn
        return view(*args, **kwargs)

    return _require_ldap_conn
