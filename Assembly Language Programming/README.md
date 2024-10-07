# Steps to Run and Debug Assembly Programs:- 

Note:- Perform this on terminal
- **Step 1 Create the Assembly file:-** gedit file_name.asm
- **Step 2 Assemble the program:-** nasm -f elf64 file_name.asm
- **Step 3 Link the object file:-** ld file_name.o -o file_name
- **Step 4 Run the executable:-** ./file_name
- **Step 5 Debug the program using GDB:-** gdb file_name
