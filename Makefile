SHELL = /bin/sh
environment_bin := ./.venv/bin
.PHONY: lint_check editable_install test


dev_dependencies: .venv
	${environment_bin}/pip3 install --upgrade pip
	${environment_bin}/pip3 install -r ./requirements/dev.txt

editable_install: .venv
	${environment_bin}/pip3 install --editable .

lint_check:
	${environment_bin}/pylint ./show_me_the_money/**/*py

test:
	${environment_bin}/python3 -m unittest discover ./test/**/ 'test_*.py'

.venv:
	python3 -m venv ./.venv
