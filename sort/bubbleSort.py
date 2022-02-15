def sort(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(i):

            # Wenn Position 1 größer ist als Position 2 -> swap
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j +1]
                numbers[j + 1] = temp


# Array
numbers = [5, 3, 8, 6, 7, 2]

# recall function just with numbers
sort(numbers)

print(numbers)


