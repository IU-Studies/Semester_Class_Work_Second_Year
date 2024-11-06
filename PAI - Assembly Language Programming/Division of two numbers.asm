section .data
Dividend db 21       
Divisor db 5       

section .bss
quotient resb 1   
remainder resb 1  

section .text
global _start
_start:
mov al, [Dividend]
mov bl, [Divisor]
div bl           
mov [quotient], al
mov [remainder], ah

mov eax, 1       
xor ebx, ebx     
int 80h
