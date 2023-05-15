def generate_even_numbers(start, end):
    even_numbers = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


start_num = 4
end_num = 30
even_numbers = generate_even_numbers(start_num, end_num)
print(even_numbers)
