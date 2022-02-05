import re

with open("sentences.txt") as input_file, open("output.txt", "w") as output_file:
    for row, line in enumerate(input_file):
        stripped_line = line.strip()
        letter_counts = len(re.findall('[A-Za-z]', stripped_line))
        marks_count = len(re.findall('[,.\\-\'":?!]', stripped_line))
        output_file.write(f"Line: {row + 1}: {stripped_line} ({letter_counts})({marks_count})\n")