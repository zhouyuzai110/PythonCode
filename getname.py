import os

src_folder = r'\\ttnas\homes\zy0612\douyin_download'

# Set to store unique combinations of first and second fields
unique_combinations = set()

# Walk through the source directory
for root, dirs, files in os.walk(src_folder):
    for file in files:
        if '_' in file:  # Ensure the filename contains underscores
            parts = file.split('_', 2)  # Split into parts, at most 2 splits
            if len(parts) >= 2:
                # Take only the first two parts as a tuple and add to the set
                combination = (parts[0], parts[1])
                unique_combinations.add(combination)

# Print the unique combinations
for combo in sorted(unique_combinations):
    print(combo)
