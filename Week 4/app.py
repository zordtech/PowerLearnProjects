#week 4 assignment

def read_and_modify_file():
    # Ask the user for the input filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Create a new filename for the modified content
        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"File successfully modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read or write this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


read_and_modify_file()