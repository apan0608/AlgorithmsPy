def sum_two_smallest_numbers(numbers: list):
    smallest = numbers[0]
    smaller = numbers[1]
    for i in range(2, len(numbers)):
        if numbers[i] < smallest:
            if smaller > smallest:
                smaller = smallest
            smallest = numbers[i]         
        elif numbers[i] < smaller:
            smaller = numbers[i]
    print(smaller + smallest)



sum_two_smallest_numbers([5, 8, 12, 18, 22])
    
    # [4, 5, 2, 18])