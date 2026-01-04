# Reference Image Overlay Tool

A lightweight Python tool for overlaying an image on your screen at any position and scale. Useful for artists, designers, or developers who want to reference or compare images without switching windows.

---

## Features

- Load any image from your filesystem.
- Click anywhere on the screen to position the overlay.
- Scale the image up or down while preserving the aspect ratio.
- Always-on-top, borderless window for unobstructed reference.
- Cross-platform: works on Windows, Linux, and macOS.
- Safeguards in case of a scaling error.

---

## Upcoming/Desired Features and Updates

* Click-through capability.
* Previews when hovering mouse cursor and waiting to set image position.
* Allow alpha/opacity to be changed.
* Scaling slider/input UI with image preview/dimensions.
* More user-friendly UI, perhaps outside of ```cmd```.

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
2. Enter desired scale.
3. Select image from file viewer.
4. Click to position image on screen.
5. Close ```cmd``` window when finished.

---

## License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.  

You are free to:

- **Use** the software for any purpose  
- **Modify** it to suit your needs  
- **Distribute** copies of your modifications  

Under the condition that **any modifications you deploy or distribute, including over a network, must also be released under the AGPL-3.0**.  

For the full license text, see [LICENSE](LICENSE) or visit [GNU AGPL v3.0](https://www.gnu.org/licenses/agpl-3.0.html).
