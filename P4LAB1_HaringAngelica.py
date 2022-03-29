user_text = input()

char_to_remove = ' .,!'
char_count = 0
for character in user_text:
    if character not in char_to_remove:
        char_count += 1
print(char_count)
