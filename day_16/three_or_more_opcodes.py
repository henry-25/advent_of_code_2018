import pprint

def part_one():
    pendingInitialRegisters = None
    pendingOpcodeArray = None
    pendingFinalRegisters = None
    foundOpcodes = set()
    opcodeSets = list()
    opcodeDict = {
        'checkAddr' : set(),
        'checkAddi' : set(),
        'checkMulr' : set(),
        'checkMuli' : set(),
        'checkBanr' : set(),
        'checkBani' : set(),
        'checkBorr' : set(),
        'checkBori' : set(),
        'checkSetr' : set(),
        'checkSeti' : set(),
        'checkGtir' : set(),
        'checkGtri' : set(),
        'checkGtrr' : set(),
        'checkEqir' : set(),
        'checkEqri' : set(),
        'checkEqrr' : set()
    }
    numHighOpcodes = 0
    with open('input_part_one.txt') as input_file:
        for line in input_file:
            line = line.strip()
            #FORMATTING
            if line:
                lineArray = line.split(':')
                if lineArray[0] == 'Before':
                    pendingInitialRegisters = lineArray[1].replace(' ', '').replace('[', '').replace(']', '').split(',')
                    pendingInitialRegisters = [int(i) for i in pendingInitialRegisters]
                elif lineArray[0] == 'After':
                    pendingFinalRegisters = lineArray[1].replace(' ', '').replace('[', '').replace(']', '').split(',')
                    pendingFinalRegisters = [int(i) for i in pendingFinalRegisters]
                else:
                    pendingOpcodeArray = lineArray[0].split(' ')
                    pendingOpcodeArray = [int(i) for i in pendingOpcodeArray]

            #EVALUATING AFTER EVERY THREE LINES
            if pendingInitialRegisters and pendingFinalRegisters and pendingOpcodeArray:
                numOpcodes = 0
                currSetInstructions = set()
                if (checkAddr(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkAddr'].add(pendingOpcodeArray[0])
                if (checkAddi(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkAddi'].add(pendingOpcodeArray[0])
                if (checkMulr(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkMulr'].add(pendingOpcodeArray[0])
                if (checkMuli(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkMuli'].add(pendingOpcodeArray[0])
                if (checkBanr(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkBanr'].add(pendingOpcodeArray[0])
                if (checkBani(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkBani'].add(pendingOpcodeArray[0])
                if (checkBorr(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkBorr'].add(pendingOpcodeArray[0])
                if (checkBori(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkBori'].add(pendingOpcodeArray[0])
                if (checkSetr(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkSetr'].add(pendingOpcodeArray[0])
                if (checkSeti(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkSeti'].add(pendingOpcodeArray[0])
                if (checkGtir(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkGtir'].add(pendingOpcodeArray[0])
                if (checkGtri(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkGtri'].add(pendingOpcodeArray[0])
                if (checkGtrr(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkGtrr'].add(pendingOpcodeArray[0])
                if (checkEqir(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkEqir'].add(pendingOpcodeArray[0])
                if (checkEqri(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkEqri'].add(pendingOpcodeArray[0])
                if (checkEqrr(pendingInitialRegisters, pendingFinalRegisters, pendingOpcodeArray)):
                    numOpcodes += 1
                    opcodeDict['checkEqrr'].add(pendingOpcodeArray[0])
                if numOpcodes > 2:
                    numHighOpcodes += 1
                opcodeSets.append(currSetInstructions)
                # else:
                #     print('Instructions and opcodes \n', pendingInitialRegisters, '\n', pendingOpcodeArray, '\n', pendingFinalRegisters, '\n Num opcodes:', numOpcodes)
                numOpcodes = 0
                pendingInitialRegisters = None
                pendingFinalRegisters = None
                pendingOpcodeArray = None

    while len(foundOpcodes) < 16:
        for key, value in opcodeDict.items():
            if len(value) == 1:
                foundOpcodes.add((key, value.pop()))
        for key, value in opcodeDict.items():
            for i in foundOpcodes:
                if i[1] in value:
                    value.remove(i[1])

    pprint.pprint(foundOpcodes)


def checkAddr(initialRegisters, finalRegisters, opcodeArray):
    return finalRegisters[opcodeArray[3]] == initialRegisters[opcodeArray[1]] + initialRegisters[opcodeArray[2]]
def checkAddi(initialRegisters, finalRegisters, opcodeArray):
    return finalRegisters[opcodeArray[3]] == initialRegisters[opcodeArray[1]] + opcodeArray[2]
def checkMulr(initialRegisters, finalRegisters, opcodeArray):
    return finalRegisters[opcodeArray[3]] == initialRegisters[opcodeArray[1]] * initialRegisters[opcodeArray[2]]
def checkMuli(initialRegisters, finalRegisters, opcodeArray):
    return finalRegisters[opcodeArray[3]] == initialRegisters[opcodeArray[1]] * opcodeArray[2]
def checkBanr(initialRegisters, finalRegisters, opcodeArray):
    return finalRegisters[opcodeArray[3]] == initialRegisters[opcodeArray[1]] & initialRegisters[opcodeArray[2]]
def checkBani(initialRegisters, finalRegisters, opcodeArray):
    return finalRegisters[opcodeArray[3]] == initialRegisters[opcodeArray[1]] & opcodeArray[2]
def checkBorr(initialRegisters, finalRegisters, opcodeArray):
    return finalRegisters[opcodeArray[3]] == initialRegisters[opcodeArray[1]] | initialRegisters[opcodeArray[2]]
def checkBori(initialRegisters, finalRegisters, opcodeArray):
    return finalRegisters[opcodeArray[3]] == initialRegisters[opcodeArray[1]] | opcodeArray[2]
def checkSetr(initialRegisters, finalRegisters, opcodeArray):
    return finalRegisters[opcodeArray[3]] == initialRegisters[opcodeArray[1]]
def checkSeti(initialRegisters, finalRegisters, opcodeArray):
    return finalRegisters[opcodeArray[3]] == opcodeArray[1]
def checkGtir(initialRegisters, finalRegisters, opcodeArray):
    if finalRegisters[opcodeArray[3]] == 1: 
        return opcodeArray[1] > initialRegisters[opcodeArray[2]]
    elif finalRegisters[opcodeArray[3]] == 0:
        return opcodeArray[1] <= initialRegisters[opcodeArray[2]]
    else:
        return False
def checkGtri(initialRegisters, finalRegisters, opcodeArray):
    if finalRegisters[opcodeArray[3]] == 1: 
        return initialRegisters[opcodeArray[1]] > opcodeArray[2]
    elif finalRegisters[opcodeArray[3]] == 0:
        return initialRegisters[opcodeArray[1]] <= opcodeArray[2]
    else:
        return False
def checkGtrr(initialRegisters, finalRegisters, opcodeArray):
    if finalRegisters[opcodeArray[3]] == 1: 
        return initialRegisters[opcodeArray[1]] > initialRegisters[opcodeArray[2]]
    elif finalRegisters[opcodeArray[3]] == 0:
        return initialRegisters[opcodeArray[1]] <= initialRegisters[opcodeArray[2]]
    else:
        return False
def checkEqir(initialRegisters, finalRegisters, opcodeArray):
    if finalRegisters[opcodeArray[3]] == 1:
        return opcodeArray[1] == initialRegisters[opcodeArray[2]]
    elif finalRegisters[opcodeArray[3]] == 0:
        return opcodeArray[1] != initialRegisters[opcodeArray[2]]
    else:
        return False
def checkEqri(initialRegisters, finalRegisters, opcodeArray):
    if finalRegisters[opcodeArray[3]] == 1:
        return initialRegisters[opcodeArray[1]] == opcodeArray[2]
    elif finalRegisters[opcodeArray[3]] == 0:
        return initialRegisters[opcodeArray[1]] != opcodeArray[2]
    else:
        return False
def checkEqrr(initialRegisters, finalRegisters, opcodeArray):
    if finalRegisters[opcodeArray[3]] == 1:
        return initialRegisters[opcodeArray[1]] == initialRegisters[opcodeArray[2]]
    elif finalRegisters[opcodeArray[3]] == 0:
        return initialRegisters[opcodeArray[1]] != initialRegisters[opcodeArray[2]]
    else:
        return False


def part_two():
    instructionDict = {
        11 : evalAddi,
        9 : evalAddr,
        1 : evalBani,
        5 : evalBanr,
        3 : evalBori,
        6 : evalBorr,
        4 : evalEqir,
        0 : evalEqri,
        10 : evalEqrr,
        12 : evalGtir,
        14 : evalGtri,
        13 : evalGtrr,
        7 : evalMuli,
        15 : evalMulr,
        2 : evalSeti,
        8 : evalSetr}

    registers = [0, 0, 0, 0]
    
    with open('input_part_two.txt') as input_file:
        for line in input_file:
            inputInstruction = [int(i) for i in line.strip().split(' ')]
            registers = instructionDict[inputInstruction[0]](registers, inputInstruction)
            print(registers)

def evalAddr(registers, currentInstruction):
    registers[currentInstruction[3]] = registers[currentInstruction[1]] + registers[currentInstruction[2]]
    return registers
def evalAddi(registers, currentInstruction):
    registers[currentInstruction[3]] = registers[currentInstruction[1]] + currentInstruction[2]
    return registers
def evalMulr(registers, currentInstruction):
    registers[currentInstruction[3]] = registers[currentInstruction[1]] * registers[currentInstruction[2]]
    return registers
def evalMuli(registers, currentInstruction):
    registers[currentInstruction[3]] = registers[currentInstruction[1]] * currentInstruction[2]
    return registers
def evalBanr(registers, currentInstruction):
    registers[currentInstruction[3]] = registers[currentInstruction[1]] & registers[currentInstruction[2]]
    return registers
def evalBani(registers, currentInstruction):
    registers[currentInstruction[3]] = registers[currentInstruction[1]] & currentInstruction[2]
    return registers
def evalBorr(registers, currentInstruction):
    registers[currentInstruction[3]] = registers[currentInstruction[1]] | registers[currentInstruction[2]]
    return registers
def evalBori(registers, currentInstruction):
    registers[currentInstruction[3]] = registers[currentInstruction[1]] | currentInstruction[2]
    return registers
def evalSetr(registers, currentInstruction):
    registers[currentInstruction[3]] = registers[currentInstruction[1]]
    return registers
def evalSeti(registers, currentInstruction):
    registers[currentInstruction[3]] = currentInstruction[1]
    return registers
def evalGtir(registers, currentInstruction):
    if currentInstruction[1] > registers[currentInstruction[2]]:
        registers[currentInstruction[3]] = 1
    else:
        registers[currentInstruction[3]] = 0
    return registers
def evalGtri(registers, currentInstruction):
    if registers[currentInstruction[1]] > currentInstruction[2]:
        registers[currentInstruction[3]] = 1
    else:
        registers[currentInstruction[3]] = 0
    return registers
def evalGtrr(registers, currentInstruction):
    if registers[currentInstruction[1]] > registers[currentInstruction[2]]:
        registers[currentInstruction[3]] = 1
    else:
        registers[currentInstruction[3]] = 0
    return registers
def evalEqir(registers, currentInstruction):
    if currentInstruction[1] == registers[currentInstruction[2]]:
        registers[currentInstruction[3]] = 1
    else:
        registers[currentInstruction[3]] = 0
    return registers
def evalEqri(registers, currentInstruction):
    if registers[currentInstruction[1]] == currentInstruction[2]:
        registers[currentInstruction[3]] = 1
    else:
        registers[currentInstruction[3]] = 0
    return registers
def evalEqrr(registers, currentInstruction):
    if registers[currentInstruction[1]] == registers[currentInstruction[2]]:
        registers[currentInstruction[3]] = 1
    else:
        registers[currentInstruction[3]] = 0
    return registers


if __name__ == "__main__":
    part_two()