# Python Learning — Modular, Reusable & Efficient Code

This repository contains small Python projects created while learning and improving my Python programming fundamentals.

The goal is not just to make programs work, but to learn how to write **clean, modular, reusable, efficient, and maintainable code** while applying concepts such as **DRY (Don't Repeat Yourself)**.

## 🎮 Projects

### 1. Rock Paper Scissors

A simple command-line Rock Paper Scissors game.

**Concepts practiced:**

* Functions
* Modularization
* Dictionaries and tuples
* Constants
* Input validation
* Random module
* DRY principle
* Reusable functions

### 2. Guess the Number

A number guessing game where the user tries to guess a randomly generated number between 1 and 1000.

**Concepts practiced:**

* Functions and modularization
* Exception handling
* Input validation
* Loops and conditionals
* Random number generation
* Clean code structure

### 3. Dice Roller

A command-line dice rolling program that allows the user to generate multiple random dice values.

**Concepts practiced:**

* Functions
* List comprehensions
* Random number generation
* Input validation
* Exception handling
* Function reuse
* Modular code structure

### 4. QR Code Generator

A simple QR code generator created to learn how to work with **third-party Python packages** and **virtual environments**.

The program accepts data such as a URL from the user and generates a QR code image using the `qrcode` package.

**Concepts practiced:**

* Third-party Python packages
* `pip`
* Virtual environments
* Dependency management
* `.gitignore`
* User input
* Working with external libraries
* Generating and saving QR code images

## 🧠 What I'm Learning

This repository focuses on improving my understanding of:

* 🐍 Python fundamentals
* 🧩 **Modularization**
* 🔧 **Functions and reusable code**
* ♻️ **DRY — Don't Repeat Yourself**
* 🧹 Clean and readable code
* 🎯 Separation of responsibilities
* 🛡️ Input validation and exception handling
* 📦 Python modules and third-party packages
* 🌱 Virtual environments
* 📋 Dependency management
* 🔄 Code refactoring
* ⚡ Efficient and maintainable code
* 🔀 Git and GitHub fundamentals

## 🌱 Virtual Environments & Third-Party Packages

While building the QR Code Generator, I learned how to create and work with a **Python virtual environment**.

A virtual environment keeps project-specific dependencies isolated from the global Python installation.

### Creating a Virtual Environment

```bash
python -m venv venv
```

### Activating the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

### Installing the Required Package

For the QR Code Generator, I installed the `qrcode` package:

```bash
pip install qrcode
```

### Deactivating the Virtual Environment

```bash
deactivate
```

I also used a **`.gitignore`** file to prevent the `venv/` directory from being tracked by Git.

This helped me understand the basic workflow of:

```text
Create virtual environment
        ↓
Activate environment
        ↓
Install required packages
        ↓
Build the project
        ↓
Use .gitignore to exclude venv/
        ↓
Deactivate environment
```

## 🔄 Refactoring Approach

For each project, I am gradually improving the code instead of trying to write the perfect version immediately.

```text
Make it work
     ↓
Understand the code
     ↓
Identify repeated logic
     ↓
Apply DRY
     ↓
Break code into functions
     ↓
Improve modularity
     ↓
Refactor for readability
```

The goal is to understand **why** these practices are useful rather than simply following them.

## 🔀 Git & GitHub

Along with Python, this repository is also helping me understand **version control and how Git works**.

I am practicing working with:

* Commits
* Branches
* Changes and Git history
* Remote repositories
* GitHub repositories
* `.gitignore`
* Managing and tracking project changes

The repository also gives me practical experience with Git while continuously developing and refactoring these projects.

## 🔎 Algorithms & Data Structures

As I continue learning Python, I have also started implementing and studying basic algorithms and data structures to improve my problem-solving and programming fundamentals.

### Searching Algorithms

Implemented:

* Linear Search
* Binary Search

These helped me understand different searching approaches and their time complexities.

### Sorting Algorithms

Implemented:

* Bubble Sort
* Selection Sort
* Insertion Sort
* Merge Sort
* Quick Sort

These implementations helped me understand sorting techniques, algorithm efficiency, recursion, and different time and space complexity trade-offs.

### ⏱️ Execution Time

I also added code to measure the execution time of Python programs using `time.perf_counter()`.

This helps me compare the practical execution time of different implementations and understand the relationship between code efficiency and algorithm complexity.

### 📚 Data Structures

Implemented basic versions of:

* Stack using Python lists
* Queue using Python lists
* Deque using Python lists

These implementations helped me understand fundamental data structure operations such as:

* Push and Pop
* Enqueue and Dequeue
* Adding and removing elements from both ends

This section is helping me build a stronger foundation in **Data Structures and Algorithms (DSA)** while improving my understanding of how different operations affect performance.

## 🔤 Theory of Computation & DFA

I have also started implementing concepts from **Theory of Computation (TOC)** using Python to better understand how formal languages and automata work in practice.

### Deterministic Finite Automata (DFA)

Implemented Python programs based on DFA concepts, including:

* DFA state transitions
* String validation using DFA
* Pattern recognition
* Accepting and rejecting states
* Regular-language based validation

These implementations help me connect the theoretical concepts of **states, transitions, alphabets, and accepting states** with practical Python programs.

This section will be expanded as I learn more concepts from **Theory of Computation and Automata**.


## 🎯 Purpose

This repository is part of my journey to strengthen my **Python, problem-solving, and software development skills** through hands-on practice.

**Python → Clean Code → Algorithms & Data Structures → Efficiency → Git & GitHub**

More projects and implementations will be added as I continue learning and improving.

> **Learn → Build → Refactor → Understand → Repeat**

