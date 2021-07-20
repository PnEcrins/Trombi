from pathlib import Path


from flask import Blueprint, jsonify, request
from ldap3 import SUBTREE
from werkzeug.exceptions import BadRequest

from ldaptrombipy.ldap_utils import ldap_connect
from ldaptrombipy.env import STATIC_IMAGE_PATH
from ldaptrombipy.config import EXCLUDED_GROUPS

blueprint = Blueprint("api", __name__)
base = "dc=pne,dc=dom"


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
    # TODO : groups voir nextcloud
    # if "group" in filters:
    ldap_cnx.search(
        search_base=base,
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
        search_base=base,
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
                login = user.get("sAMAccountName", "") + ".jpg"
                file = Path(STATIC_IMAGE_PATH / login)
                user["has_photo"] = file.exists()
                dep = user["department"]
                if len(dep) > 0:
                    cur_dep = dep
                else:
                    cur_dep = "Autre"
                data.setdefault(cur_dep, []).append(user)
    return jsonify(data)


@blueprint.route("/upload_photo/<user>", methods=["POST"])
def updload_photo(user):
    file = request.files.get("image")
    if file:
        print(file)
        extension = file.filename.split(".")[1].lower()
        print(extension)
        if extension == "jpg":
            new_file_path = Path(STATIC_IMAGE_PATH / f"{user}.{extension}")
            file.save(new_file_path)
            return str(new_file_path)
        else:
            return BadRequest("Extension must be .jpg")
    return BadRequest("No file")


# https://github.com/cannatag/ldap3/issues/327
# search_filter="(&(objectclass=person)(memberof:1.2.840.113556.1.4.1941:=CN=Administrateurs,CN=Builtin,DC=PNE,DC=dom))",
