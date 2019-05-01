# Rename Paper

Rename pdf file name to the title of a paper. It's easy to find a paper with Spotlight search or related applications (like Alfred) using its title.

![demo](https://user-images.githubusercontent.com/30214093/56454634-b5e99200-638e-11e9-8846-c4d72f9c51f0.png)

## Requirements

- macOS
- Python 3
- pdfminer3
- lxml
- NumPy

## Installation

1. Install python packages.

```
pip install lxml
pip install pdfminer3
pip install numpy
```

2. Clone this repository and install a command.

```
git clone https://github.com/nk35jk/rename_paper.git
cd rename_paper
cp rename_paper.py /usr/local/bin/rename_paper
```

3. Install a service (for GUI use).

Open "Rename Paper.workflow" with "Automator.app" and install the "Rename Paper" service (by this, "Rename Paper.workflow" is moved to `$HOME/Library/Services/` directory).

4. Set a keyboard shortcut.

Open "System Preferences.app" and move to `Keyboard -> Shortcuts -> App Shortcuts`. Then, press "+" button to add a keyboard shortcut. Choose "Finder.app" for "Application" field, "Rename Paper" for "Menu Title" field and your favorite keyboard shortcut (command + R is recommended).

## Usage

### GUI

Select pdf files in Finder and press `command + R` to rename them.

### Command line

`python rename_paper.py /path/to/pdf_file`
