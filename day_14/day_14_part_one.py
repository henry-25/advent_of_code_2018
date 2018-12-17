recipes_array = [3, 7]
elf_1_pos = 0
elf_2_pos = 1
num_recipes = 2864801
i = 0

while i < ((num_recipes + 1) * 2):
    sum_curr = recipes_array[elf_1_pos] + recipes_array[elf_2_pos]
    for char in str(sum_curr):
        recipes_array.append(int(char))
    elf_1_pos = (elf_1_pos + 1 + recipes_array[elf_1_pos]) % len(recipes_array)
    elf_2_pos = (elf_2_pos + 1 + recipes_array[elf_2_pos]) % len(recipes_array)
    i += 1


# print(recipes_array[num_recipes:num_recipes + 10])