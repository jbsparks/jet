from setuptools import setup, find_packages

setup(
    name="JupyterHub_Experience_Tutorial",
    version="0.1",
    description="A small JupyterHub distribution",
    url="https://github.com/jbsparks/jet",
    author="Jupyter Development Team",
    author_email="jupyter@googlegroups.com",
    license="3 Clause BSD",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "ruamel.yaml==0.17.*",
        "jinja2",
        "pluggy==1.*",
        "passlib",
        "backoff",
        "requests",
        "bcrypt",
        "jupyterhub-traefik-proxy==0.3.*",
    ],
    entry_points={
        "console_scripts": [
            "jet-config = jet.config:main",
        ]
    },
)
