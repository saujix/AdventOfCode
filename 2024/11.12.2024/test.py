import sys

# Memoized processing for numbers using dictionary
memo = {}

def process_number(number):
    if number in memo:
        return memo[number]
    
    if int(number) == 0:
        result = [1]
    else:
        number = str(int(number))  # Remove leading zeros
        
        if len(number) % 2 == 0:  # Even-length number
            mid = len(number) // 2
            lefthalf = int(number[:mid])
            righthalf = int(number[mid:])
            result = [lefthalf, righthalf]
        else:
            result = [int(number) * 2024]
    
    memo[number] = result
    return result

def print_progress(iteration, total, bar_length=50):
    progress = int(bar_length * iteration / total)
    bar = '=' * progress + '-' * (bar_length - progress)
    sys.stdout.write(f"\rProgress: [{bar}] {iteration}/{total}")
    sys.stdout.flush()

# Open and read file
with open('input.txt', 'r') as file:
    numbers = file.read().split()

# Process numbers with memoization and progress tracking
total_iterations = 75
number_frequency = {num: numbers.count(num) for num in set(numbers)}  # Count frequency of each number

for current_iteration in range(total_iterations):
    new_frequency = {}
    total_numbers = sum(number_frequency.values())
    
    for idx, (number, freq) in enumerate(number_frequency.items()):
        processed_numbers = process_number(number)
        for processed_number in processed_numbers:
            processed_str = str(processed_number)
            new_frequency[processed_str] = new_frequency.get(processed_str, 0) + freq
        
        print_progress(idx + 1, len(number_frequency))  # Progress for this iteration
    
    number_frequency = new_frequency
    print_progress(current_iteration + 1, total_iterations)  # Overall progress
    print()  # Move to the next line after each iteration

# Count the total occurrences in the final dictionary
count = sum(number_frequency.values())
print(f"\nFinal count: {count}")