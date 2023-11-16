import sys
from PIL import Image, ImageOps

valid_extensions = ['.jpg', '.jpeg', '.png']

def check_sys():
    match [len(sys.argv) < 3, len(sys.argv) == 3]:
        case [False, False]:
            sys.exit ('Too many comand-line arguments')
        case [True, False]:
            sys.exit ('Too few comand-line arguments')
        case [False, True]:
            return True

if check_sys() is True:
    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    if (not input_image_path.lower().endswith(tuple(valid_extensions)) or not output_image_path.lower().endswith(tuple(valid_extensions))):
        sys.exit("Invalid extension")
    elif input_image_path.lower()[-4:] != output_image_path.lower()[-4:]:
        sys.exit("Output file extension must match the input file extension")
    else:
        try:
            Image.open(input_image_path)
        except FileNotFoundError:
            print("Input image not found.")
            sys.exit(1)
        else:
            shirt = Image.open("shirt.png")
            input_image = Image.open(input_image_path)
            input_size = input_image.size
            input_image = ImageOps.fit(input_image, size=shirt.size)
            input_image.paste(shirt, (0, 0), shirt)
            input_image.save(output_image_path)
