# Check Banr
initialRegisters = [0, 3, 3, 3]
opcodeArray = [14, 3, 1, 2]
finalRegisters = [0, 3, 1, 3]

print('Register A:', initialRegisters[opcodeArray[1]])
print('Register B:', initialRegisters[opcodeArray[2]])
print('Register C:', finalRegisters[opcodeArray[3]])

print(finalRegisters[opcodeArray[3]] == initialRegisters[opcodeArray[1]] & initialRegisters[opcodeArray[2]])