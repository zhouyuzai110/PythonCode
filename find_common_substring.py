def find_longest_common_substring(strings):
    if not strings:
        return "", []

    # 使用第一个字符串作为初始的共同子字符串
    common_substring = strings[0]

    for string in strings[1:]:
        temp = ""
        for i in range(len(common_substring)):
            for j in range(i + 1, len(common_substring) + 1):
                substring = common_substring[i:j]
                if substring in string and len(substring) > len(temp):
                    temp = substring
        common_substring = temp

    # 找出包含共同子字符串的所有字符串
    matching_strings = [s for s in strings if common_substring in s]

    return common_substring, matching_strings


# 示例数据
strings = ["hello world", "world is beautiful", "beautiful day", "hello again", "goodbye world"]

common_substring, matching_strings = find_longest_common_substring(strings)

print(f"共同的字符串: {common_substring}")
print("包含共同字符串的字符串:")
for s in matching_strings:
    print(s)
