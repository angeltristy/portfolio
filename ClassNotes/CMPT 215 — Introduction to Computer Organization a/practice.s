# function ecall numbers
.equ SYS_exit, 93
.equ SYS_printInt, 244

.section .rodata
newl: .asciz "\n"

.section .bss
    A: .space 40

.section .text
.globl _start:
#s0 for i
#s1 for N
#t0 as a pointer

_start:
    mv   s0, zero      # i = 0
    # (s1 should already contain N; if not, load it before the loop)
    la   t0, A         # t0 = &A[0] (pointer to first int)

loop:
    beq  s0, s1, next  # if i == N, exit loop

    lw   t1, 0(t0)     # t1 = A[i]
    addi t1, t1, 1     # t1 = t1 + 1
    sw   t1, 0(t0)     # A[i] = t1

    addi s0, s0, 1     # i++
    addi t0, t0, 4     # t0 = t0 + 4  (FIX: advance by 4 bytes per int)

    j    loop          # repeat

next:
    # ... continue program (or exit, etc.)
    # (example exit)
    li   a0, 0
    li   a7, 93        # SYS_exit
    ecall