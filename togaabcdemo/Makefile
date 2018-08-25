
default:
	@echo "Toga ABC Demo Makefile"
	@echo "setup-linux -- python setup.py linux -s"

setup-linux-virtualenv:
	@# virtualenv -p /usr/bin/python3.6 guidemo --system-site-packages
	@# OR:
	cd ${VIRTUAL_ENV}/lib/python3.6/site-packages
	ln -si /usr/lib/python3.6/dist-packages/gi

setup-toga-linux-deps:
	sudo dnf install -y pygobject3 python3-gobject \
		python3-cairo-devel cairo-gobject-devel gobject-introspection-devel

setup-linux:
	python setup.py linux -s

build: setup-linux
