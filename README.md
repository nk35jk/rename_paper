# Rename Paper

Rename pdf file name to the title of the paper.

![demo](https://user-images.githubusercontent.com/30214093/56454634-b5e99200-638e-11e9-8846-c4d72f9c51f0.png)

## Installation

### Requirements

- macOS
- Python 3
- pdfminer3
- lxml

```
pip install lxml
pip install pdfminer3
```

```
git clone https://github.com/nk35jk/rename_paper.git
cd rename_paper
cp rename_paper.py /usr/local/bin/rename_paper
```

(optional) Automator

## Usage

### GUI
Select pdf files in Finder and press `command + R` to rename them. 

### Command line
`python rename_paper.py /path/to/pdf_file`
