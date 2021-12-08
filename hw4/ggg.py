lst = [1, 3, 6, 9, 12, 13, 17, 20]
new_lst = [el for el in lst if el > lst[lst.index(el)-1]]
print(new_lst)