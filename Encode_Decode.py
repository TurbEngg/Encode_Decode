import random
import tkinter as tk

def encode(text, seed):
    # Pad the text
    pad_length1 = random.randrange(5, 25)
    pad_length2 = random.randrange(5, 25)
    padded_text = pad_length1 * "0" + text + pad_length2 * "0"

    random.seed(seed)
    # Encode the padded text
    encoded_text = ''
    for char in padded_text:
        encoded_char = ord(char) + random.randint(0, 94)
        if encoded_char > 126:
            encoded_char -= 94
        encoded_text += chr(encoded_char)

    random.seed(seed+1)
    # Shuffle the encoded text
    encoded_text = [char for char in encoded_text]
    random.shuffle(encoded_text)
    shuffled_text = ''.join(encoded_text)

    return shuffled_text


def decode(encoded_text, seed):
    random.seed(seed+1)

    # Get the original order of characters
    original_order = list(range(len(encoded_text)))
    shuffled_order = original_order[:]
    random.shuffle(shuffled_order)

    # Unshuffle the encoded text
    unshuffled_text = ''.join([encoded_text[shuffled_order.index(i)] for i in original_order])

    random.seed(seed)

    # Decode the unshuffled text
    decoded_text = ''
    for char in unshuffled_text:
        decoded_char = ord(char) - random.randint(0, 94)
        if decoded_char < 32:
            decoded_char += 94
        decoded_text += chr(decoded_char)

    # Strip padding
    return decoded_text.strip("0")

def on_encode_button():
    text = text_entry.get("1.0", tk.END).strip()
    seed = int(seed_entry.get())
    encoded_text = encode(text, seed)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Encoded Text: " + encoded_text)

def on_decode_button():
    text = text_entry.get("1.0", tk.END).strip()
    seed = int(seed_entry.get())
    decoded_text = decode(text, seed)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Decoded Text: " + decoded_text)

root = tk.Tk()
root.title("Text Encoder/Decoder")

# Create a frame with padding
pad_frame = tk.Frame(root, padx=20, pady=15)
pad_frame.pack()

# Text entry
text_label = tk.Label(pad_frame, text="Enter Text:")
text_label.grid(row=0, column=0, sticky="w")
text_entry = tk.Text(pad_frame, width=50, height=5)  # Adjust width and height here
text_entry.grid(row=1, column=0)

# Seed entry
seed_label = tk.Label(pad_frame, text="Enter Seed Number:")
seed_label.grid(row=3, column=0, sticky="w")
seed_entry = tk.Entry(pad_frame, width=30)
seed_entry.grid(row=4, column=0, sticky="w")

# Encode and Decode buttons
button_frame = tk.Frame(pad_frame)
button_frame.grid(row=5, column=0, sticky="w")

encode_button = tk.Button(button_frame, text="Encode", command=on_encode_button)
encode_button.pack(side=tk.LEFT)

decode_button = tk.Button(button_frame, text="Decode", command=on_decode_button)
decode_button.pack(side=tk.LEFT)

# Output text
output_text = tk.Text(pad_frame, height=5, width=50)
output_text.grid(row=6, columnspan=3)

root.mainloop()