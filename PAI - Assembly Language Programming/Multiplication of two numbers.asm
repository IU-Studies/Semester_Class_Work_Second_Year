;8086 ALP to perform multiplication of 2, 8 Bit numbers stored in memory, store your result in memory. 
;Use gdb debugger to execute and check the result. 

section .data
num1 db 15 
num2 db 3

section .bss
res1 resb 1

section .text
global _start
_start:

mov al, [num1]
mov bl, [num2]
mul bl
mov [res1], al

mov eax, 1
xor ebx, ebx
INT 80h
