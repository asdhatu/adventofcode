import re

# For Advent of Code Day 1
# Takes a file of lines and reformats them to find the calibration value
# Calibration values are here the first and last numbers to appear in every line, placed in the 10's and 1's digits.
def remove_non_numeric(input_file_path, output_file_path):
    # Open the input file in read mode and the output file in write mode
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        # Iterate over each line in the input file
        for line in input_file:
            # Use regular expression to remove non-numeric characters
            cleaned_line = re.sub(r'\D', '', line)
            # Write the cleaned line to the output file
            output_file.write(cleaned_line + '\n')

def process_line(line):
    # Check if the line is empty or if it consists only of spaces
    if not line or len(line) == 0:
        return '00'  # Return '00' or another placeholder that indicates an invalid line
    # Prepare the first and last characters, checking if they are numeric
    first_char = line[0] if line[0].isdigit() else ''
    last_char = line[-1] if line[-1].isdigit() else ''
    # Combine the first character, cleaned middle part, and last character
    return first_char + last_char

def transform_file(input_file_path):
    # Declare empty sum variable
    summ = 0
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            # Strip newline characters for processing and add them back for output
            cleaned_line = process_line(line.strip())
            summ += int(cleaned_line)
    return summ
            
# Example usage
input_file_path = 'input_file.txt'
output_file_path = 'output_file.txt'
remove_non_numeric(input_file_path, output_file_path)
print(transform_file(output_file_path))
