Welcome

HOW TO USE:
Running the script should generate a popup window with 3 fields and 2 buttons. 
Enter the text you would like to encode or decode into the first window,
enter your encrytpion seed (a string of numbers of any length ie. 173273618728361623),
then hit either 'Encode' or 'Decode'.

ENCRYTPION DETAILS:
The app randomly alters the length of the message with padding to prevent people from being able to guess the contents based on length.
The padding and contents are assigned random random letters or symbols then randomly shuffled. This means that the encrytpion cant be cracked using letter frequencies etc.
Decryption does the same in reverse. the key is used to set the random.seed() to allow repeatable results.

I may be wrong but i believe that unless they have the key and this software, a message encoded by this app is impossible to decode as it contains no information from the original message. 
The only volnerability that i can see is someone who has the software could brute force the seed so i advise making your seeds very long.
