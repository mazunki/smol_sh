
# Smol Shell
`smol_sh` is a Python >=3.10 shell, inspired by a desire to learn how shells are built, and aims to integrate Python into the user's environment.

It is not a POSIX-compliant shell, by default, but may eventually support different modes.

## Features

- Colourful shell by default
- JSON built-in support
- Object piping (not only text)
- Saving commands and arguments for later reuse

## Requirements

- `python3.10` or newer
- `pygments` for colourful shell
- `conda` for a safe environment

## Installation

The automatic installation expects the usage of Conda to keep the environment set up. You could manage this yourself if you want to.

Use the `Makefile`. There are mainly four targets:

- `make environment` (run it once, it will set up the `smolsh` virtual environment)
- `make activate` simply changes the conda environment to `smolsh`.

- `make run` will boot up a shell
- `make test` will run the tests

## Warranty and License

Do whatever you want with this, but please don't sell it, and keep attribution where it's due. I am not responsible if you break something to not reading the source code.

Pull requests, feature suggestions, and general complaints are welcome :)

