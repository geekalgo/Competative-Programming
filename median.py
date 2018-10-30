def median(numbers):
    numbers = sorted(numbers)
    center = (int) ((len(numbers))/ 2)
    if len(numbers) % 2 == 0:
        print(numbers[center - 1:center + 1])
        return sum(numbers[center - 1:center + 1]) / 2.0
    else:
        return numbers[center]

numbr = [1,2,3,4]
m1=median(numbr)
print(m1)
