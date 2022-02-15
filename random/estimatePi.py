import random

# define a function
def estimate_pi(n):

    # 0 points in circle
    numPointCircle = 0

    # 0 points in total
    numPointTotal = 0

    # n time loop | _ = "i dont care"
    for _ in range(n):

        # random numbers for x and y

        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # if the distance is smaller than 1 => NumPointCircle and numPointTotal + 1
        distance = x**2 + y**2

        if distance <= 1:
            numPointCircle += 1
        numPointTotal += 1

    
    pi = 4 * numPointCircle / numPointTotal
    return pi

result = estimate_pi(10000)
print(result)