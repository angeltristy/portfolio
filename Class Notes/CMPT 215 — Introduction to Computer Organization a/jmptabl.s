# function numbers for environment calls
	.equ SYS_exit, 93
	.equ SYS_readInt, 245
	.equ SYS_printStr, 248
	.equ SYS_readStr, 249

# ascii character codes
	.equ NEWLINE, 10
	.equ BLANK, 32

# read-only data section
	.section .rodata
prmpt1: .asciz "Enter a four character string:\n"
prmpt2: .asciz "Enter an integer between 0 and 3: "
newl:	.asciz "\n"
jmptab:	.word A
	.word B
	.word C
	.word D

# uninitialized data section
	.section .bss
istr:	.space 128
ostr:	.space 6
junk:   .space 128

# code section
	.section .text
	.globl _start

_start:	la t0, ostr
	li t1, NEWLINE
	sb t1, 4(t0)
	sb zero,5(t0)

again:	la a0, prmpt1
	li a7, SYS_printStr
	ecall

	la a0, istr
	li a1, 128
	li a7, SYS_readStr
	ecall

	la s0, istr		# part up to getint needed for length !=4 chars
	li s1, NEWLINE
	li s2, BLANK
	addi s3, s0, 4
	sb zero, 5(s0)

loop:	lbu s4, 0(s0)
	beq s1, s4, pad		# found a newline character in input string
	beq s0, s3, getint	# input length > 4
	addi s0, s0, 1
	j loop

pad:	beq s0, s3, getint
	sb s2, 0(s0)		# pad with blanks if string < 4 characters
	addi s0, s0, 1
	j pad

getint:	la a0, prmpt2
	li a7, SYS_printStr
	ecall

	li a7, SYS_readInt
	ecall
	mv s0, a0

	la a0, junk		# get rid of anything else on line that
	li a1, 128		#    integer was read on
	li a7, SYS_readStr
	ecall

	li t0, 3
	bgtu s0, t0, getint

	la s1, istr
	la s2, ostr

	la s3, jmptab
	add s0, s0, s0		# instead of the two "add s0, s0, s0"
	add s0, s0, s0		# instructions, could use "slli s0, s0, 2"
	add s3, s3, s0
	lw s3, 0(s3)
	jr s3

A:	lbu t1, 0(s1)
	sb t1, 0(s2)
	lbu t1, 1(s1)
	sb t1, 1(s2)
	lbu t1, 2(s1)
        sb t1, 2(s2)
        lbu t1, 3(s1)
        sb t1, 3(s2)
	j prnt
	
B:	lbu t1, 1(s1)
	sb t1, 0(s2)
	lbu t1, 2(s1)
	sb t1, 1(s2)
	lbu t1, 3(s1)
        sb t1, 2(s2)
        lbu t1, 0(s1)
        sb t1, 3(s2)
	j prnt

C:	lbu t1, 2(s1)
	sb t1, 0(s2)
	lbu t1, 3(s1)
	sb t1, 1(s2)
	lbu t1, 0(s1)
        sb t1, 2(s2)
        lbu t1, 1(s1)
        sb t1, 3(s2)
	j prnt

D:	lbu t1, 3(s1)
	sb t1, 0(s2)
	lbu t1, 0(s1)
	sb t1, 1(s2)
	lbu t1, 1(s1)
        sb t1, 2(s2)
        lbu t1, 2(s1)
        sb t1, 3(s2)

prnt:	la a0, ostr
	li a7, SYS_printStr
        ecall
	j again
