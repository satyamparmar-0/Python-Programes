a=["jammu","kasoli","haridwar"]
# try catch and finally block
try:
    print(a[1])
    print(a[3])
except:
    print("an error occured")
finally:
    print("this block is always executed")

# more things related to the exception handling

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print("Result:", result)
    finally:
        print("Execution completed.")

divide(10, 2)
divide(10, 0)

# more things with the exception handling
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: An I/O error occurred.")
    finally:
        print("Finished attempting to read the file.")
