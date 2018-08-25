
default:
	@echo "Gui demo Makefile"

install:
	pip install -r ./requirements.txt

setup-toga-cookiecutter:
	pip install cookiecutter briefcase
	cookiecutter https://github.com/pybee/briefcase-template

build-togaabcdemo:
	make -C ./togaabcdemo build

build-ipywidgetsdemo:
	make -C ./ipywidgetsdemo build
