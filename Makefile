.PHONY: venv install
UNAME := $(shell uname)

venv:
ifeq ($(UNAME), Windows)
	py -3 -m venv venv;
else
	python3 -m venv venv
endif

install: venv
ifeq ($(UNAME), Windows)
	venv\Scripts\activate.bat; \
	pip3 install -r requirements.txt;
else
	. venv/bin/activate; \
	pip3 install -r requirements.txt;
endif

serve-setup:
	. venv/bin/activate; \
	python3 manage.py migrate;

serve:
	. venv/bin/activate; \
	python3 manage.py runserver 0.0.0.0:8000;
