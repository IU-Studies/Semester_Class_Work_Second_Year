# NumPy Quick Read

This repository provides a quick overview of essential NumPy operations for Python developers. From creating arrays to performing advanced operations like reshaping and random value generation, this guide serves as a starting point for anyone looking to understand and use NumPy efficiently.

---

## Prerequisites

- Python 3.x installed on your system.
- Install NumPy using pip:
  ```bash
  pip install numpy
  ```

## Getting Started

To use NumPy in your script, import it as follows:
```python
import numpy as np
```

---

## Contents

### 1. **Creating NumPy Arrays**
- **Basic Array Creation:**
  ```python
  arr = np.array([1, 2, 3])
  print(arr)
  ```
- **Array from User Input:**
  ```python
  l = []
  for i in range(5):
      user_input = int(input("Enter value: "))
      l.append(user_input)
  print(np.array(l))
  ```

### 2. **Array Dimensions**
- **Find Dimensions:**
  ```python
  arr = np.array([3, 2, 4])
  print(arr.ndim)
  ```
- **2D Array:**
  ```python
  arr = np.array([[1, 2, 3], [5, 6, 7]])
  print(arr.ndim)
  ```
- **3D Array:**
  ```python
  arr = np.array([[[1, 2, 3], [5, 6, 7], [0, 8, 7]]])
  print(arr.ndim)
  ```
- **Higher Dimensional Array:**
  ```python
  arr = np.array([1, 2, 3, 4], ndmin=10)
  print(arr.ndim)
  ```

### 3. **Pre-filled Arrays**
- **Zero-filled Array:**
  ```python
  arr = np.zeros(4)
  print(arr)
  ```
- **One-filled Array:**
  ```python
  arr = np.ones(4)
  print(arr)
  ```
- **Empty Array:**
  ```python
  arr = np.empty(4)
  print(arr)
  ```

### 4. **Range and Sequence Generation**
- **Using `arange`:**
  ```python
  arr = np.arange(1, 11)
  print(arr)
  ```
- **Using `linspace`:**
  ```python
  arr = np.linspace(0, 10, num=5)
  print(arr)
  ```

### 5. **Identity and Random Arrays**
- **Identity Matrix:**
  ```python
  arr = np.eye(4)
  print(arr)
  ```
- **Random Arrays:**
  - Uniform Distribution (`rand`):
    ```python
    arr = np.random.rand(5)
    print(arr)
    ```
  - Normal Distribution (`randn`):
    ```python
    arr = np.random.randn(5)
    print(arr)
    ```
  - Fractional Values (`ranf`):
    ```python
    arr = np.random.ranf(5)
    print(arr)
    ```
  - Integers (`randint`):
    ```python
    arr = np.random.randint(1, 10, 5)
    print(arr)
    ```

### 6. **Data Types**
- **Check Data Type:**
  ```python
  arr = np.array([1, 2, 3])
  print(arr.dtype)
  ```
- **Explicit Type Conversion:**
  ```python
  arr = np.array([1, 2, 3], dtype=np.int8)
  print(arr.dtype)
  ```

### 7. **Array Shape and Reshape**
- **Check Shape:**
  ```python
  arr = np.array([[1, 2], [5, 6], [7, 8]])
  print(arr.shape)
  ```
- **Reshape Array:**
  ```python
  arr = np.array([1, 2, 3, 4, 5, 6])
  temp_arr = arr.reshape(3, 2)
  print(temp_arr)
  ```



