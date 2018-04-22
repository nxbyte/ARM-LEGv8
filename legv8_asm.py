#!/usr/bin/python3

'''
    File: legv8_asm.py
    Description: A python script to generate machine code for a subset of ARM LEGv8 instructions
    Version: 2 (Tested to work with: LDUR, STUR, ADD, SUB, ORR, AND, CBZ and B instructions)
    How to use:
    1. Run Python script (using Python3)
    2. Input instruction (example: ADD r5, r3, r2) or (example: LDUR x10 [x1, #10])
    3. See the C-interpretation, machine code in binary format and machine code in decimal format
    Developers: Warren Seto and Ralph Quinto
'''

# Get Instruction from keyboard
raw_instruction = input('\nEnter an ARM LEGv8 Assembly Instruction: ')

# Formatting the inputted string for parsing
formatted_instruction = raw_instruction.replace(' ', ',').replace(']', '').replace('[', '')

# Split input into list for parsing
instruction_list = list(filter(None, formatted_instruction.split(',')))

# One-to-one relationship between opcodes and their binary representation
OPCODES = {
    'LDUR' : ['11111000010'],
    'STUR' : ['11111000000'],
    'ADD'  : ['10001011000', '+'],
    'SUB'  : ['11001011000', '-'],
    'ORR'  : ['10101010000', '|'],
    'AND'  : ['10001010000', '&'],
    'CBZ'  : ['10110100'],
    'B'    : ['000101']
}

# [31:0] == [MSB:LSB]
machine_code = OPCODES[instruction_list[0]][0]

print('\n------- C Interpretation -------')

if (instruction_list[0] == 'LDUR' or instruction_list[0] == 'STUR'): # D-Type

    dt_address = 0 if len(instruction_list) < 4 else int(''.join(filter(str.isdigit, instruction_list[3])))

    op = '00'
    rn = int(''.join(filter(str.isdigit, instruction_list[2])))
    rt = int(''.join(filter(str.isdigit, instruction_list[1])))

    if (instruction_list[0] == 'LDUR'): # LDUR
        print('Register[' + str(rt) + '] = RAM[ Register[' + str(rn) + ']' + ('' if len(instruction_list) < 4 else (' + ' + str(dt_address))) + ' ]')
    else: # STUR
        print('RAM[ Register[' + str(rn) + ']' + ('' if len(instruction_list) < 4 else (' + ' + str(dt_address))) + ' ] = Register[' + str(rt) + ']')

    machine_code += str(bin(dt_address)[2:].zfill(9)) + op + str(bin(rn)[2:].zfill(5)) + str(bin(rt)[2:].zfill(5))

elif (instruction_list[0] == 'ADD' or
        instruction_list[0] == 'SUB' or
        instruction_list[0] == 'ORR' or
        instruction_list[0] == 'AND'): # R-Type

    rm = int(''.join(filter(str.isdigit, instruction_list[3])))
    shamt = '000000' # LSL and LSR support has not been added
    rn = int(''.join(filter(str.isdigit, instruction_list[2])))
    rd = int(''.join(filter(str.isdigit, instruction_list[1])))
    print('Register[' + str(rd) + '] = Register[' + str(rn) + '] ' + OPCODES[instruction_list[0]][1] + ' Register[' + str(rm) + ']')

    machine_code += str(bin(rm)[2:].zfill(5)) + shamt + str(bin(rn)[2:].zfill(5)) + str(bin(rd)[2:].zfill(5))

elif (instruction_list[0] == 'B'): # B-Type

    br_address = int(''.join(filter(str.isdigit, instruction_list[1])))
    print('PC = ' + str(br_address))

    machine_code += str(bin(br_address)[2:].zfill(26))

elif (instruction_list[0] == 'CBZ'): # CB-Type

    cond_br_address = int(''.join(filter(str.isdigit, instruction_list[2])))
    rt = int(''.join(filter(str.isdigit, instruction_list[1])))
    print('if ( Register[' + str(rt) + '] == 0 ) { PC = ' + str(cond_br_address) + ' }')
    print('else { PC++ }')

    machine_code += str(bin(cond_br_address)[2:].zfill(19)) + str(bin(rt)[2:].zfill(5))

else:
    raise RuntimeError('OPCODE (' + instruction_list[0] + ') not supported')

# Output the machine code representation of the input
print('\n------- Machine Code (' + str(len(machine_code)) + '-bits) -------')
print('BINARY : ' + machine_code)
print('HEX    : ' + str(hex(int(machine_code, 2)))[2:])
print('')
