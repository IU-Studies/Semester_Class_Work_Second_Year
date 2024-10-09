section .data
first_name db "Enter first name:- "
middle_name db "Enter middle name:- "
last_name db "Enter last name:- "

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
MOV EDX, 19
INT 80h

MOV EAX, 3
MOV EBX, 0
MOV ECX, first_name_input
MOV EDX, 51d
INT 80h

MOV EAX, 4
MOV EBX, 1
MOV ECX, middle_name
MOV EDX, 20
INT 80h

MOV EAX, 3
MOV EBX, 0
MOV ECX, middle_name_input
MOV EDX, 51d
INT 80h

MOV EAX, 4
MOV EBX, 1
MOV ECX, last_name
MOV EDX, 18
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
