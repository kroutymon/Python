
# define a function
def shaker(array):

    # left range 0
    left = 0
    #right range of array - 1
    right =  len(array) - 1

    #while left is less or equal to right
    while left <= right:
        #range = left to right
        for i in range(left, right):
            #if pos 1 ist greater than pos 2
            if array[i] > array[i + 1]:
                #
                array[i], array[i + 1] = array[i + 1], array[i]
        right -= 1 

        #opposite 
        for i in range(right, left, - 1):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
        left += 1


array = [40, 29, 190, 10234, 5, 12]
shaker(array)

print(array)