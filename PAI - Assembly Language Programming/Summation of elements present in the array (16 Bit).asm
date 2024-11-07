;8086 ALP to perform array addition. Declare byte type array in the program and store 16 Bit result in 
;memory. Use gdb debugger to execute and check the result. 

section .data
arr1 db 0ffh, 20h, 30h, 40h, 50h
arrlen equ $-arr1

section .bss
sumlb resb 1
sumhb resb 1

section .text
global _start
_start:

mov ebx, arr1
mov cx, arrlen

up1: mov al, [ebx]
add [sumlb], al

jnc down1
inc byte [sumhb]

down1: inc ebx
loop up1

mov eax, 1
mov ebx, 0
int 80h
