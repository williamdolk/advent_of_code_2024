import nbformat as nbf
from datetime import date
import os

day_number = date.today().day
notebook_filename = f'day_{day_number}.ipynb'
test_input_filename = 'test_input_1.txt'
input_filename = 'input_1.txt'
aoc_day_directory = f'day_{day_number}'

nb = nbf.v4.new_notebook()

nb['cells'] = [
    nbf.v4.new_markdown_cell(f'# Day {day_number}\n## Puzzle 1'),
    nbf.v4.new_code_cell('import numpy as np'),
    nbf.v4.new_code_cell("input_file = 'input_1.txt'\n# input_file = 'test_input_1.txt'"),
    nbf.v4.new_code_cell('with open(file=input_file, mode="r") as file:\n    pass'),
    nbf.v4.new_markdown_cell('## Puzzle 2'),
    nbf.v4.new_code_cell()
]

if not os.path.exists(aoc_day_directory):
    print('Creating directory...')
    os.mkdir(aoc_day_directory)

else:
    print('Directory already exists!')

if not os.path.exists(os.path.join(aoc_day_directory, notebook_filename)):
    print('Creating notebook...')

    with open(os.path.join(aoc_day_directory, notebook_filename), 'w') as f:
        nbf.write(nb, f)

else:
    print('Notebook already exists!')

if not os.path.exists(os.path.join(aoc_day_directory, test_input_filename)):
    print('Creating empty test input file...')

    with open(os.path.join(aoc_day_directory, test_input_filename), 'w') as f:
        f.write('')

else:
    print('Test input file already exists!')

if not os.path.exists(os.path.join(aoc_day_directory, input_filename)):
    print('Creating empty input file...')

    with open(os.path.join(aoc_day_directory, input_filename), 'w') as f:
        f.write('')

else:
    print('Input file already exists!')