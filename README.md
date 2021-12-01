### Hexlet tests and linter status:
[![Actions Status](https://github.com/renata-nerenata/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/renata-nerenata/python-project-lvl2/actions)
[![Actions Status](https://github.com/renata-nerenata/python-project-lvl2/workflows/test.yml/badge.svg)](https://github.com/renata-nerenatapython-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a48adcf1d95882daed37/maintainability)](https://codeclimate.com/github/renata-nerenata/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a48adcf1d95882daed37/test_coverage)](https://codeclimate.com/github/renata-nerenata/python-project-lvl2/test_coverage)


### Codeclimate chech up status:
<a href="https://codeclimate.com/github/codeclimate/codeclimate/maintainability"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability" /></a>

## Difference generator

Utility for finding difference between .json and .yml files. Report can be presented in three forms:
- stylish
- plain
- json

### Run

```console
poetry run python -m gen_diff.gendiff first_file second_file style
```

### Demo

#### Stylish: flat files
[![asciicast](https://asciinema.org/a/452906.svg)](https://asciinema.org/a/452906)

#### Plain: flat files
[![asciicast](https://asciinema.org/a/452909.svg)](https://asciinema.org/a/452909)

#### JSON: flat files
[![asciicast](https://asciinema.org/a/452912.svg)](https://asciinema.org/a/452912)

_____

#### Stylish: complex files
[![asciicast](https://asciinema.org/a/452919.svg)](https://asciinema.org/a/452919)

#### Plain: complex files
[![asciicast](https://asciinema.org/a/452918.svg)](https://asciinema.org/a/452918)

#### JSON: complex files
[![asciicast](https://asciinema.org/a/452916.svg)](https://asciinema.org/a/452916)
