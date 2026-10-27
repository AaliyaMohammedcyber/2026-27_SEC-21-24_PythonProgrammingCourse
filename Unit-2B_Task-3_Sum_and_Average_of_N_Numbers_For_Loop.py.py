ttl_input_num= int(input("Enter how many numbers:"))
total_sum= 
for input_index in range(ttl_input_num):
    enterted_number = float(input("Enter a number: "))
    total_sum= total_sum + enterted_number
average = total_sum / ttl_input_num
print(f"Sum = {total_sum}")
print(f"Average = {average}")