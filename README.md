# Temperature Converter

A simple desktop GUI app built with Python's `tkinter` that converts between Celsius and Fahrenheit.

## Features
- Convert Celsius → Fahrenheit
- Convert Fahrenheit → Celsius
- Lightweight GUI, no external dependencies

## Requirements
- Python 3.x (tkinter is included in the standard library on most systems)

## Usage
Run the notebook `temperature_converter.ipynb` in Jupyter, or extract the code into a `.py` file and run:

```bash
python temperature_converter.py
```

Enter a value in the corresponding field and click **Convert** to see the result.

## How it works
- `c_to_f()` reads the Celsius entry, applies `(C * 9/5) + 32`, and displays the result.
- `f_to_c()` reads the Fahrenheit entry, applies `(F - 32) * 5/9`, and displays the result.

## License
MIT
