# Menu information function
def get_menu_choice():
    print('''
*** Menu ***

1. Encrypt string
2. Decrypt string
3. Brute force decryption
4. Quit
    ''')
    command_list = [1, 2, 3, 4]

    # Prompt for and read command input choice from user
    command = int(input("What would you like to do [1,2,3,4]? "))

    # Validate user's input
    while command not in command_list:
        print("Invalid choice, please enter either 1, 2, 3 or 4.")
        print()
        command = int(input("What would you like to do [1,2,3,4]? "))
    print()
    return command

# Offset information function
def get_offset():
    offset = int(input("Please enter offset value (1 to 94): "))
    
    # Prompt for and read, and validate offset input choice from user
    while offset not in range(1,95):
        offset = int(input("Please enter offset value (1 to 94): "))
    return offset
 

# Encrypt/ Decrypt string function
def translate_string(the_string, offset):
    
    # If user's choice is to encrypt string
    if command == 1:
            
        # Create a list to store encrypted character from the string
        encrypted_char_list = []
        
        # Encrypt the string by running through every character in the string 
        for char in the_string:
            
            # Find the ASCII value of each character in the string, and each encrypted character's ASCII value for offset points
            char_point = ord(char)
            char_offset_point = char_point + offset
            
            # If the offset point is beyond 126, wrap back to the beginning of ASCII table by subtracting total number of characters (95)
            # Otherwise, if the offset point is less than 32, add 95 to it
            if char_offset_point > 126:
                char_offset_point -= 95
            elif char_offset_point < 32:
                char_offset_point += 95
                
            # Find the ASCII encrypted character through its ASCII value
            encrypted_char = chr(char_offset_point)
            
            # Add the encrypted character to the encrypted character list
            encrypted_char_list.append(encrypted_char)
            
        # Display the encrypted string
        print()
        print("Encrypted string:")
        
        # Creat an empty encrypted string to store the encrypted string
        encrypted_string = ''
        
        # Find the encrypted string by running through each character in the encrypted character list
        for char in encrypted_char_list:
            encrypted_string += char
        print(encrypted_string)

    # If user's choice is to encrypt string# If user's choice is to encrypt string
    elif command == 2:
        
        # Create a list to store decrypted character from the string
        decrypted_char_list = []
        offset = - offset
            
        # Decrypt the string by running through every character in the string 
        for char in the_string:
            
            # Find the ASCII value of each character in the string, and each decrypted character's ASCII value for offset points
            char_point = ord(char)
            char_offset_point = char_point + offset
            
            # If the offset point is beyond 126, wrap back to the beginning of ASCII table by subtracting total number of characters (95)
            # Otherwise, if the offset point is less than 32, add 95 to it
            if char_offset_point > 126:
                char_offset_point -= 95
            elif char_offset_point < 32:
                char_offset_point += 95
                
            # Find the ASCII decrypted character through its ASCII value
            decrypted_char = chr(char_offset_point)
            
            # Add the decrypted character to the decrypted character list
            decrypted_char_list.append(decrypted_char)
            
        # Display the decrypted string
        print()
        print("Decrypted string:")
        
        # Creat an empty decrypted string to store the decrypted string
        decrypted_string = ''
        
        # Find the decrypted string by running through each character in the decrypted character list
        for char in decrypted_char_list:
            decrypted_string += char
        print(decrypted_string)
        
        
    # If user's choice is to have brute-force decryption    
    elif command == 3:
        
        # Create a list to store decrypted character from the string
        brute_force_char_list = []
        
        # Decrypt the string by running through every character in the string
        for offset in range(1,95):
            for char in the_string:
                
                # Find the ASCII value of each character in the string, and each decrypted character's ASCII value for offset points
                char_point = ord(char)
                char_offset_point = char_point - offset
                
                # If the offset point is beyond 126, wrap back to the beginning of ASCII table by subtracting total number of characters (95)
                # Otherwise, if the offset point is less than 32, add 95 to it
                if char_offset_point > 126:
                    char_offset_point -= 95
                elif char_offset_point < 32:
                    char_offset_point += 95
                    
                # Find the ASCII decrypted character through its ASCII value
                brute_force_char = chr(char_offset_point)
                
                # Add the decrypted character to the decrypted character list
                brute_force_char_list.append(brute_force_char)
                
            # Display the decrypted string
            print("Offset:", offset, "= Decrypted string: ", end= '')
            
            # Creat an index and empty decrypted string to store the decrypted string
            decrypted_string = ''
            
            # Find the decrypted string by running through each character in the decrypted brute-force character list
            for char in brute_force_char_list:
                decrypted_string += char
            print(decrypted_string)
            
            # Update the list which stores decrypted character from the string to an empty list, so that
            # the for loop can store the new characters decrypted from other offsets
            brute_force_char_list = []

    return (the_string, offset)

# Display menu, prompt for and read user's input
command = get_menu_choice()

# If user wants to encrypt or decrypt a string
while command != 4:
    if command == 1 or command == 2:
        
        # If user wants to encrypt a string
        if command == 1:
            the_string = input("Please enter string to encrypt: ")
            
        # If user wants to decrypt a string
        elif command == 2:
            the_string = input("Please enter string to decrypt: ")
            
        # Prompt for and read user's offset input
        offset = get_offset()
        
        # Encrypt or decrypt a string according to user's choice
        translate_string(the_string, offset)         
    
    # If user's choice is to brute-force decrypt a string
    elif command == 3:
        the_string = input("Please enter string to decrypt: ")
        translate_string(the_string, offset)
        
    # Display menu, prompt for and read user's input
    command = get_menu_choice()
            
# If user wants to quit the program   
if command == 4:
    print("Goodbye.")

