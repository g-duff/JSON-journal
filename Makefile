SHELL = /bin/sh

environment := ./.venv
environment_bin := ${environment}/bin

.PHONY: clean format editable_install lint_check test

# Default Goal
editable_install: dev_dependencies
	${environment_bin}/pip3 install --editable .

clean:
	rm -rf ${environment}

dev_dependencies: .venv
	${environment_bin}/pip3 install --upgrade pip
	${environment_bin}/pip3 install -r ./requirements/dev.txt

format:
	${environment_bin}/autopep8 --in-place ./json_journal/*py ./tests/*py

lint:
	${environment_bin}/pylint ./json_journal/*py ./tests/*py

test:
	${environment_bin}/python3 -m unittest discover ./tests/ 'test_*.py'

.venv:
	python3 -m venv ${environment}
