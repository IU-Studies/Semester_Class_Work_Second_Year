;8086 ALP to perform division of 2, 8 Bit numbers stored in memory, store your result in memory. 
;Use gdb debugger to execute and check the result. 

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
