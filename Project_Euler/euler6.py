def sum_of_squares(n):
    sum = 0
    for i in range(1,n+1):
        sq = i ** 2
        sum = sum + sq
    return sum
def square_of_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum ** 2

print(square_of_sum(100) - sum_of_squares(100))
