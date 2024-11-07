section .data
msg1 db 10,15,'Enter valid single digit HEX (0-9, A-F, a-f): '
msg1len equ $-msg1
msg2 db 10,15,'Entered digit is invalid HEX, please reenter single digit valid HEX: '
msg2len equ $-msg2
msg3 db 10,15,'Entered HEX digit is: '
msg3len equ $-msg3
msg4 db 10,15,'Decimal value is: '
msg4len equ $-msg4

section .bss
h1d resb 1          ; Buffer to store user input (1 byte)
decimal resb 1      ; Buffer for storing the decimal result (1 byte)

%macro rw 4
mov eax,%1
mov ebx,%2
mov ecx,%3
mov edx,%4
int 80h
%endmacro

section .text
global _start
_start:

; Prompt user for input
call h1da
call h1dd

; Convert HEX digit to decimal
call hex_to_decimal

; Print the result
call print_decimal

mov eax,1            ; Exit the program
mov ebx,0
int 80h

; Function to display prompt and read user input
h1da:
rw 4,1,msg1,msg1len
up1: rw 3,0,h1d,2  ; Read user input (one byte)
; Validate HEX input
cmp [h1d], byte '0'
jb error
cmp [h1d], byte '9'
jbe convert_digit
cmp [h1d], byte 'A'
jb error
cmp [h1d], byte 'F'
jbe convert_uppercase
cmp [h1d], byte 'a'
jb error
cmp [h1d], byte 'f'
jbe convert_lowercase
error: rw 4,1,msg2,msg2len
jmp up1

convert_lowercase:
    sub [h1d], byte 20h     ; Convert lowercase to uppercase
convert_uppercase:
    sub [h1d], byte 'A' - 10 ; Convert 'A'-'F' to decimal 10-15
    jmp store_decimal

convert_digit:
    sub [h1d], byte '0'      ; Convert '0'-'9' to decimal 0-9
store_decimal:
    mov al, [h1d]            ; Load the value from h1d into register AL
    mov [decimal], al        ; Store the value from AL into decimal
    ret

; Function to display entered HEX digit
h1dd:
rw 4,1,msg3,msg3len
cmp [h1d], byte 9
jbe add30
add [h1d], byte 'A' - 10
add30: add [h1d], byte '0'
rw 4,1,h1d,1                ; Print the entered HEX digit
ret

; Function to print the decimal value
print_decimal:
rw 4,1,msg4,msg4len
mov al, [decimal]           ; Load the decimal value
add al, '0'                 ; Convert it to ASCII
rw 4,1,decimal,1            ; Output the decimal value
ret
