import sys
from PIL import Image

def remove_iccp_profile(input_file, output_file):
    try:
        with Image.open(input_file) as img:
            # Remove ICC profile if exists
            img.info.pop("icc_profile", None)
            img.save(output_file)
            print(f"iCCP profile removed successfully. Saved to: {output_file}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: rmpngprofile.py -f <input_file>")
        sys.exit(1)
    
    # Parse arguments
    if sys.argv[1] == "-f":
        input_file = sys.argv[2]
        output_file = input_file  # Overwrite the original file
        remove_iccp_profile(input_file, output_file)
    else:
        print("Invalid argument. Use: -f <input_file>")
        sys.exit(1)

if __name__ == "__main__":
    main()
