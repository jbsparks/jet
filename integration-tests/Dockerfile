# Systemd inside a Docker container, for CI only
ARG ccpe_image
FROM ${ccpe_image}

RUN zypper install -y \
        systemd \
        curl \
        git \
        sudo

# Kill all the things we don't need
RUN find /etc/systemd/system \
    /usr/lib/systemd/system \
    -path '*.wants/*' \
    -not -name '*journald*' \
    -not -name '*systemd-tmpfiles*' \
    -not -name '*systemd-user-sessions*' \
    -exec rm \{} \;

RUN mkdir -p /etc/sudoers.d
RUN systemctl set-default multi-user.target

STOPSIGNAL SIGRTMIN+3

# comment these lines out for a none-development install
ENV JET_BOOTSTRAP_DEV=yes
ENV JET_BOOTSTRAP_PIP_SPEC=/srv/src
ENV PATH=/opt/tljh/hub/bin:${PATH}

CMD ["/bin/bash", "-c", "exec /usr/lib/systemd/systemd --log-target=journal 3>&1"]
