section .data
msg1 db "Welcome"
msg1len equ $-msg1

section .bss

section .text
global _start
_start:

MOV EAX, 4
MOV EBX, 1
MOV ECX, msg1
MOV EDX, msg1len
INT 80h

MOV eax, 1
MOV ebx, 0
int 80h
