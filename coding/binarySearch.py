def binary_search(input_array, value):
    l = len(input_array)-1
    mid = int(l/2)
    count = 0;
    while(count <= l):
        if input_array[mid] > value:
            mid = int((l-mid)/2)
        elif input_array[mid] < value:
            mid = int((l+mid)/2)
        else:
            return "Found at " + str(mid)
        count += 1;
    return "Not Found"

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15

print (binary_search(test_list, test_val1))

print (binary_search(test_list, test_val2))