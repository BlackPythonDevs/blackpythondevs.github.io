FROM mcr.microsoft.com/devcontainers/jekyll:2-bullseye
LABEL org.opencontainers.image.source https://github.com/oleksis/blackpythondevs.com
LABEL org.opencontainers.image.description "Black Python Developers website."

COPY requirements-dev.txt /tmp/requirements-dev.txt
COPY --chmod=0755 .devcontainer/post-create-bpdevs.sh /usr/local/post-create-bpdevs.sh

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && rm -rf /var/lib/apt/lists/*

EXPOSE 4000/tcp
