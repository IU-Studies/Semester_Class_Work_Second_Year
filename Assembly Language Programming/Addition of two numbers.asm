section .data
num1 db 20h ;
num2 db 2h

section .bss
res1 resb 1

section .text
global _start
_start:

mov al, [num1]
add al, [num2]
mov [res1], al

mov eax, 1
mov ebx, 0
INT 80h
