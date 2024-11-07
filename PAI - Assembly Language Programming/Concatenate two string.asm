; 8086 ALP to concatenate 2 strings accepted from the user and display concatenated string.

section .data
mes1 db 10,15, "Enter the first string: "
mes1len equ $-mes1
mes2 db 10,15, "Enter the second string: "
mes2len equ $-mes2
mes3 db 10,15, "Concatenated string is: "
mes3len equ $-mes3

section .bss
str1 resb 20
str2 resb 20
strconcat resb 40  
str1len resb 1
str2len resb 1
strconlen resb 1

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

call strlencal

call strconcat1

mov eax, 1
mov ebx, 0
int 80h
ret
    
strlencal:
rw 4,1,mes1, mes1len  
rw 3,0,str1,20        
mov esi, str1
xor ecx, ecx          

up1:
cmp byte [esi], 0ah  
je down1
inc esi               
inc ecx               
jmp up1

down1:
mov [str1len], cl    
rw 4,1,mes2, mes2len 
rw 3,0,str2,20       
mov edi, str2
xor edx, edx          

up2:
cmp byte [edi], 0ah  
je down2
inc edi               
inc edx               
jmp up2

down2:
mov [str2len], dl    
mov al, [str1len]
add al, [str2len]
mov [strconlen], al   
ret

strconcat1:
mov esi, str1         
mov edi, strconcat   

    
up3:
mov al, [esi]         
mov [edi], al         
inc esi
inc edi
dec byte [str1len]    
jnz up3              

mov esi, str2        

  
up4:
mov al, [esi]         
mov [edi], al        
inc esi
inc edi
dec byte [str2len]    
jnz up4              

    
rw 4,1,mes3,mes3len   
rw 4,1,strconcat,[strconlen] 
ret
