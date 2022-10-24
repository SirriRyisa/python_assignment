# Using for loop to print even numbers within the range of 1-30
for even_numbers in range (1, 30):
 if(even_numbers %2) == 0:
  print(even_numbers)
  
  
# Using while loop to print even numbers within the range of 1-30
even_number = 1
while even_number <= 30:
    print(even_number)
    even_number +=1

  
# Using while loop to print odd numbers within the range of 1-30
for odd_numbers in range(1, 30):
  if(odd_numbers %2) == 1:
    print(odd_numbers)
    
# Using while loop to print odd numbers within the range of 1-30

odd_number = 1
while odd_number <= 30:
  print(odd_number)
  odd_number +=1

# Ahmed financial statement
int = 50000
marketing = int*25/100
operations = int*50/100
customer_acquisition = int*25/100
total_num_customer = customer_acquisition/5
print(f"Amount spent on marketing: {marketing}")
print(f"Operation expenses sumed upto: {operations}")
print(f"Custoer acquisition amounted: {customer_acquisition}")
print(f"Number of customers acquired at 5ghc is: {total_num_customer}")