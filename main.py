import random
import string

# added base64 as a soft encoding layer. it is applied right before the characters get encrypted with the key. This works as a character shift and also hide the length of original message.
def base64(mode, input_value):  # mode: 1 is encode, 2 is decode
    # replacing the dictionary with a string, prob gonna do smth like loop through each char then calculate the corrisponding b64 value
    base64_code = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" # could prob use string.printable() or smth later

    if mode == 1:
        input_binary = ""
        for i in input_value:
            test_value = bin(ord(i))[2:].zfill(8) # zfill() aka zero fill just adds zeros at the end of a number. zfill(8) so add 8 zeros. bin() converts each ascii to its binary representation. [2:] because when u use bin() it prefixes with 0b so we cut that sghit off. 0b1010101 -> 1010101
            input_binary += test_value

        binary_truncated_value = []
        temp_value = ""
        counter = 1
        for i in input_binary:
            temp_value += i
            if counter % 6 == 0:
                binary_truncated_value.append(temp_value)
                temp_value = ""
            counter += 1
        if counter % 6 != 0:
            while len(temp_value) != 6:
                temp_value = temp_value + "0"
            binary_truncated_value.append(temp_value)

        # basically loop through each value in binary truncated value list, convert the binary string bin_val to a decimal integer with int(bin_val, 2) the 2 means convert to base 2
        # then the for loop will match the converted bin_val (which will be a decimal value now) to the corrisponding value in binary_truncated_value.
        # which all get stored in b64_output as a list
        b64_output = [base64_code[int(bin_val, 2)] for bin_val in binary_truncated_value]

        output_text = ''.join(b64_output) # we dont want it to return a list so convert list form to string form by joining each character
        
        while len(output_text) % 4 != 0:
            output_text += '='

        return output_text
    
    elif mode == 2:
        input_value = input_value.replace("=", "") # remove the "=" padding if there is any
        
        truncated_binary_output = []
        for i in input_value:
            binary_key = bin(base64_code.index(i))[2:] # convert each character to binary form using bin() and cut the binary prefix "0b" using [2:]
            while len(binary_key) != 6:
                binary_key = "0" + binary_key # split into 6 bit chunks and append to truncated_binary_output list
            truncated_binary_output.append(binary_key)
        
        # append each 6 bit binary into binary_source
        binary_source = ""
        for i in truncated_binary_output:
            binary_source += i
    
        # convert binary from 6 bit to 8 bit similar to old logic
        binary_group_output = []
        temp_value = ""
        counter = 1
        for i in binary_source:
            temp_value += i
            if counter % 8 == 0:
                binary_group_output.append(temp_value)
                temp_value = ""
            counter += 1
        if counter % 8 != 0:
            while len(temp_value) != 8:
                temp_value = temp_value + "0"
            binary_group_output.append(temp_value)
    
        # convert each ascii value back into a character with chr() basically it does the inverse of ord()
        output_string = ""
        for i in binary_group_output:
            output_string += chr(int(i, 2))
    
        return output_string

def byte_conversion(input_bytes, amount, direction): # using bitwise operations to shift bytes
    if direction == 0: # left
        output_bytes = input_bytes << amount # shift bytes left by pushing zeros in from the right and let the leftmost bits fall off
    elif direction == 1: # right
        output_bytes = input_bytes >> amount # shift bytes right by pushing zeros in from the left and let the leftmost bits fall off
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
        text = base64(1, str(input("[Jicrypt]: Enter the text you want to encrypt: ")))
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
        
        print("Decrypted message: " + base64(2, str(decrypted_text)))
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