import platform
import psutil
import math

# Utility functions for numbers
def find_pi_to_nth_digit(n):
    return f"{math.pi:.{n}f}"

def find_e_to_nth_digit(n):
    return f"{math.e:.{n}f}"

def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def prime_factorization(num):
    factors = []
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors

def next_prime():
    n = 2
    while True:
        if all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
            yield n
        n += 1

# Example functions for computer specs and basic checks
def check_computer_specs():
    print("\nChecking computer specifications...\n")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    
    memory = psutil.virtual_memory()
    print(f"\nTotal RAM: {memory.total / (1024 ** 3):.2f} GB")
    print(f"Available RAM: {memory.available / (1024 ** 3):.2f} GB")
    print(f"Used RAM: {memory.used / (1024 ** 3):.2f} GB")
    
    disk = psutil.disk_usage('/')
    print(f"\nTotal Disk Space: {disk.total / (1024 ** 3):.2f} GB")
    print(f"Used Disk Space: {disk.used / (1024 ** 3):.2f} GB")
    print(f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB")

    print("\nSpecification check completed.")
    input("Press Enter to return to the main menu.\n")

def check_even_odd():
    try:
        num = int(input("Enter a number to check if it is even or odd: "))
        if num % 2 == 0:
            print(f"{num} is even.\n")
        else:
            print(f"{num} is odd.\n")
    except ValueError:
        print("Invalid input. Please enter an integer.\n")

# Menu functions
def show_menu():
    print("Main Menu:")
    print("1. Computer Specifications")
    print("2. Numbers and Calculations")
    print("3. Exit")

def show_numbers_menu():
    print("Numbers and Calculations Menu:")
    print("1. Find PI to the Nth Digit")
    print("2. Find e to the Nth Digit")
    print("3. Fibonacci Sequence")
    print("4. Prime Factorization")
    print("5. Next Prime Number Generator")
    print("6. Back to Main Menu")

# Main function to run the program
def main():
    while True:
        show_menu()
        choice = input("Please select an option (1-3): ")
        
        if choice == '1':
            check_computer_specs()
        elif choice == '2':
            show_numbers_menu()
            num_choice = input("Select a Numbers option (1-6): ")
            if num_choice == '1':
                n = int(input("Enter decimal places for PI: "))
                print("PI to", n, "places:", find_pi_to_nth_digit(n))
            elif num_choice == '2':
                n = int(input("Enter decimal places for e: "))
                print("e to", n, "places:", find_e_to_nth_digit(n))
            elif num_choice == '3':
                n = int(input("Enter number of terms for Fibonacci: "))
                print("Fibonacci sequence:", fibonacci_sequence(n))
            elif num_choice == '4':
                num = int(input("Enter a number for prime factorization: "))
                print("Prime factors:", prime_factorization(num))
            elif num_choice == '5':
                print("Next prime generator. Press Enter for next prime, 'q' to quit.")
                prime_gen = next_prime()
                while input() != 'q':
                    print(next(prime_gen))
            elif num_choice == '6':
                continue
            else:
                print("Invalid option.\n")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    main()
