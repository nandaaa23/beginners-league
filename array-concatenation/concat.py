list1=[1,2,3]
list2=[2,4,5]

concatenated_list=list1+list2
print(concatenated_list)

unique_elements_set = set(concatenated_list)

concatenated_without_duplicates = list(unique_elements_set)

print(concatenated_without_duplicates)