FROM mcr.microsoft.com/devcontainers/jekyll:2-bullseye
LABEL org.opencontainers.image.source https://github.com/oleksis/blackpythondevs.com
LABEL org.opencontainers.image.description "Black Python Developers website."

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y build-essential git \
    && rm -rf /var/lib/apt/lists/*

# Install rbenv and ruby-build
RUN git clone https://github.com/rbenv/rbenv.git ~/.rbenv \
    && echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc \
    && echo 'eval "$(rbenv init -)"' >> ~/.bashrc \
    && git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build \
    && echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc

# Install Ruby 3.2.2
RUN /bin/bash -c 'source ~/.bashrc && rbenv install $(cat .ruby-version) && rbenv global $(cat .ruby-version)'

COPY requirements-dev.txt /usr/local/requirements-dev.txt
# COPY --chmod=0755 .github/.devcontainer/on-create-bpdevs.sh /usr/local/on-create-bpdevs.sh
COPY --chmod=0755 .github/.devcontainer/post-create-bpdevs.sh /usr/local/post-create-bpdevs.sh

EXPOSE 4000/tcp
