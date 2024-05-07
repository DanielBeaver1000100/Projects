import pyperclip
import openpyxl

def print_first_name_from_excel(file_path, column):
    try:
        # Load the Excel workbook
        wb = openpyxl.load_workbook(file_path)
        
        # Select the active worksheet
        ws = wb.active
        
        # Iterate through each row in the specified column and print the first name
        for i, cell in enumerate(ws[column], start=1):
            Title = cell.value
            try:
                First_Name=Title.split()[1] 
                Last_name = Title.split()[2]  # Split the full name and get the 3rd part
                print(f"#{i}: {First_Name , Last_name}")
                pyperclip.copy(Last_name)
                input("Press Enter to continue to the next row...")
            except:
                print("*")
            
    except FileNotFoundError:
        print("File not found.")
    except KeyError:
        print("Invalid column name.")

# Example usage
file_path = r"c:\Users\danie\Desktop\Copy of AllDevices_May2024.xlsx"  # Update this with your file path
column = "D"  # Update this with the column you want to print
print_first_name_from_excel(file_path, column)