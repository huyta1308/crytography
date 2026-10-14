char_start_in = ord('A')
char_end_in = ord('Z')

r = char_end_in - char_start_in +1

encrypted = 'AIIX'
for key_index in range(-r + 1, r + 1):
    print(f'Key = {key_index}   ', end = '')
    for c in range(len(encrypted)):
        if ord(encrypted[c]) + key_index < ord('A'):
            print(chr(ord(encrypted[c]) + key_index + r), end = '')
        elif ord(encrypted[c]) + key_index > ord('Z'):
            print(chr(ord(encrypted[c]) + key_index - r), end = '')
        else:
            print(chr(ord(encrypted[c]) + key_index), end = '')
    print()