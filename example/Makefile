.PHONY: help
.DEFAULT_GOAL := help
CONTAINER  = example_docker_container_name
VIRTUALENV_DIR = .venv
VOLUMES = -v $$(pwd):/code
PORTS = -p 8000:8000
DOCKER_RUN = docker run $(PORTS) --rm -it $(VOLUMES) $(CONTAINER)

help:
	# Print help by extracting ##-comments per target
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

docker-clean clean:
	-docker stop $(CONTAINER)
	-docker rm -f $(CONTAINER)

docker-build build:  ## Build Docker container
	docker build -t $(CONTAINER) .

docker-run run:  ## Run Docker container
	$(DOCKER_RUN)

docker-shell:  ## Run Docker shell
	$(DOCKER_RUN) bash

docker-test test:
	$(DOCKER_RUN) pytest

docker-ipython:
	$(DOCKER_RUN) ipython


virtualenv-create:  ## Create virtualenv
	virtualenv --python=$$(which python3.7) $(VIRTUALENV_DIR)
	$(VIRTUALENV_DIR)/bin/pip3 install -r requirements.txt
	$(VIRTUALENV_DIR)/bin/pip3 install -r requirements-dev.txt
	$(VIRTUALENV_DIR)/bin/pip3 install .
	@echo "Activate virtualenv:\n. $(VIRTUALENV_DIR)/bin/activate"

virtualenv-test:
	$(VIRTUALENV_DIR)/bin/pytest


lint:  ## Run linter (Flake8, isort)
	$(DOCKERCMD) pytest --flake8
	$(DOCKERCMD) pytest --isort
