def compute(dictionary): 
	sum_tasks = sum([value for key,value in dictionary.items()])
	space_count = 20 - len(str(sum_tasks)) - len('total:')
	spaces = space_count * ' '
	text = 'Total '+ spaces + str(sum_tasks)
	print(text)	
def display(dictionary):
	print()
	header_text = ''
	dividing_space_count = 20 - len('items')  - len('amount')
	header_text = 'items'+dividing_space_count*' '+'amount'
	print(header_text)
	text = ''
	for name,amount in dictionary.items():
		text = ''
		dividing_space_count = 20 - len(name)  - len(str(amount))
		text += name+dividing_space_count*' '+str(amount)
		print(text)
def convert_to_pdf():
    from pathlib import Path
    from PIL import Image
    dir = Path(r'C:\Users\grold\Downloads')
    image_folder = dir/'images'
    
    image_paths = sorted(image_folder.rglob('*.jpg'))
    for path in image_paths:
        print(path.name)
    images = []
    for file in image_paths:
        img = Image.open(file)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        images.append(img)

    output_pdf = image_folder/"merged.pdf"
    # First image is the base, others are appended
    if images:
        images[0].save(
            output_pdf,
            save_all=True,
            append_images=images[1:]
        )
        print("Saved as merged.pdf")
    else:
        print(f"No .jpg files found in {image_folder}")
    
    
    
                
if __name__ == '__main__':

	convert_to_pdf()

