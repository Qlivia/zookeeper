initial_atoms = int(input())
final_atoms = int(input())
half_lives = 0

while initial_atoms >= final_atoms:
    initial_atoms /= 2
    half_lives += 1

half_life_length = 12

days = int(half_lives * half_life_length)

print(days)
