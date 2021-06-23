import time

count_odd_number = 0
count_even_numbers = 0
sum_odd_number = 0
sum_even_number = 0
n = 0
try:
    for number in range(0,10):
        n = int(input("Number:"))
        if n % 2 == 0:
            if n == 0:
                sum_even_number = sum_even_number
                count_even_numbers += 0
            else:
                sum_even_number += n
                count_even_numbers += 1
        elif n % 2 !=0:
            sum_odd_number += n
            count_odd_number += 1
    print(f"""
    {count_odd_number} Single numbers available.
    Sum of odd numbers --->{sum_odd_number} 
    Average of odd numbers --->{sum_odd_number / count_odd_number}
    *************************************************************
    {count_even_numbers} Even numbers available.
    Sum of even numbers--->{sum_even_number}
    Average of even numbers--->{sum_even_number / count_even_numbers}
    """)
except ValueError:
    print("Please enter an integer.")
    print("The program is closing ")
    time.sleep(5)
except ZeroDivisionError:
    print("Please enter at least one of the even and odd numbers")
    print("The program is closing ")
    time.sleep(5)

