# Makefile for managing Jekyll project for blackpythondevs.github.io

# Set up the environment by pulling the latest Ruby build definitions, installing Ruby 3.3.5,
# as seen in the .ruby-version file, installing required gems and Python packages,
# and configuring pre-commit hooks

setup:
    # Pull the latest ruby-build plugin updates
	- git -C /root/.rbenv/plugins/ruby-build pull

    # Install Ruby version 3.3.5 using rbenv
	- rbenv install 3.3.5

    # Install the necessary Ruby gems defined in the Gemfile
	- bundle install

    # Install Python dependencies defined in requirements-dev.txt
	- pip install -r requirements-dev.txt

    # Set up pre-commit hooks as defined in the configuration file
	- pre-commit install


# Start the Jekyll development server
start:
	bundle exec jekyll serve


# Start the Jekyll server in detached mode (runs in the background)
start-detach:
	bundle exec jekyll serve --detach


# Stop the detached Jekyll server (Kill the background Jekyll process)
stop-detach:
	pkill -f jekyll
