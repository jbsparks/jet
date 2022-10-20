#  CCPE JupyterHub Experience Tutorial (JET) ![](jetpack.png)

[![GitHub](https://img.shields.io/badge/issue_tracking-github-blue?logo=github)](https://github.com/jbsparks/jet/issues)

**CCPE JupyterHub Experience Tutorial** (JET) distribution helps you provide Jupyter Notebooks
to 1-100 users on a single server.

The primary audience are people who do not consider themselves 'system administrators'
but would like to provide hosted Jupyter Notebooks for their students or users.
All users are provided with the same environment, and administrators
can easily install libraries into this environment without any specialized knowledge.

See the [latest documentation](https://github.com/jbsparks/jet/tree/main/docs)
for more information on using JET or 'The Littlest JupyterHub' from which it's derived from, albeit this is SLES based.

## Development Status

This project is currently in **_very_ alpha** state. Folks have been using installations
of ``JET`` for more than a year now to great success. While we try hard not to, we
might still make breaking changes that have no clear upgrade pathway.

## Installation

The JupyterHub (JET) can run on any server that is running at least
**SLES15sp3**.

We have several tutorials to get you started.

- Tutorials to create a new server from scratch on a provider & run JET
  on it. These are **recommended** if you do not have much experience setting up
  servers.
  - ... your favorite provider here, if you can contribute!

- Tutorial to install JET on an already running server you have root access to.
  You should use this if your cloud provider does not already have a direct tutorial,
  or if you have experience setting up servers.

## Documentation

We place a high importance on consistency, readability and completeness of
documentation. If a feature is not documented, it does not exist. If a behavior
is not documented, it is a bug! We try to treat our documentation like we treat
our code: we aim to improve it as often as possible.

If something is confusing to you in the documentation, it is a bug. We would be
happy if you could [file an issue on the github project](https://github.com/jbsparks/jet/issues) about it - or
even better, contribute.

## How to get started, a developers guide

The easiest & safest way to develop and test JET is with Docker.

1. Install Docker Community Edition by following the instructions on their website.
2. Clone the git repo (or your fork of it).
3. Build a docker image that has a functional systemd in it.

In the following example, we are using a ``ccpe`` container as the base and hence providing PE as an environment to jupyterhub environment. 

```bash
docker build --tag jet-systemd --build-arg "ccpe_image=ccpe-rocm:22.10" --file integration-tests/Dockerfile .
```

Run a docker container with the image in the background, while bind mounting your JET repository under ``/srv/src``.
```bash
docker rm --force jet-dev      # is there is an old one running
docker run \
  --privileged \
  --detach \
  --name=jet-dev \
  --publish 12000:80 \
  --mount type=bind,source=$(pwd),target=/srv/src \
  jet-systemd
```
Check the status
```bash
docker ps -a --filter "name=jet-dev"
CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS         PORTS                                     NAMES
36c94071dc1d   jet-systemd   "/bin/bash -c 'exec …"   3 minutes ago   Up 3 minutes   0.0.0.0:12000->80/tcp, :::12000->80/tcp   jet-dev
```

Get a shell inside the running docker container. 

**Note:** If you are into VSCode, you can connect to the local running container :smiley: 

see https://code.visualstudio.com/docs/remote/attach-container

```bash
docker exec -it jet-dev /bin/bash
```

Run the bootstrapper from inside the container (see step above): The container image is already set up to default to a ``dev`` install, so it’ll install from your local repo rather than from github.
```bash
python3 /srv/src/bootstrap/bootstrap.py --admin admin
```
_Or, if you would like to setup the admin’s password during install, you can use this command (replace “admin” with the desired admin username and “password” with the desired admin password):_

```bash
python3 /srv/src/bootstrap/bootstrap.py --admin admin:<password>
```
* The primary hub environment will also be in your PATH already for convenience.
You should be able to access the JupyterHub from your browser now at [http://localhost:12000](http://localhost:12000). 

  Congratulations, you are set up to develop **JET**!
* Make some changes to the repository. You can test easily depending on what you changed.

  * If you changed the bootstrap/bootstrap.py script or any of its dependencies, you can test it by running ``python3 /srv/src/bootstrap/bootstrap.py``.

  * If you changed the jet/installer.py code (or any of its dependencies), you can test it by running ``python3 -m jet.installer``.

  * If you changed jet/jupyterhub_config.py, jet/configurer.py, /opt/jet/config/ or any of their dependencies, you only need to restart jupyterhub for them to take effect. jet-config reload hub should do that.

Looking at Logs has information on looking at various logs in the container to debug issues you might have.