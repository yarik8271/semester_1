from PIL import Image

def run_pillow():
    img = Image.new('RGB', (100, 100), color='red')
    return f'Image Mode: {img.mode}, Size: {img.size}'
