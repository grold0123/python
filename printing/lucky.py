import os
def record(date,file_name='payments.txt'):
	with open(file_name,'a') as file:
		file.write(f'{date}:P600\n')
def read(file_name='payments.txt'):
	with open(file_name,'r') as file:
		record_dict = {}
		count = 1
		for line in file:
			line = line.strip().split(':')
			record_dict[count] = line[0],line[1] 
			count += 1			
		return record_dict
def remove_all(file_name='payments.txt'):
	with open(file_name,'w') as file:
		pass
def remove_a_record(file_name='payments.txt'):
	display
	records = read()
	choice = int(input('Remove record number: '))
	if choice in records:
		del records[choice]
	else:
		print('No record...')
	print('Record removed.....')
	print()
	with open(file_name,'w') as file:
		for number,record in records.items():
			file.write(record[0],record[1])
def display():
	records = read()
	if len(records) == 0:
		print('No records..')
	
	for number,record in records.items():
		print(str(number)+'.',record[0],record[1])
def total_contributions():
	records = read()
	total = len(records) * 600
	total = 'P '+str(total)
	print('Contributed '+str(len(records))+' times' )
	print('Total contribution is '+total)
def choices():
	print(
		'Press 1: add to record\n'
		'Press 2: show records\n'
		'Press 3: delete all records\n'
		'Press 4: remove a record\n'
		'Press 5: show total number of contributions and total amount\n'
		'Press x: exit\n'
	)

def main():

	while True:
		choices()
		user_choice = input('Choice: ')
		print()
		if user_choice == '1':
			dat_ = input('Date: ')
			print('recording...')
			print()
			record(dat_)
			print()
		elif user_choice == '2': 
			print('displaying records...')
			print()
			display()
			print()
		elif user_choice == '3': 
			print('Deleting records....')
			print()
			remove_all()
			print()
		elif user_choice == '4': 
			remove_a_record()
		elif user_choice == '5': 
			print('Showing number of contributions and total amount.....')
			print()
			total_contributions()
			print()
		elif user_choice == 'x': 
			break

		again = input('Use again, Yes/No: ')
		if again.lower().strip() == 'no':
			break
		os.system('cls')
	os.system('cls')
	print('Closing program....')

if __name__ == '__main__' :
	main()
