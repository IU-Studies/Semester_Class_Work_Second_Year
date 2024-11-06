section .data
first_name db "Enter first name:- "
msg1len equ $-first_name
middle_name db "Enter middle name:- "
msg2len equ $-middle_name
last_name db "Enter last name:- "
msg3len equ $-last_name

section .bss
first_name_input resb 51
middle_name_input resb 51
last_name_input resb 51

section .text
global _start
_start:

MOV EAX, 4
MOV EBX, 1
MOV ECX, first_name
MOV EDX, msg1len
INT 80h

MOV EAX, 3
MOV EBX, 0
MOV ECX, first_name_input
MOV EDX, 51d
INT 80h

MOV EAX, 4
MOV EBX, 1
MOV ECX, middle_name
MOV EDX, msg2len
INT 80h

MOV EAX, 3
MOV EBX, 0
MOV ECX, middle_name_input
MOV EDX, 51d
INT 80h

MOV EAX, 4
MOV EBX, 1
MOV ECX, last_name
MOV EDX, msg3len
INT 80h

MOV EAX, 3
MOV EBX, 0
MOV ECX, last_name_input
MOV EDX, 51d
INT 80h

MOV EAX, 4
MOV EBX, 1           
MOV ECX, first_name_input
MOV EDX, 51           
INT 80h

MOV EAX, 4           
MOV EBX, 1           
MOV ECX, middle_name_input  
MOV EDX, 51           
INT 80h

MOV EAX, 4           
MOV EBX, 1           
MOV ECX, last_name_input    
MOV EDX, 51
INT 80h

MOV eax, 1
MOV ebx, 0
int 80h
