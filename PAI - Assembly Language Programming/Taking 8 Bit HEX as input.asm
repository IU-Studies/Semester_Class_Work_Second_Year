;8086 ALP to accept 8 Bit Haxadecimal number from the user and display the same on screen. 
;Implement validity check and ASCII to HEX and HEX to ASCII.  

section .data

msg1 db 10,15,'Enter valid 2 digit HEX NUM (0-FF) '
msg1len equ $-msg1
msg2 db 10,15,'Enter NUM is invalid HEX, please reenter valid 2 digit HEX (0-FF) '
msg2len equ $-msg2
msg3 db 10,15,'Entered 2 digit HEX NUM is : '
msg3len equ $-msg3

count db 2
h2d db 0,0,0
h2dn db 0
flag db 0

section .bss
h1d resb 1

%macro rw 4
push rax
push rbx
push rcx
push rdx
mov eax,%1
mov ebx,%2
mov ecx,%3
mov edx,%4
int 80h
pop rdx
pop rcx
pop rbx
pop rax
%endmacro

section .text
global _start
_start:

rw 4,1,msg1,msg1len

call h2da

rw 4,1,msg3,msg3len

call h2dd

mov eax,1
mov ebx,0
int 80h

h2da:
mov [count], byte 2
mov [flag],byte 0
rw 3,0,h2d,3
mov ebx,h2d
up2: 
cmp [ebx],byte 0ah
je return
mov al,[ebx]
mov [h1d],al
call asciitohex
cmp [flag],byte 1
jz h2da
shl byte [h2dn],4
mov al,[h1d]
or [h2dn],al
inc ebx
dec byte [count]
jnz up2
return: ret

asciitohex:
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
jbe sub57

error: mov [flag],byte 1
rw 4,1,msg2,msg2len
ret

sub57: sub [h1d],byte 20h
sub37: sub [h1d],byte 7h
sub30: sub [h1d],byte 30h
ret

h2dd:
mov byte [count],2
up3:rol byte [h2dn],4
mov al,[h2dn]
and al,0fh
mov [h1d],al
call h1dd
dec byte [count]
jnz up3
ret


h1dd:
cmp [h1d], byte 9
jbe add30
add [h1d],byte 7h
add30: add [h1d],byte 30h
rw 4,1,h1d,1
ret
