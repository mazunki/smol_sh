.PHONY: environment activate run test clean

.DEFAULT_GOAL := run

environment:
	conda create -n smolsh
	conda activate smolsh
	conda install python=3.10
	pip install -e .

activate:
	conda activate smolsh

run: activate
	@python -m smol_sh

test:
	@python -m unittest tests/test.py

clean:
	rm -rf **/__pycache__
