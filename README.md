# Vectorized Masker

A image manipulation script that replaces target background colors using vectorized matrix operations instead of iterative pixel loops.

## Core Concepts Demonstrated
* **Array Vectorization:** Leverages NumPy multidimensional arrays to apply conditional color masks across entire image dimensions simultaneously, bypassing Python loop overhead.
* **Boolean Masking:** Utilizes `numpy.all()` across the color channel axis (`axis=-1`) to evaluate RGB threshold criteria instantly.

## Requirements
1. **Python** `Python 3.x` or higher
2. **Pillow:** `pip install Pillow`
3. **NumPy:** `pip install numpy`
