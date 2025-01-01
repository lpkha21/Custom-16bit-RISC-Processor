This is the custom made 16 bit processor made in Logisim. Including custom Assembly Language and compiler written in python.
The user can write code in code.txt file and python code generates machine.txt which should be uploaded in the ROM in Logisim.


Usage:
  Write code in code.txt and run compile.sh in terminal. The machine.txt file will be generated which can be uploaded in the ROM.
  

Available Assembly Commands:


- **`LOAD`:** Load a value from memory into a register.  
  Syntax: `LOAD X<reg>, X<memaddr>`  
  Example: `LOAD X1, X10` loads the value at memory address `X10` into register `X1`.

- **`STORE`:** Store a value from a register into memory.  
  Syntax: `STORE X<reg>, X<memaddr>`  
  Example: `STORE X1, X10` stores the value in register `X1` to memory address `X10`.

- **`ADD`:** Add two registers and store the result in a destination register.  
  Syntax: `ADD X<dest>, X<reg1>, X<reg2>`  
  Example: `ADD X1, X2, X3` computes `X2 + X3` and stores the result in `X1`.

- **`SUB`:** Subtract the value of one register from another.  
  Syntax: `SUB X<dest>, X<reg1>, X<reg2>`  
  Example: `SUB X1, X2, X3` computes `X2 - X3` and stores the result in `X1`.

- **`MUL`:** Multiply two registers and store the result in a destination register.  
  Syntax: `MUL X<dest>, X<reg1>, X<reg2>`  
  Example: `MUL X1, X2, X3` computes `X2 * X3` and stores the result in `X1`.

- **`DIV`:** Divide one register by another and store the result in a destination register.  
  Syntax: `DIV X<dest>, X<reg1>, X<reg2>`  
  Example: `DIV X1, X2, X3` computes `X2 / X3` and stores the result in `X1`.

- **`SHIFTL`:** Shift a register value to the left by a specific amount.  
  Syntax: `SHIFTL X<dest>, X<reg>, X<shift>`  
  Example: `SHIFTL X1, X2, X3` shifts the value in `X2` left by the amount in `X3` and stores the result in `X1`.

- **`SHIFTR`:** Shift a register value to the right by a specific amount.  
  Syntax: `SHIFTR X<dest>, X<reg>, X<shift>`  
  Example: `SHIFTR X1, X2, X3` shifts the value in `X2` right by the amount in `X3` and stores the result in `X1`.

- **`NOT`:** Perform a bitwise NOT on a register.  
  Syntax: `NOT X<dest>, X<reg>`  
  Example: `NOT X1, X2` computes the bitwise NOT of `X2` and stores the result in `X1`.

- **`AND`:** Perform a bitwise AND operation between two registers.  
  Syntax: `AND X<dest>, X<reg1>, X<reg2>`  
  Example: `AND X1, X2, X3` computes `X2 & X3` and stores the result in `X1`.

- **`OR`:** Perform a bitwise OR operation between two registers.  
  Syntax: `OR X<dest>, X<reg1>, X<reg2>`  
  Example: `OR X1, X2, X3` computes `X2 | X3` and stores the result in `X1`.

- **`NAND`:** Perform a bitwise NAND operation between two registers.  
  Syntax: `NAND X<dest>, X<reg1>, X<reg2>`  
  Example: `NAND X1, X2, X3` computes `~(X2 & X3)` and stores the result in `X1`.

- **`XOR`:** Perform a bitwise XOR operation between two registers.  
  Syntax: `XOR X<dest>, X<reg1>, X<reg2>`  
  Example: `XOR X1, X2, X3` computes `X2 ^ X3` and stores the result in `X1`.

- **`NOR`:** Perform a bitwise NOR operation between two registers.  
  Syntax: `NOR X<dest>, X<reg1>, X<reg2>`  
  Example: `NOR X1, X2, X3` computes `~(X2 | X3)` and stores the result in `X1`.

- **`JMP`:** Jump to a specific program counter address.  
  Syntax: `JMP X<address>`  
  Example: `JMP X10` jumps to instruction at address `X10`.

- **`BRNE`:** Branch to an address if two registers are not equal.  
  Syntax: `BRNE X<reg1>, X<reg2>, X<address>`  
  Example: `BRNE X1, X2, X10` branches to `X10` if `X1` is not equal to `X2`.

- **`BREQ`:** Branch to an address if two registers are equal.  
  Syntax: `BREQ X<reg1>, X<reg2>, X<address>`  
  Example: `BREQ X1, X2, X10` branches to `X10` if `X1` is equal to `X2`.

- **`LI`:** Load an immediate value into a register.  
  Syntax: `LI X<reg>, <value>`  
  Example: `LI X1, 42` loads the value `42` into `X1`.

- **`MV`:** Move a value from one register to another.  
  Syntax: `MV X<dest>, X<src>`  
  Example: `MV X1, X2` copies the value in `X2` to `X1`.
