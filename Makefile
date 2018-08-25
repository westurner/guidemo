

install:
	pip install -r ./requirements.txt

setup-toga-cookiecutter:
	pip install cookiecutter briefcase
	cookiecutter https://github.com/pybee/briefcase-template
