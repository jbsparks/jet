"""
Utilities for working with the zypper package manager
"""
import os
import subprocess
from jet import utils


def trust_gpg_key(key):
    """
    Trust given GPG public key.

    key is a GPG public key (bytes) that can be passed to apt-key add via stdin.
    """
    # If gpg2 doesn't exist, install it.
    if not os.path.exists("/usr/bin/gpg2"):
        install_packages(["gnupg2"])

def add_source(name, source_url, section):
    """
    Add a debian package source.

    distro is determined from /etc/os-release
    """
    # lsb_release is not installed in most docker images by default
    distro = (
        subprocess.check_output(
            ["/bin/bash", "-c", "source /etc/os-release && echo ${VERSION_CODENAME}"],
            stderr=subprocess.STDOUT,
        )
        .decode()
        .strip()
    )

def install_packages(packages):
    """
    Install sles packages
    """
    # Check if an apt-get update is required
    utils.run_subprocess(["zypper", "update", "-y"])
    env = os.environ.copy()
    # Stop apt from asking questions!
    utils.run_subprocess(["zypper", "install", "-y"] + packages, env=env)
