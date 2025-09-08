def display_all(items:dict):
    print('*'*20)
    for date,tasks in items.items():
        print('---'+date+'---')
        date_sale_total = 0
        for task_number,tasks_items in tasks.items():
            task_number_total = 0
            for job,price in tasks_items.items():
                margin = 20-len(job)
                print(job,f'{price:>{margin}}')
                task_number_total += price 
            print('-'*20)
            margin = 20-len('total:')
            print('total:',f'{task_number_total:>{margin}}')
            print()
            date_sale_total += task_number_total
        print('Total for',date,'is',date_sale_total)

def display_sales(items:dict,date:str):
    print('---'+date+'---')
    total = 0
    for item,price in items[date].items():
        margin = 20-len(item)
        print(item,f'{price:>{margin}}')
        total += price 
    print('-'*20)
    margin = 20-len('total:')

    print('total:',f'{total:>{margin}}')
    print()

def export_txt(items):
    pass