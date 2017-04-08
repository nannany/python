import random


def generate_combination():
    numbers = ""
    for _ in range(10):
        rand_num = random.randint(0, 99)
        if rand_num < 10:
            numbers += "0"
        numbers += str(rand_num)
        if _ != 9:
            numbers += "-"
    return numbers


last_winning = '01-89-05-10-65-27-00-70-16-50'
for i in range(65536):
    random.seed(i)
    x = generate_combination()
    if x == last_winning:
        print(generate_combination())
