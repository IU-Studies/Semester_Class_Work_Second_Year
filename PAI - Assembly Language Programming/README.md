
# How to Run and Debug Assembly Programs:- 

These are the commands that you need to follow in the Ubuntu terminal to run your assembly code.




## The steps are as follows:

**Step 1 Create the Assembly file:-**
```bash
  gedit file_name.asm
```

**Step 2 Assemble the program:-**
```bash
   nasm -f elf64 file_name.asm
```

**Step 3 Link the object file:-**
```bash
    ld file_name.o -o file_name
```

**Step 4 Run the executable:-**
```bash
    ./file_name
```

**Step 5 Debug the program using GDB:-**
```bash
   gdb file_name
```

