# Merge-PDF

Merge-PDF is a simple tool to merge your PDFs offline for free.

## Requirements

Make sure you have [Python 3.7+](https://www.python.org/downloads/) with [pip](https://pip.pypa.io/en/stable/installation/) installed.

```shell
python3 --version && python3 -m pip --version
```

## Installation

- Clone this repository.

```shell
git clone https://github.com/kyllianasselindebeauville/merge-pdf.git
```

- Change directory into it.

```shell
cd merge-pdf
```

- Use the package manager `pip` to install `merge-pdf`.

```shell
python3 -m pip install .
```

## Usage

```
usage: merge-pdf [-h] [-o out] [-V] [files ...]

Merge PDF files.

positional arguments:
  files                 PDF files to merge

options:
  -h, --help            show this help message and exit
  -o out, --output out  name of the output file
  -V, --version         show program's version number and exit
```

## Examples

- Merge multiple PDF files *(default behavior)*.

```shell
merge-pdf file1.pdf file2.pdf file3.pdf
```

> file1-merged.pdf

- Merge multiple PDF files into a specified output file.

```shell
merge-pdf -o output.pdf file1.pdf file2.pdf file3.pdf
```

> output.pdf

## Contributing

Pull requests are welcome. Please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)
