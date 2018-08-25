
default:
	@echo "ipywidgets abc demo Makefile"

install:
	pip install notebook ipywidgets
	jupyter nbextension enable --py widgetsnbextension --sys-prefix

install-jupyterlab:
	pip install jupyterlab ipywidgets
	jupyter labextension install @jupyter-widgets/jupyterlab-manager

build:
	jupyter-nbconvert --to=python ./ipywidgets_abc_demo.ipynb
