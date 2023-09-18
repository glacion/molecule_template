.PHONY: prepare venv clean

ABS_DIR := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))
REL_DIR := $(notdir $(ABS_DIR:/=))
VENV := $(addsuffix .venv, $(ABS_DIR))

prepare: venv
	$(VENV)/bin/pre-commit run --all-files

venv:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -U .

clean:
	rm -rf .venv ~/.cache/molecule/$(REL_DIR)

