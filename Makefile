SHELL = /bin/sh
environment_bin := ./.venv/bin
.PHONY: editable_install test


dev_dependencies: .venv
	${environment_bin}/pip3 install --upgrade pip
	${environment_bin}/pip3 install -r ./requirements/dev.txt

editable_install: dev_dependencies
	${environment_bin}/pip3 install --editable .

test:
	${environment_bin}/python3 -m unittest discover ./tests/ 'test_*.py'

.venv:
	python3 -m venv ./.venv
