FROM mcr.microsoft.com/devcontainers/jekyll:2-bullseye
LABEL org.opencontainers.image.source https://github.com/oleksis/blackpythondevs.com
LABEL org.opencontainers.image.description "Black Python Developers website."
ARG RUBY_VERSION=3.2.2

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

# Init rbenv
RUN echo 'eval "$(rbenv init -)"' >> ~/.bashrc

# Install Ruby $RUBY_VERSION
RUN /bin/bash -c 'source ~/.bashrc && rbenv install $RUBY_VERSION && rbenv global $RUBY_VERSION'

COPY requirements-dev.txt /usr/local/requirements-dev.txt
COPY --chmod=0755 .github/.devcontainer/post-create-bpdevs.sh /usr/local/post-create-bpdevs.sh

EXPOSE 4000/tcp
