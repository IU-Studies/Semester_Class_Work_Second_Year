section .data
first_name db "Enter first name:- "
middle_name db "Enter middle name:- "
last_name db "Enter last name:- "


section .bss
first_name_input resb 50d
middle_name_input resb 50d
last_name_input resb 50d

section .text
global _start
_start:

%macro print_msg 2
    mov eax, 4
    mov ebx, 1
    mov ecx, %1
    mov edx, %2
    int 80h
%endmacro

%macro read_input 1
    mov eax, 3
    mov ebx, 0
    mov ecx, %1
    mov edx, 51d
    int 80h
%endmacro

_start:
    print_msg first_name, 19
    read_input first_name_input

    print_msg middle_name, 20
    read_input middle_name_input

    print_msg last_name, 18
    read_input last_name_input

    print_msg first_name_input, 50
    print_msg middle_name_input, 50
    print_msg last_name_input, 50

    mov eax, 1
    mov ebx, 0
    int 80h
