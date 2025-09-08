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
		

if __name__ == '__main__':

	tasks = {
		'clr_copy':40,
		'bk_copy':4,
		'clr_copy_1':10,
		'bk_copy_1':10,
		'photo':20,
		'photo_1':20
		}

	display(tasks)
	print('-'*20)
	compute(tasks)
	