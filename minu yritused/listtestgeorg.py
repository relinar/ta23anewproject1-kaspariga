lst = [1, 2, 3, 4, 5, 6]

def is_sorted(lst):
    asc, desc = True, True
    for i in range(len(lst) - 1):
        if [i] < [i + 1]:
            desc = False
        if [i] > [i + 1]:
            asc = False
    return asc or desc

if is_sorted(lst):
    print("list is sorted")
else:
    print("list is not sorted")