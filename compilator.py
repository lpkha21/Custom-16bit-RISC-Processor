def convert_operand(operand):
    operand = operand.upper()

    if operand.startswith('X') and operand[1:].isdigit():
        return int(operand[1:])  
    elif operand.startswith('0X'):  # Hexadecimal immediate value
        return int(operand, 16)  # Convert hexadecimal string to integer
    else:
        raise ValueError(f"Operand '{operand}' format not recognized.")

def compile_assembly_file(input_file, output_file):
    machine_code = {
        'LOAD': '00001',
        'STORE': '00010',
        'ADD': '00011',
        'SUB': '00100',
        'MUL': '00101',
        'SHIFTR': '00110', 
        'DIV': '00111',   
        'SHIFTL': '01000',
        'NOT': '01001',
        'AND': '01010',
        'OR': '01011',
        'NAND': '01100',
        'XOR': '01101',
        'NOR': '01110',
        'JMP': '01111',
        'BRNE': '10000',
        'BREQ': '10001',
        'LI': '10010',
        'MV': '10011'
    }

    with open(input_file, 'r') as f:
        assembly_code = f.read()

    assembly_code = assembly_code.upper()

    total_additional = 0
    line_to_address = {}

    original_lines = assembly_code.strip().split('\n')
    
    # First pass: map original line numbers to addresses considering additional instructions
    for line_number, line in enumerate(original_lines):
        adjusted_line_number = line_number + total_additional
        line_to_address[line_number] = adjusted_line_number
        parts = line.split()
        instr = parts[0].upper()

        if instr in machine_code and instr not in ['LOAD', 'STORE', 'LI', 'BRNE', 'BREQ', 'MV', 'JMP']:
            total_additional += 1  # Each ALU instruction will add an additional MV instruction

    compiled_code = [f"{format(0, '16b')}"]

    # Second pass: compile the code
    for line_number, line in enumerate(original_lines):
        parts = line.split()
        instr = parts[0].upper()
        operands = [operand.upper() for operand in parts[1:]]

        if instr not in machine_code:
            raise ValueError(f"Instruction '{instr}' not supported or defined in machine code.")

        binary_instr = machine_code[instr]

        if instr in ['LOAD', 'STORE']:
            reg = convert_operand(operands[0])
            ramaddr = convert_operand(operands[1])
            binary_code = f"{binary_instr}{format(reg, '03b')}{format(ramaddr, '08b')}"
            compiled_code.append(binary_code)

        elif instr in ['BRNE', 'BREQ']:
            xi = convert_operand(operands[0])
            xj = convert_operand(operands[1])
            PCaddr = line_to_address[convert_operand(operands[2])]
            binary_code = f"{binary_instr}{format(xi, '03b')}{format(xj, '03b')}{format(PCaddr, '05b')}"
            compiled_code.append(binary_code)

        elif instr == 'LI':
            reg = convert_operand(operands[0])
            immediate_value = convert_operand(operands[1])
            if immediate_value < 0 or immediate_value >= (1 << 11):
                raise ValueError(f"Immediate value '{immediate_value}' for LI instruction out of range (0 to 2047).")
            binary_code = f"{binary_instr}{format(reg, '03b')}{format(immediate_value, '08b')}"
            compiled_code.append(binary_code)

        elif instr == 'MV':
            src = convert_operand(operands[0])
            dest = convert_operand(operands[1])
            binary_code = f"{binary_instr}{format(src, '03b')}{format(dest, '03b')}00000"
            compiled_code.append(binary_code)

        elif instr == 'JMP':
            PCaddr = line_to_address[convert_operand(operands[0])]
            binary_code = f"{binary_instr}{format(PCaddr, '011b')}"
            compiled_code.append(binary_code)

        else:  # ALU instructions
            xi = convert_operand(operands[0])
            xj = convert_operand(operands[1])
            xk = convert_operand(operands[2])
            temp_reg = 7  # Using x7 as the temporary register

            # ALU operation x7 = xj OP xk
            binary_code = f"{binary_instr}{format(temp_reg, '03b')}{format(xj, '03b')}{format(xk, '03b')}00"
            compiled_code.append(binary_code)

            # Move the result from x7 to xi
            mv_instr = machine_code['MV']
            mv_code = f"{mv_instr}{format(temp_reg, '03b')}{format(xi, '03b')}00000"
            compiled_code.append(mv_code)

    with open(output_file, 'w') as f:
        for code in compiled_code:
            hex_code = format(int(code, 2), '04X')
            f.write(hex_code + '\n')

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python compile_assembly.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    compile_assembly_file(input_file, output_file)
