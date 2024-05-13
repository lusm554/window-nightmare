create_venv:
	python3 -m venv .venv

install_reqs: create_venv
	.venv/bin/pip install -r requirements.txt --quiet

run: install_reqs
	.venv/bin/python3 main.py index.html

all: run
