# Fibonacci Series in Python

A simple Python program to generate the **Fibonacci Series** for a given number of terms.

## 📌 About

The Fibonacci series is a sequence in which each number is the sum of the previous two numbers.

Example:

```text
0 1 1 2 3 5 8 13 21 ...
```

## 💻 Code

```python
n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
```

## ▶️ Example

**Input:**

```text
Enter number of terms: 7
```

**Output:**

```text
Fibonacci Series:
0 1 1 2 3 5 8
```

## 🧠 How It Works

1. Start with `a = 0` and `b = 1`.
2. Print the value of `a`.
3. Calculate the next number using `c = a + b`.
4. Update `a` and `b`.
5. Repeat the process until the required number of terms is printed.

## 🛠️ Requirements

* Python 3.x

## 🚀 How to Run

```bash
python fibonacci.py
```

## 📚 Concepts Used

* Variables
* `input()`
* `for` loop
* Arithmetic operators
* Updating variables
* Fibonacci sequence

## 👨‍💻 Author

**Nishant Punia**

---

⭐ If you find this project useful, consider giving it a star!
