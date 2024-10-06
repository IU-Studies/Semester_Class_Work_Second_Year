section .data
    msg1 db 'Enter a Hex Digit: $'
    msg2 db 0Ah,0Dh, 'In Decimal it is: $'
    hexInput db 10 dup(0)
    decOutput db 10 dup(0)

section .bss
    temp resb 1

section .text
    global _start

_start:
    ; Print the message to enter a hex digit
    mov edx, len msg1
    mov ecx, msg1
    mov ebx, 1
    mov eax, 4
    int 0x80

    ; Read the hex input
    mov eax, 3
    mov ebx, 0
    mov ecx, hexInput
    mov edx, 10
    int 0x80

    ; Convert hex to decimal
    mov esi, hexInput
    xor eax, eax
    xor ebx, ebx
    mov ecx, 16

convert_loop:
    lodsb
    cmp al, 0
    je done
    sub al, '0'
    cmp al, 9
    jbe valid_digit
    sub al, 7
valid_digit:
    imul ebx, ecx
    add ebx, eax
    jmp convert_loop

done:
    ; Convert decimal to string
    mov eax, ebx
    mov edi, decOutput + 9
    mov byte [edi], 0
    dec edi

convert_to_string:
    xor edx, edx
    div ecx
    add dl, '0'
    mov [edi], dl
    dec edi
    test eax, eax
    jnz convert_to_string

    ; Print the decimal output message
    mov edx, len msg2
    mov ecx, msg2
    mov ebx, 1
    mov eax, 4
    int 0x80

    ; Print the decimal output
    mov edx, 10
    mov ecx, edi
    mov ebx, 1
    mov eax, 4
    int 0x80

    ; Exit the program
    mov eax, 1
    xor ebx, ebx
    int 0x80

len equ $ - msg1
