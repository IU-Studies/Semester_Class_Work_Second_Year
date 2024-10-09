section .data
arr1 db 1,2,3,4,5
arrlen equ $-arr1

section .bss
sumlb resb 1

section .text
global _start
_start:

mov ebx, arr1
mov cx, arrlen

up1: mov al, [ebx]
add [sumlb], al

inc ebx
loop up1

mov eax, 1
mov ebx, 0
int 80h
