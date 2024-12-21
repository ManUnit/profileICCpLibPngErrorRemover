import sys
import os
from PIL import Image

def remove_iccp_profile(input_file, output_file):
    try:
        with Image.open(input_file) as img:
            # Remove ICC profile if exists
            img.info.pop("icc_profile", None)
            img.save(output_file)
            print(f"iCCP profile removed successfully. Saved to: {output_file}")
    except Exception as e:
        print(f"Error processing file {input_file}: {e}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".png"):
                input_file = os.path.join(root, file)
                remove_iccp_profile(input_file, input_file)  # Overwrite the original file

def main():
    if len(sys.argv) < 3:
        print("Usage: rmpngprofile.exe -f <input_file> | -d <directory>")
        sys.exit(1)

    # Parse arguments
    option = sys.argv[1]
    if option == "-f":
        input_file = sys.argv[2]
        output_file = input_file  # Overwrite the original file
        remove_iccp_profile(input_file, output_file)
    elif option == "-d":
        directory = sys.argv[2]
        if not os.path.isdir(directory):
            print(f"Error: {directory} is not a valid directory.")
            sys.exit(1)
        process_directory(directory)
    else:
        print("Invalid argument. Use: -f <input_file> or -d <directory>")
        sys.exit(1)

if __name__ == "__main__":
    main()
 