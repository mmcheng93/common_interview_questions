import random

def make_key(alpha_num):
    """Make the key from the alphanumeric input."""
    
    alpha_num = list(alpha_num) # Convert the alphanumeric string into a list, with each element comprise containing 1 character
    random.shuffle(alpha_num) # Shuffle the list
    cipher = ''.join(alpha_num) # Create the cipher
    return cipher # Return the cipher

def encrypt(msg, key, alpha_num):
    """Encrypt a message using a key."""
    
    map = dict(zip(alpha_num, key)) # Create a dictionary with the cipher mapped to each alphanumeric character
    encrypted = ''.join(map.get(i) for i in msg) # Substitute each character in the message with the mapped character from the cipher
    return encrypted # Return the encrypted message

def decrypt(cipher, key, alpha_num):
    """Decrypt a message using a key."""
    
    map = dict(zip(key, alpha_num)) # Create a dictionary with each alphanumeric character mapped to the corresponding character in the cipher
    decrypted = ''.join(map.get(i) for i in cipher) # Substitute each character in the cipher with the corresponding alphanumeric character
    return decrypted # Return the decrypted message

if __name__ == "__main__":

    msg = input('Enter a message you want encrypted. ')
    alpha_num = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,;:!()[]{}/\@#$%^&*-+= ' + "'" + '"' # Alphanumeric string
    key = make_key(alpha_num)
    cipher = encrypt(msg, key, alpha_num)
    decrypted = decrypt(cipher, key, alpha_num)
    print(msg)
    print(alpha_num)
    print(key)
    print(cipher)
    print(decrypt(cipher, key, alpha_num))