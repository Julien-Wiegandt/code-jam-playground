import random
import time

# Get an random int array
def random_array(n=20,min=-100, max=100):
    array = []
    for i in range(random.randint(0, n)):
        array.append(random.randint(min, max))
    return array

# ----- Secondary function ----- #
def swap (array, one, second):
    temp = array[one]
    array[one] = array[second]
    array[second] = temp

def get_max(array):
    if(len(array)>0):
        max=array[0]
        for i in array:
            if(i > max):
                max = i
        return max

# Worse case : O(n*k) where k the maximum number of digits in a number.
def get_transform_array_and_max(array):
    new_array = []
    if(len(array)>0):
        max=array[0]
        for i in array:
            if(i > max):
                max = i
            figure = [i]
            for j in range(len(str(i))-1, -1, -1):
                figure.append(int(str(i)[j]))
            new_array.append(figure)
    return (new_array, max)

def custom_counting_sort(array, index):
    sorted_array = []
    if(len(array)>0):
        max = 11
        count_array = [[] for i in range(max)]
        for item in array:#O(n)
            if(len(item)-index-2 < 0):
                count_array[0].append(item)
            else:
                count_array[item[index+1]+1].append(item)
        for i in range(max): #O(11)
            if(len(count_array[i])>0):
                sorted_array += count_array[i]
    return sorted_array

# Worst Case: O(n^2)
# Average Case: O(n*logn)
# Best case: O(n*logn)
def insertion_sort(array, desc=False):
    sortedArray = []
    for number in array:
        if(len(sortedArray) == 0):
            sortedArray.append(number)
        else:
            for j in range(0,len(sortedArray)):
                if(sortedArray[j] > number and not(desc)):
                    sortedArray.insert(j, number)
                    break
                elif(sortedArray[j] < number and desc):
                    sortedArray.insert(j, number)
                    break
                elif(j == len(sortedArray)-1):
                    sortedArray.append(number)
                    
    return sortedArray

# Worst Case: O(n^2)
# Average Case: O(n*logn)
# Best case: O(n*logn)
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if(array[j] > array[j+1]):
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp

# Worst Case: O(n^2)
# Average Case: O(n*logn)
# Best case: O(n*logn)
def selection_sort(array):
    sortedArray = []
    while(len(array)>0):
        min = array[0]
        for number in array:
            if(number < min):
                min = number
        sortedArray.append(min)
        array.remove(min)
    array = sortedArray

# Worst Case: O(n^2)
# Average Case: O(n*logn)
# Best case: O(n*logn)
def quick_sort(array, start, end):
    if(start<end):
        # Choose the pivot value
        min = (array[start], start)
        mid = (array[start], start)
        max = (array[start], start)
        for i in [(array[int(end/2)],int(end/2)), (array[end], end)]: # O(1)
            if(i[0] > max[0]):
                max = i
            elif(i[0] < min[0]):
                min = i
            else:
                mid = i
        pivot = mid[0]
        swap(array, mid[1], end)

        # Sort by the pivot
        j = start
        for i in range(start, end):
            if(array[i] < pivot):
                swap(array, i, j)
                j += 1
        swap(array, j, end)
        quick_sort(array, start, j)
        quick_sort(array, j+1, end)

# Worst Case: O(n*logn)
# Average Case: O(n*logn)
# Best case: O(n*logn)
def merge_sort(array):
    length = len(array)
    if(len(array)>1):
        mid = int((length/2))
        array1 = array[0:mid]
        array2 = array[mid: length]
        merge_sort(array1)
        merge_sort(array2)

        # Merge the arrays
        i = j = k = 0
        while(i<len(array1) and j<len(array2)):
            if(array1[i] < array2[j]):
                array[k] = array1[i]
                i += 1
            else:
                array[k] = array2[j]
                j += 1
            k += 1
        
        # Add the possible missing items
        while i < len(array1):
            array[k] = array1[i]
            i += 1
            k += 1
        
        while j < len(array2):
            array[k] = array2[j]
            j += 1
            k += 1


        if(array1[0] < array2[0]):
            array = array1 + array2
        else:
            array = array2 + array1

# Worst Case: O(n+k), where n is the size of input array and k is the count of unique elements in the array
def counting_sort(array):
    sorted_array = []
    if(len(array)>0):
        max = get_max(array)
        count_array = [0] * (max+1)
        for item in array:
            count_array[item] = count_array[item] + 1
        for i in range(max+1):
            if(count_array[i]>0):
                temp = [i] * count_array[i]
                sorted_array += temp
    return sorted_array


# Worst Case : O(nk) where k is the maximum number of digits in a number.
def radix_sort(array):
    if(len(array)>0):
        (new_array, max) = get_transform_array_and_max(array) #O(n)
        numbers = len(str(max))
        for i in range(numbers):#O(n*numbers)
            new_array = custom_counting_sort(new_array, i)
        res = []
        for item in new_array:#0(n)
            res.append(item[0])
        return res


array = random_array(n=20000,min=0, max=100)
print("for n = ",len(array))
begin = time.process_time()
insertion_sort(array)
end = time.process_time()
print("insertion_sort exec time : ",end-begin)

begin = time.process_time()
bubble_sort(array)
end = time.process_time()
print("bubble_sort exec time : ",end-begin)

begin = time.process_time()
selection_sort(array)
end = time.process_time()
print("selection_sort exec time : ",end-begin)

begin = time.process_time()
quick_sort(array, 0, len(array)-1)
end = time.process_time()
print("quick_sort exec time : ",end-begin)

begin = time.process_time()
merge_sort(array)
end = time.process_time()
print("merge_sort exec time : ",end-begin)

begin = time.process_time()
counting_sort(array)
end = time.process_time()
print("counting_sort exec time : ",end-begin)

begin = time.process_time()
radix_sort(array)
end = time.process_time()
print("radix_sort exec time : ",end-begin)