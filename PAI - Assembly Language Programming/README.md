
# How to Run and Debug Assembly Programs?

These are the commands that you need to follow in the Ubuntu terminal to run your assembly code.


## The steps are as follows:

**Step 1: Create the Assembly file:-**
```bash
  gedit file_name.asm
```

**Step 2: Assemble the program:-**
```bash
   nasm -f elf64 file_name.asm
```

**Step 3: Link the object file:-**
```bash
    ld file_name.o -o file_name
```

**Step 4: Run the executable:-**
```bash
    ./file_name
```

**Step 5: Debug the program using GDB:-**
```bash
   gdb file_name
```

#### Step 6: These are some of the commands you will need after executing the GDB command (i.e. Step 5 command).

| No. | Command             | Description                                                                                      |
| :-- | :------------------ | :----------------------------------------------------------------------------------------------- |
| 1 | `break _start` | This command sets a breakpoint at the very beginning of the assembly program, allowing you to start debugging from the first instruction. |
| 2 | `run` | This command is used to start the execution of the program under the debugger's control.  |
| 3 | `nexti` | This command is used to step over the next machine instruction when debugging an assembly program. |
| 4   | `x/1xb &variable_name` | This command examines memory at the address of `variable_name`. The `x` command inspects memory, and the `/1xb` option specifies to display 1 byte in hexadecimal format at the address of `variable_name`. |
| 5   | `print/x $register_name` | This command prints the content of a specific CPU register (`register_name`) in hexadecimal format. You can replace `$register_name` with registers like `$eax`, `$ebx`, etc. |
| 6   | `stepi`             | This command steps **into** the next machine instruction, executing it and stopping after that. If the instruction is a function call, `stepi` will enter the function and stop at the first instruction inside the function. |
| 7   | `quit`              | This command exits the `gdb` debugger, terminating the debugging session. |

