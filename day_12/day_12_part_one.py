no_plant = dict()
plant = dict()
rules = dict()
rules['.'] = no_plant
rules['#'] = plant
plant_pots = ['.' for x in range(201)]
num_generations = 50000000000


with open('input.txt') as input_file:
    for line in input_file:
        if(line[0] == 'i'):
            line = line.split(':')[1].strip()
            i = 10
            for char in line:
                if char == '#':
                    plant_pots[i] = '#'
                i += 1
        elif (line[0] == '.' or line[0] == '#'):
            line = line.split('=>')
            if line[0].strip()[2] == '.':
                rules['.'].update({line[0].strip() : line[1].strip()})
            elif line[0].strip()[2] == '#':
                rules['#'].update({line[0].strip() : line[1].strip()})

i = 0
while i < num_generations:
    print(i)
    updates = ['.' for x in range(201)]
    for a, plant in enumerate(plant_pots):
        constructed_plant_key = ''
        if not a < 2 and not a > 199:
            adjacent_plants = plant_pots[a - 2 : a + 3]
            for entry in adjacent_plants:
                constructed_plant_key += entry
            if plant == '.' and constructed_plant_key in rules['.'].keys():
                updates[a] = rules['.'][constructed_plant_key]
            elif plant == '#' and constructed_plant_key in rules['#'].keys():
                updates[a] = rules['#'][constructed_plant_key]
            else:
                updates[a] = '.'
    plant_pots = updates
    i += 1
        
print(i, ': ', plant_pots)

plants_total = 0
for a, plant in enumerate(plant_pots):
    if plant == '#':
        plants_total += (a - 10)

print(plants_total)