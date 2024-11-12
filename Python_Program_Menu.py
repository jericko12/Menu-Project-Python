import platform
import psutil

def first_program():
    print("\nChecking computer specifications...\n")
    
    # Basic System Information
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    
    # Memory Information
    memory = psutil.virtual_memory()
    print(f"\nTotal RAM: {memory.total / (1024 ** 3):.2f} GB")
    print(f"Available RAM: {memory.available / (1024 ** 3):.2f} GB")
    print(f"Used RAM: {memory.used / (1024 ** 3):.2f} GB")
    
    # Disk Information
    disk = psutil.disk_usage('/')
    print(f"\nTotal Disk Space: {disk.total / (1024 ** 3):.2f} GB")
    print(f"Used Disk Space: {disk.used / (1024 ** 3):.2f} GB")
    print(f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB")

    # CPU Information
    print(f"\nNumber of CPUs: {psutil.cpu_count(logical=True)}")
    print(f"CPU Frequency: {psutil.cpu_freq().current:.2f} MHz")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")

    print("\nSpecification check completed.")
    input("Press Enter to return to the main menu.\n")


def second_program():
    print("\nYou are now in the Second Program.")
    # Example functionality: Check if a number is even or odd
    num = int(input("Enter a number to check if it is even or odd: "))
    if num % 2 == 0:
        print(f"{num} is even.\n")
    else:
        print(f"{num} is odd.\n")


def show_menu():
    print("Menu:")
    print("1. Check Computer Specifications")
    print("2. Second Program")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Please select an option (1-3): ")

        if choice == '1':
            first_program()
        elif choice == '2':
            second_program()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")


if __name__ == "__main__":
    main()
