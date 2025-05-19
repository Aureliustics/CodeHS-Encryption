import random
import string

def byte_conversion(input_bytes, PIM, direction): # using bitwise operations to shift bytes
    if direction == 0: # left
        output_bytes = input_bytes << PIM # shift bytes left by pushing zeros in from the right and let the leftmost bits fall off
    elif direction == 1: # right
        output_bytes = input_bytes >> PIM # shift bytes right by pushing zeros in from the left and let the leftmost bits fall off
    return ~output_bytes # byte inversion for further measure

def string_encrypt(text, key):
    encrypted = ''.join([chr((ord(char) ^ key) % 256) for char in text])
    return encrypted

def string_decrypt(encrypted_text, key):
    decrypted = ''.join([chr((ord(char) ^ key) % 256) for char in encrypted_text])
    return decrypted

def xor_encrypt(text, key, bloat_option):
    bloat = "" # nothing by default
    key = byte_conversion(key, len(text), 0) ^ 0xABCDEF # add further encryption by masking the key

    encoded = string_encrypt(text, key)
    if bloat_option.lower() == "y":
        bloat_len = random.randint(len(text) / 2, len(text) * 4) # range padding length to be between half of text size to 4x text size
        bloat = ''.join([random.choice(string.printable) for _ in range(bloat_len)]) # this helps obsecure original message length
    encrypted_message = encoded + bloat
    return encrypted_message, len(text)

def xor_decrypt(encoded_text, key, bloat = 0):
    key = byte_conversion(key, len(encoded_text), 1) ^ 0xABCDEF # undo the key masking
    if bloat > 0: # checks if bloat was used and cuts the bloat accordingly
        encrypted_text = encoded_text[:bloat] # remove bloat if there is any
    else:
        encrypted_text = encoded_text
    decrypted_message = string_decrypt(encrypted_text, key)
    return decrypted_message

def Jicrypt(): # logic for selecting options
    choice = int(input("[Jicrypt]: Encrypt or decrypt? (1 or 2): "))
    if choice == 1:
        text = input("[Jicrypt]: Enter the text you want to encrypt: ")
        key = int(input("[Jicrypt]: Enter a key (as an integer): "))
        bloat_option = str(input("Enable bloat? This can enhance security by obsecuring the length of your message. (Y or N): "))

        encrypted_text, bloat = xor_encrypt(text, key, bloat_option)
        print("Encrypted message:" + repr(encrypted_text)[1:-1])
        if bloat_option.lower() == "y":
            print("[Jicrypt]: Generated bloat (Remember this): " + str(bloat))
        exit_routine = int(input("[Jicrypt]: Run again (1) or exit (2): "))
        if exit_routine == 1:
            print("\n")
            Jicrypt()
        elif exit_routine == 2:
            print("[Jicrypt]: Exitting...")
    elif choice == 2:
        encrypted_text = str(input("Enter encrypted text: "))
        decryption_key = int(input("Enter the key to decrypt the message: "))
        bloat = int(input("Bloat number (0 if none): "))
        
        decrypted_text = xor_decrypt(encrypted_text, decryption_key, bloat)
        
        print("Decrypted message: " + decrypted_text)
        exit_routine = int(input("[Jicrypt]: Run again (1) or exit (2): "))
        if exit_routine == 1:
            print("\n")
            Jicrypt()
        else:
            print("[Jicrypt]: Exitting...")
    else:
        print("[Jicrypt]: Provide a valid option.")
        Jicrypt()

Jicrypt()