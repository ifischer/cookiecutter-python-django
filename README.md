Python Django Cookiecutter template
==================================

Cookiecutter scaffold to create minimal Python Django web application.
Features:

* proper module setup with setup.py and requirements.txt
* Docker as sole requirement
* Makefile for quick access to Docker commands 

Installation
------------

Install cookiecutter:
```
# Globally:
pip install cookiecutter

# Via pipsi (https://github.com/mitsuhiko/pipsi):
pipsi install cookiecutter
```

Create project from template:
```
cookiecutter -o $PROJECT_HOME .
```

Test
----

To generate the example - thereby testing the scaffold, run:
```
make build test
```
