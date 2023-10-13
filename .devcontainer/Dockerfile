FROM mcr.microsoft.com/devcontainers/jekyll:2-bullseye
ARG PYTHON_VERSION="3.11.6"
ENV VERSION=${PYTHON_VERSION}

USER root

ADD --chmod=0755 https://raw.githubusercontent.com/devcontainers/features/main/src/python/install.sh /tmp/
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && /tmp/install.sh

COPY requirements-dev.txt /tmp/requirements-dev.txt
RUN /usr/local/python/${PYTHON_VERSION}/bin/python3 -m pip install --no-cache-dir -r /tmp/requirements-dev.txt \
    && /usr/local/python/${PYTHON_VERSION}/bin/python3 -m playwright install --with-deps

COPY --chmod=0755 .devcontainer/post-create-bpdevs.sh /usr/local/post-create-bpdevs.sh
