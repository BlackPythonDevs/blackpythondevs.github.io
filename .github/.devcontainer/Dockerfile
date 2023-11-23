FROM mcr.microsoft.com/devcontainers/jekyll:2-bullseye
LABEL org.opencontainers.image.source https://github.com/oleksis/blackpythondevs.com
LABEL org.opencontainers.image.description "Black Python Developers website."

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && rm -rf /var/lib/apt/lists/*

COPY requirements-dev.txt ./requirements-dev.txt
COPY --chmod=0755 .github/.devcontainer/on-create-bpdevs.sh /usr/local/on-create-bpdevs.sh
COPY --chmod=0755 .github/.devcontainer/post-create-bpdevs.sh /usr/local/post-create-bpdevs.sh

EXPOSE 4000/tcp
