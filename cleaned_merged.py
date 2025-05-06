with open('mergedlist', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

seen = set()
unique_lines = []
for line in lines:
    if line not in seen:
        seen.add(line)
        unique_lines.append(line)

with open('mergedlist_clean', 'w', encoding='utf-8') as outfile:
    outfile.writelines(unique_lines)
