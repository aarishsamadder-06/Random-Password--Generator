# randpass

A small command-line Python utility to generate random passwords based on user preferences.

## Overview
`randpass.py` prompts the user for desired password length and whether to include uppercase letters, digits, and special characters, then generates a shuffled password that satisfies the selected constraints.

- File: [randpass.py](randpass.py)  
- Main function: [`generate_password`](randpass.py)

## Features
- Customizable length
- Optional inclusion of:
  - Uppercase letters
  - Digits
  - Special characters
- Ensures at least one character from each selected category is present

## Requirements
- Python 3.7+

## Usage
Run from the command line:

```bash
python 