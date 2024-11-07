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
h1d resb 1          
decimal resb 1      

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

call h1da
call h1dd

call hex_to_decimal

call print_decimal

mov eax,1           
mov ebx,0
int 80h

h1da:
rw 4,1,msg1,msg1len
up1: rw 3,0,h1d,2  
cmp [h1d], byte '0'
jb error
cmp [h1d], byte '9'
jbe sub30
cmp [h1d], byte 'A'
jb error
cmp [h1d], byte 'F'
jbe sub37
cmp [h1d], byte 'a'
jb error
cmp [h1d], byte 'f'
jbe to_upper
error: rw 4,1,msg2,msg2len
jmp up1

to_upper: sub [h1d], byte 20h  ; Convert lowercase a-f to uppercase A-F
jmp sub37

sub37: sub [h1d], byte 7h    
sub30: sub [h1d], byte 30h   
ret

h1dd:
rw 4,1,msg3,msg3len
cmp [h1d], byte 9
jbe add30
add [h1d],byte 7h
add30: add [h1d],byte 30h
rw 4,1,h1d,1            
ret

hex_to_decimal:
cmp [h1d], byte 9
jbe store_decimal
; If the input is a letter between 'A' and 'F'
add [h1d], byte 9       
store_decimal:
mov al, [h1d]        
mov [decimal], al    
ret

print_decimal:
rw 4,1,msg4,msg4len
mov al, [decimal]      
add al, '0'            
rw 4,1,decimal,1       
ret
