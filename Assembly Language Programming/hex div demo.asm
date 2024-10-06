section .data
msg1 db 10,15,'Enter valid single digit HEX (0-9, A-F, a-f)'
msg1len equ $-msg1
msg2 db 10,15,'Enter digit is invalid HEX, please reenter single digit valid HEX'
msg2len equ $-msg2
msg3 db 10,15,'Entered HEX digit is '
msg3len equ $-msg3

section .bss
h1d resb 1

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

mov bl, 10
rw 4,1,msg1,msg1len
rw 3,0,h1d,2

cmp [h1d], byte '0'
jb error
cmp [h1d], byte '9'
mov al, [h1d]
jbe div10

cmp [h1d], byte 'A'
jb error
cmp [h1d], byte 'F'
mov al, [h1d]
jbe div10

cmp [h1d], byte 'a'
jb error
cmp [h1d], byte 'f'
mov al, [h1d]
jbe div10

error: rw 4,1,msg2,msg2len

div10: div bl

mov [h1d], al
rw 4,1,msg3,msg3len
cmp [h1d], byte 9
jbe add30
add [h1d],byte 7h
add30: add [h1d],byte 30h
rw 4,1,h1d,1

mov eax,1
mov ebx,0
int 80h
