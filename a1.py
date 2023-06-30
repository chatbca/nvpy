N = int(input("Enter the number of elements in the list: "))
my_list = []


for i in range(N):
    my_list.append(int(input(f"Enter element {i+1}: ")))


unique_list = []
for element in my_list:
    if my_list.count(element) == 1:
        unique_list.append(element)


print("The unique elements in the list are:", unique_list)
