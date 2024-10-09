section .data
num1 db 5 
num2 db 5

section .bss
res1 resb 1

section .text
global _start
_start:

mov al, [num1]
mov bl, [num2]
div bl
mov [res1], al

mov eax, 1
xor ebx, ebx
INT 80h
