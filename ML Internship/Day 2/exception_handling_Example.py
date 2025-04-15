def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    else:
        print("File read successfully.")
    finally:
        print("Read attempt complete.")

if __name__ == "__main__":
    filename = input("Enter filename: ")
    read_file(filename)
