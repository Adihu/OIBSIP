import random
import string

def generate_password():
    print("=== RANDOM PASSWORD GENERATOR ===")
    try:
        length = int(input("Enter desired password length (minimum 8): "))
        if length < 8:
            print("Error: Password length must be at least 8 characters.")
            return
            
        print("Choose character types to include:")
        inc_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        inc_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        inc_nums = input("Include numbers? (y/n): ").strip().lower() == 'y'
        inc_syms = input("Include symbols? (y/n): ").strip().lower() == 'y'
        
        character_pool = ""
        if inc_upper:
            character_pool += string.ascii_uppercase
        if inc_lower:
            character_pool += string.ascii_lowercase
        if inc_nums:
            character_pool += string.digits
        if inc_syms:
            character_pool += string.punctuation
            
        if not character_pool:
            print("Error: You must select at least one character type.")
            return
            
        password = ''.join(random.choice(character_pool) for _ in range(length))
        print(f"\nGenerated Password: {password}")
        
    except ValueError:
        print("Error: Please enter a valid number for the length.")

if __name__ == "__main__":
    generate_password()