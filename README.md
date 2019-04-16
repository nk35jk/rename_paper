# Rename Paper

Rename pdf file name to the title of the paper.

## Requirements

- Python 3
- pdfminer3
- lxml

```
pip install lxml
pip install pdfminer3
```

## Set up

```
cp rename_paper.py /usr/local/bin/rename_paper
```

(optional) Make quick action with Automator
```
source ~/.zshrc
for f in "$@"
do
	${HOME}/.pyenv/shims/python /usr/local/bin/rename_paper "$f"
done
```

## How to Use


`python rename_paper.py /path/to/pdf_file`
