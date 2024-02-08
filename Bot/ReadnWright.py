import os

def file_edit(input):
    try:
        with open(input,'r')as input_file:
            content=input_file.read()
        
        print(content)
    except FileNotFoundError:
        print(f"Error: File '{input}' not found.")