.PHONY: run test clean

.DEFAULT_GOAL := run

environment:
	conda create -n smolsh
	conda activate smolsh
	conda install python=3.10
	pip install -e .

run:
	@python -m smol_sh

test:
	@python -m unittest tests/test.py

clean:
	rm -rf **/__pycache__
