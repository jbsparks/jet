"""
Simplest plugin that exercises all the hooks
"""
from jet.hooks import hookimpl


@hookimpl
def jet_extra_user_conda_packages():
    return [
        "hypothesis",
    ]


@hookimpl
def jet_extra_user_pip_packages():
    return [
        "django",
    ]


@hookimpl
def jet_extra_hub_pip_packages():
    return [
        "there",
    ]


@hookimpl
def jet_extra_apt_packages():
    return [
        "sl",
    ]


@hookimpl
def jet_config_post_install(config):
    # Put an arbitrary marker we can test for
    config["simplest_plugin"] = {"present": True}


@hookimpl
def jet_custom_jupyterhub_config(c):
    c.JupyterHub.authenticator_class = "tmpauthenticator.TmpAuthenticator"


@hookimpl
def jet_post_install():
    with open("test_post_install", "w") as f:
        f.write("123456789")


@hookimpl
def jet_new_user_create(username):
    with open("test_new_user_create", "w") as f:
        f.write(username)
