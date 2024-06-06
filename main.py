# Explain CODE in DETAIL


def is_valid_uk_postcode(postcode):
    # Remove leading and trailing whitespace
    postcode = postcode.strip().upper()

    # Define two helper functions to check if a character is a letter or a digit
    def is_letter(char):
        # Check if the character is between 'A' and 'Z'
        return 'A' <= char <= 'Z'
    
    def is_digit(char):
        # Check if the character is between '0' and '9'
        return '0' <= char <= '9'
    
    # Define a function to check if a postcode matches a given format
    def check_format(format_string, postcode):
        # Check if the format string and the postcode have the same length
        if len(format_string) != len(postcode):
            # if not true return false otherwise continue on with code (hence the !=)
            return False
        # Loop through the characters in the format string
        for i in range(len(format_string)):
            # Get the current character (i.e one of the characters) from the format string
            f_char = format_string[i]
            # Get the current character (i.e one of the characters) from the postcode
            p_char = postcode[i]
            # Check if the current character in the format string is a letter and the current character in the postcode is not a letter
            if f_char == 'A' and not is_letter(p_char):
                # if not true return false otherwise continue on with code 
                return False
            if f_char == '9' and not is_digit(p_char):
                # if not true return false otherwise continue on with code 
                return False
            # Check if the current character in the format string is a space and the current character in the postcode is not a space
            if f_char == ' ' and p_char != ' ':
                # if not true return false otherwise continue on with code 
                return False
        # If we get here, it means that all the characters in the format string have been checked and they all match the corresponding characters in the postcode
        return True
    
    # Define a list of valid postcode formats
    formats = [
        "A9 9AA",
        "A9A 9AA",
        "A99 9AA",
        "AA9 9AA",
        "AA9A 9AA",
        "AA99 9AA"
    ]
    
    # Loop through the formats and check if the postcode matches any of them
    for fmt in formats:
        # Call the check_format function to check if the postcode matches the current format
        if check_format(fmt, postcode):
            # if true return true otherwise continue on with code 
            return True
    
    return False

# Ask the user to enter a UK postal code
postcode = input("Enter a UK postal code: ")

# Remove leading and trailing whitespace
postcode = postcode.strip()

# Check if the postcode is valid for the United Kingdom
if is_valid_uk_postcode(postcode):
    # if true print the following statement otherwise continue on with code 
    print(f"The postal code '{postcode}' is valid for the United Kingdom.")
else:
    # if not true print the following statement otherwise continue on with code 
    print(f"The postal code '{postcode}' is not valid for the United Kingdom.")

