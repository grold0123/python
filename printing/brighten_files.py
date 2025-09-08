from PIL import Image, ImageEnhance
import os

def brighten_imgs(input_folder,output_folder,factor=1.5):
    '''
    Increase brightness of all images in a folder
    factor > 1.0 -->brighter
    factor < 1.0 -->darker
    '''
    os.makedirs(output_folder,exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png','.jpg','.jpeg')):
            img_path = os.path.join(input_folder,filename)
            img = Image.open(img_path)
            
            enhancer = ImageEnhance.Brightness(img)
            bright_img = enhancer.enhance(factor)
            
            save_path = os.path.join(output_folder,filename)
            bright_img.save(save_path)


input_folder = r"C:\Users\grold\Downloads\br"
output_folder = r"C:\Users\grold\Downloads\brr" 
brighten_imgs(input_folder,output_folder)
