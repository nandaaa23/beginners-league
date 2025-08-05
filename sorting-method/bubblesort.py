def bubble_sort(activity_list):
    n=len(activity_list)

    for i in range(n):
        for j in range(0,n-i-1):
            if len(activity_list[j]) > len(activity_list[j+1]):
                activity_list[j], activity_list[j+1] = activity_list[j+1], activity_list[j]
    return activity_list


list=['sleeping','eating','bsing','studying','bathing']
sorted_list=bubble_sort(list)

print(sorted_list)