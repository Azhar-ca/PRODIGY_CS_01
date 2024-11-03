#python
def caesar_cipher(text, shift, mode='encrypt'):
    # Adjust the shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    result = ""
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        # Leave non-alphabetic characters unchanged
        else:
            result += char
    return result

# Get user input
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

# Perform encryption or decryption
if mode == 'encrypt' or mode == 'decrypt':
    result = caesar_cipher(message, shift, mode)
    print(f"The resulting text is: {result}")
else:
    print("Invalid mode! Please type 'encrypt' or 'decrypt'.")
