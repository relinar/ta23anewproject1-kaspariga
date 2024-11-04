lst = [1, 6, 3, 4, 5, 6]

def is_sorted(lst):
    asc, desc = True, True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:  # Changed < to > for descending check
            desc = False
        if lst[i] < lst[i + 1]:  # Check for ascending order
            asc = False
    return asc or desc

if is_sorted(lst):  # Call the function with the list
    print("List is sorted")
else:
    print("List is not sorted")
