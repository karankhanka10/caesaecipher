alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text_u , shift_u , direction):
    enc = ""
    for i in text_u:
        position = alphabet.index(i)
        if direction == 'encode':
            pos = position + shift_u
            if pos<26:
                new_position = pos
            else:
                new_position = pos % 26
        else:
            pos = position - shift_u
            if pos >= 0:
                new_position = pos
            else:
                new_position = 26 + pos
        enc += alphabet[new_position]
    print(f"The {direction}d text is {enc}")

caesar(text , shift , direction)




