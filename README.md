Here’s a Python program that lets users encrypt and decrypt text using the Caesar Cipher. This code allows users to enter a message and a shift value, specifying whether they want to encrypt or decrypt the message. It’s beginner-friendly and ideal for learning how a simple cipher algorithm works.

Caesar Cipher Python Program:-
The Caesar Cipher is a classic encryption algorithm that shifts each letter in a message by a certain number of places. With this program, you can choose a shift value and apply it to your message for encryption or decryption.

How It Works !
Encrypting: For each letter, the program shifts it forward by the specified amount (wraps around from 'Z' to 'A' for uppercase and 'z' to 'a' for lowercase).
Decrypting: The shift is applied in reverse by negating it.
Input Handling: Non-alphabetic characters remain the same, making it safe for sentences with punctuation and spaces.

example:-
Enter the message: Hello, World!
Enter the shift value: 3
Type 'encrypt' to encrypt or 'decrypt' to decrypt: encrypt
The resulting text is: Khoor, Zruog!
Enter the shift value: 3
Type 'encrypt' to encrypt or 'decrypt' to decrypt: decrypt
The resulting text is: Hello, World!
