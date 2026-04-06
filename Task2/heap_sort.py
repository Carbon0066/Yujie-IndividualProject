from heap import MaxHeap 

def heap_sort(arr):
    # step 1: max heap then build heap
    h = MaxHeap()
    h.build_heap(arr)
    result = []

    # step 2: keep removing max
    while len(h.heap) > 0:
        result.insert(0, h.removemax())

    return result


if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    print("Original Example Code:", arr)
    sorted_arr = heap_sort(arr)
    print("Example Code Sorted:", sorted_arr)

    user_input = input("Enter numbers separated by space: ")
    # convert input string to integer list
    arr1 = []
    for x in user_input.split():
        arr1.append(int(x))

    print("You entered:", arr1)
    # call heap sort
    sorted_arr = heap_sort(arr1)
    print("Sorted result:", sorted_arr)
    