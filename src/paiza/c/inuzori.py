first_round = input().split()
second_round = input().split()
first_round_red = int(first_round[0])
first_round_blue = int(first_round[1])
second_round_red = int(second_round[0])
second_round_blue = int(second_round[1])

times = input().split()
times_map = {1: int(times[0]), 2: int(times[1]), 3: int(times[2]), 4: int(times[3])}

if times_map[first_round_red] > times_map[first_round_blue]:
    first_round_winner = first_round_blue
else:
    first_round_winner = first_round_red

if times_map[second_round_red] > times_map[second_round_blue]:
    second_round_winner = second_round_blue
else:
    second_round_winner = second_round_red

times_final = input().split()

if first_round_winner < second_round_winner:
    times_final_map = {first_round_winner: int(times_final[0]), second_round_winner: int(times_final[1])}
else:
    times_final_map = {first_round_winner: int(times_final[1]), second_round_winner: int(times_final[0])}

if times_final_map[first_round_winner] < times_final_map[second_round_winner]:
    print(first_round_winner)
    print(second_round_winner)
else:
    print(second_round_winner)
    print(first_round_winner)
