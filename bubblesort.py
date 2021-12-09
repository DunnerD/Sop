# Creating a bubble sort function  
import numpy as np
from random import randint
from timeit import repeat

def bubble_sort(list1, array):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  

  steup_code = f"form_main_import{list}"
  if list != "sorted" else
  stmt = f"{list1}({array})"
times = repeat(setup = setup_code, stmt=stmt, repeat=3, number=10)

list1 = np.random.randint(1,200000,20000)
print("The unsorted list is: ", list)
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(list){min(times)})  