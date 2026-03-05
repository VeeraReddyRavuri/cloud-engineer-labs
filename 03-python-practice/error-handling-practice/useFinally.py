def read_file(fileName):

    try:
        with open(fileName, "r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError as e:
        print(f"File not found at the location: {e}")
    except PermissionError as e:
        print(f"Unable to access file: {e}")
    finally:
        print("Script finished")

file_name = input("Enter file name: ")
read_file(file_name)