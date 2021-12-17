import glob
import os 

from pathlib import Path

from flask import Blueprint, jsonify, request
from ldap3 import ALL_ATTRIBUTES, SUBTREE
from werkzeug.exceptions import BadRequest

from ldaptrombipy.ldap_utils import ldap_connect
from ldaptrombipy.config import BASE_QUERY
from ldaptrombipy.env import STATIC_IMAGE_PATH
from ldaptrombipy.config import EXCLUDED_GROUPS

blueprint = Blueprint("api", __name__)


RETURNED_ATTR = [
    "cn",
    "sn",
    "displayName",
    "whenCreated",
    "description",
    "memberOf",
    "distinguishedName",
    "department",
    "mail",
    "homePhone",
    "sAMAccountName",
    "mobile"
]



def build_ldap_filter_string(filters):
    and_filters = {"objectclass": "user", "cn": "*", "sn": "*"}
    if "department" in filters:
        and_filters["department"] = filters["department"]
    f_string = ""
    for attr, filter in and_filters.items():
        f_string = f"{f_string}({attr}={filter})"
    return f"(&{f_string})"


@blueprint.route("/users")
@ldap_connect
def all_users(ldap_cnx):
    filters = request.args.to_dict()
    f_string = build_ldap_filter_string(filters)
    ldap_cnx.search(
        search_base=BASE_QUERY,
        search_filter=f_string,
        search_scope=SUBTREE,
        attributes=RETURNED_ATTR,
    )
    data = []
    for r in ldap_cnx.response:
        data.append(r.get("attributes", ""))
    return jsonify(data)


@blueprint.route("/users_order_by_dep")
@ldap_connect
def all_users_by_dep(ldap_cnx):
    filters = request.args.to_dict()
    f_string = build_ldap_filter_string(filters)
    # TODO : groups voir nextcloud
    ldap_cnx.search(
        search_base=BASE_QUERY,
        search_filter=f_string,
        search_scope=SUBTREE,
        attributes=RETURNED_ATTR,
    )
    data = {}
    for r in ldap_cnx.response:
        user = r.get("attributes", "")
        if user:
            dn = user["distinguishedName"].split(",")
            dn = "=".join(dn).split("=")
            wanted_user = True
            for excluded_groups in EXCLUDED_GROUPS:
                if excluded_groups in dn:
                    wanted_user = False
            if wanted_user:
                login = user.get("sAMAccountName", "")+".*"
                photo_path = glob.glob(str(STATIC_IMAGE_PATH / login))
                if len(photo_path) > 0:
                    user["has_photo"] = True
                    user["photo_extension"] = photo_path[0].split(".")[-1]
                dep = user["department"]
                if len(dep) > 0:
                    cur_dep = dep
                else:
                    cur_dep = "Autre"
                data.setdefault(cur_dep, []).append(user)
    sorted_users = {}
    for key, val in data.items():
        sorted_users[key] = sorted(val, key=lambda k : k["displayName"])
    return jsonify(sorted_users)


@blueprint.route("/test")
@ldap_connect
def test(ldap_cnx):
    filters = request.args.to_dict()
    f_string = build_ldap_filter_string(filters)
    # TODO : groups voir nextcloud
    ldap_cnx.search(
        search_base=BASE_QUERY,
        search_filter=f_string,
        search_scope=SUBTREE,
        attributes=ALL_ATTRIBUTES,
    )
    with open("/tmp/truc.txt", "w") as f:
        for r in ldap_cnx.response:
            user = r.get("attributes", "")
            f.write(str(user))
    return 'la'
    

@blueprint.route("/upload_photo/<user>", methods=["POST"])
def updload_photo(user):
    file = request.files.get("image")
    if file:
        extension = file.filename.split(".")[1].lower()
        search_photo = Path(STATIC_IMAGE_PATH / f"{user}.*")
        for exist_photo in glob.glob(str(search_photo)):
            os.remove(exist_photo)
        new_file_path = Path(STATIC_IMAGE_PATH / f"{user}.{extension}")
        file.save(new_file_path)
        return str(new_file_path)
    return BadRequest("No file")


# https://github.com/cannatag/ldap3/issues/327
# search_filter="(&(objectclass=person)(memberof:1.2.840.113556.1.4.1941:=CN=Administrateurs,CN=Builtin,DC=PNE,DC=dom))",
