;8086 ALP to compare 2 strings accepted from the user and display the result and comparison.

section .data
mes1 db 10, 15, "Enter first string "
mes1len equ $-mes1
mes2 db 10, 15, "Enter second string "
mes2len equ $-mes2
mes3 db 10, 15, "Entered strings are EQUAL "
mes3len equ $-mes3
mes4 db 10, 15, "Entered string are NOT EQUAL "
mes4len equ $-mes4

section .bss
str1 resb 50
str2 resb 50
str1len resb 1
str2len resb 1

%macro rw 4
mov eax, %1
mov ebx, %2
mov ecx, %3
mov edx, %4
int 80h
%endmacro

section .text
global _start
_start:

rw 4,1,mes1,mes1len
rw 3,0,str1,50

rw 4,1,mes2,mes2len
rw 3,0,str2,50

mov esi, str1
up1: mov al,[esi]
cmp al,0ah
je down1
inc byte [str1len]
inc esi
jmp up1

down1: mov edi, str2
up2: mov al, [edi]
cmp al,0ah
je down2
inc byte [str2len]
inc edi
jmp up2

down2:
mov al, [str1len]
cmp al, [str2len]
jne down3
MOV ESI, str1
MOV EDI, str2

up3: mov al,[esi]
cmp al, [edi]
jne down3
inc esi
inc edi
cmp byte [str1len], 0
je down5
dec byte [str1len]
jnz up3
down5: rw 4,1,mes3,mes3len
jmp down4
down3: rw 4,1, mes4, mes4len

down4: mov eax,1
mov ebx,0
int 80h
