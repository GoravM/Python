alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    final_text = ""
    for char in start_text:
        
        if char in alphabet:
            position = alphabet.index(char)

            if cipher_direction == "encode":
                new_position = position + shift_amount
            elif cipher_direction == "decode":
                new_position = position - shift_amount

            new_letter = alphabet[new_position]
            final_text += new_letter
        else:
            final_text += char
        
        
    print(f"The {cipher_direction}d text is {final_text}")

End =  False
while not End:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(start_text= text, shift_amount= shift, cipher_direction= direction)
    
    want_end = str(input("Type 'yes' if you want to go again. Otherwise type 'no'. \n"))
    if(want_end == "no"):
        End = True
        print("Goodbye")