import time
from paint import logo, created_by
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            position = alphabet.index(char.lower())
            new_position = (position + shift_amount) % len(alphabet)
            new_char = alphabet[new_position]
            end_text += new_char.upper() if is_upper else new_char
        else:
            end_text += char
    return end_text

# ANSI escape codes for colors
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

print(f"{RED}{logo}{RESET}")
print(f"\n{YELLOW}{created_by}{RESET}\n")  # Print the created by text in yellow

should_end = False
while not should_end:
    print(f"{GREEN}[?] Select operation module:{RESET}")
    print(f"{GREEN}  [1] Encrypt message{RESET}")
    print(f"{GREEN}  [2] Decrypt message{RESET}")
    
    # Input validation for direction
    while True:
        direction = input(f"\n{GREEN}root@caesar:~# {RESET}")
        if direction in ['1', '2']:
            break
        else:
            print(f"{RED}[!] Invalid syntax. Enter 1 to encrypt or 2 to decrypt.{RESET}")

    text = input(f"\n{GREEN}[?] Enter message to process:\nroot@caesar:~# {RED}")
    print(RESET, end="")
    
    # Input validation for shift
    while True:
        try:
            shift = int(input(f"\n{GREEN}[?] Enter shift key (integer):\nroot@caesar:~# {RESET}"))
            break  # Exit the loop if input is valid
        except ValueError:
            print(f"{RED}[!] Error: Shift key must be a valid integer.{RESET}")

    shift = shift % len(alphabet)  # Normalize the shift value dynamically
    cipher_direction = "encode" if direction == '1' else "decode"
    
    print(f"\n{CYAN}[*] Initializing cipher engine...{RESET}")
    time.sleep(0.5)
    print(f"{CYAN}[*] Executing {cipher_direction} sequence...{RESET}")
    time.sleep(0.7)

    result = caesar(start_text=text, shift_amount=shift, cipher_direction=cipher_direction)
    output_color = RED if cipher_direction == "encode" else YELLOW
    print(f"\n{output_color}[+] OPERATION SUCCESSFUL. Output:\n>>> {result}{RESET}\n")

    restart = input(f"{GREEN}[?] Execute another sequence? (yes/no)\nroot@caesar:~# {RESET}").lower()
    if restart == "no":
        should_end = True
        print(f"{GREEN}[!] Terminating secure connection. Goodbye.{RESET}")