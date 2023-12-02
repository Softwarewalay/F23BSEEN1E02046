current_number=0
previous_number=0

for i in range(10):

    current_sum = current_number + previous_number
    print(f'current_number{current_number} previous_number{previous_number}currnt_sum{current_sum}')
    
    previous_number=current_number
    current_number=i+1
