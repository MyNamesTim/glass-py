# Reference Image Overlay Tool

A lightweight Python tool for overlaying an image on your screen at any position and scale. Useful for artists, designers, or developers who want to trace, reference, or compare images without switching windows.

---

## Features

- Load any image from your filesystem.
- Click anywhere on the screen to position the overlay.
- Scale the image up or down while preserving the aspect ratio.
- Always-on-top, borderless window for unobstructed reference.
- Cross-platform: works on Windows, Linux, and macOS.
- Safeguards in case of a scaling error.

---

## Requirements

- Python 3.8+  
- [Pillow](https://pypi.org/project/Pillow/) (for image handling)  
- [tkinter](https://docs.python.org/3/library/tkinter.html) (comes with most Python installs)

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/mynamestim/reference-overlay-python.git
cd reference-overlay-python
```

2. Install dependencies:
```bash
pip install pillow
```

## Usage

1. Run the Python script:
```bash
python reference_overlay.py
```
2. Enter desired scale
3. Select image from file viewer
4. Click to position image on screen
5. Close ```cmd``` window when finished
