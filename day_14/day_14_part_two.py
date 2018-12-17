recipes_array = [3, 7]
elf_1_pos = 0
elf_2_pos = 1
num_recipes = 0
i = 0

while True:
    sum_curr = recipes_array[elf_1_pos] + recipes_array[elf_2_pos]
    for char in str(sum_curr):
        recipes_array.append(int(char))
    if(recipes_array[num_recipes:num_recipes + 4] == [8, 6, 4, 8]):
        print(recipes_array[num_recipes:num_recipes + 6])
    if(recipes_array[num_recipes:num_recipes + 6] == [8, 6, 4, 8, 0, 1]):
        print(num_recipes)
        break
    elf_1_pos = (elf_1_pos + 1 + recipes_array[elf_1_pos]) % len(recipes_array)
    elf_2_pos = (elf_2_pos + 1 + recipes_array[elf_2_pos]) % len(recipes_array)
    i += 1
    num_recipes += 1