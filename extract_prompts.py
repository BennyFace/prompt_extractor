# easily create a list of positive prompts from a folder of stable diffusion images to use as a wildcard for testing.

# pip install pillow
# python extract_prompts.py "inputfolder" "outputfile"

from PIL import Image
import os
import argparse
import sys

parser = argparse.ArgumentParser(description='SRC folder')
parser.add_argument('input_dir', type=str, help='The input directory containing stable diffusion images to process.')
parser.add_argument('text_file_name', type=str, help='name of the text file to generate', default='promptlist.txt')
args = parser.parse_args()

input_dir = args.input_dir
output_file = args.text_file_name

def main():
    with open(output_file, "a") as f:
        for filename in os.listdir(input_dir):
            # Check if the file is a PNG file
            if filename.endswith(".png"):
                # Open the image file
                image_path = os.path.join(input_dir, filename)
                image = Image.open(image_path)

                # Extract the metadata
                metadata = image.info
                # Extract the parameters string
                parameters_str = metadata['parameters']
                # Split the string on 'Negative prompt:' and take the first part
                positive_prompt_raw = parameters_str.split('Negative prompt:')[0].strip()
                positive_prompt= positive_prompt_raw.replace('\n', '')
            
                # Write the metadata to the text file
                f.write(f"{positive_prompt}\n")
                
                # Close the image file
                image.close()


if __name__ == "__main__":
    main()