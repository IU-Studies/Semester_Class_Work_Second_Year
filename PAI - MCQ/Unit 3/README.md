
**Q.1:** Which of the following is NOT true about the 80386 real mode?

   - a) Real mode allows direct access to all 32-bit registers. ✅
   - b) Real mode is backward compatible with the 8086 processor.  
   - c) The processor starts in real mode after a reset.  
   - d) Memory protection features of the 80386 are not available in real mode.   

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.2:** During debugging, a developer wants to compare the contents of two registers and determine if they are equal. Which instruction should they use in real mode?

   - a) CMP AX, BX ✅  
   - b) SUB AX, BX  
   - c) TEST AX, BX  
   - d) MOV AX, BX  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.3:** Which mode of the 80386 processor allows running old 8086 software while using modern system capabilities?

   - a) Protected mode  
   - b) Real mode  
   - c) Virtual 8086 mode ✅  
   - d) Multitasking mode  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.4:** A system designer needs to identify when a valid bus cycle is taking place. Which pin in 80386 helps detect this?

   - a) NMI  
   - b) ADS# ✅  
   - c) M/IO#  
   - d) CLK2  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.5:** If an instruction in the 80386 specifies both a memory address and a value to be used in the operation, what addressing mode is this?

   - a) Immediate  
   - b) Direct ✅  
   - c) Register indirect  
   - d) Memory indirect  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.6:** In a data structure, you need to access the value at a specific memory address directly in your instruction. What addressing mode should be used?

   - a) Register indirect  
   - b) Direct addressing ✅  
   - c) Base-indexed  
   - d) Immediate  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.7:** An application requires accessing a memory location using the value stored in a register. Which addressing mode in 80386 is used?

   - a) Direct  
   - b) Immediate  
   - c) Register indirect ✅  
   - d) Indexed  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.8:** A computer system based on 80386 needs to handle more than one program at a time. Which feature of the 80386 supports this?

   - a) Real mode  
   - b) Virtual memory  
   - c) Multitasking ✅  
   - d) Segmentation  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">



**Q.9:** What does the READY pin in the 80386 indicate?

   - a) Processor is ready to execute instructions  
   - b) Memory or I/O is ready for data transfer ✅  
   - c) Cache is ready  
   - d) Clock signal is stable  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.10:** If a program in real mode wants to output a character to the screen, which instruction should be used?

   - a) OUT DX, AL  
   - b) INT 80H ✅  
   - c) MOV DX, [address]  
   - d) WRITE DX, AL  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.11:** Which addressing mode of the 80386 allows the addition of a displacement value to the base register and the index register?

   - a) Base-displacement  
   - b) Immediate  
   - c) Base-indexed with displacement ✅  
   - d) Register indirect  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.12:** A programmer needs to track changes in the instruction pointer for program flow control. Which register holds this value in 80386?

   - a) ESP  
   - b) EFLAGS  
   - c) EIP ✅  
   - d) CR0  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.13:** In a loop, you are processing an array and need to access memory using only the contents of an index register. Which addressing mode fits this use case?

   - a) Register indirect  
   - b) Indexed ✅  
   - c) Base-indexed  
   - d) Immediate  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.14:** An instruction needs to load a value from memory where the address is computed from a base register and a constant. Which addressing mode is used in 80386?

   - a) Direct  
   - b) Base-displacement ✅  
   - c) Immediate  
   - d) Indexed  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.15:** An instruction in 80386 needs to use an effective address computed by adding a base register and an index register without any displacement. Which addressing mode is this?

   - a) Base-indexed ✅  
   - b) Base-displacement  
   - c) Immediate  
   - d) Indexed with displacement  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.16:** You are debugging a program and need to examine the flags related to the processor's status. Which register holds this information?

   - a) CR0  
   - b) EIP  
   - c) EFLAGS ✅  
   - d) EAX  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.17:** In real mode, the 80386 microprocessor can address how much memory?

   - a) 16 KB  
   - b) 64 KB  
   - c) 1 MB ✅  
   - d) 4 GB  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">



**Q.18:** A software engineer needs to set up a stack frame for a procedure in real mode. Which instruction will help to push a value onto the stack?

   - a) PUSH AX ✅  
   - b) POP AX  
   - c) MOV [SP], AX  
   - d) CALL [address]  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.19:** In the 80386 real mode, how many segment registers are available for addressing?

   - a) 2  
   - b) 4   
   - c) 6 ✅ 
   - d) 8  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.20:** The RESET pin on 80386 is activated. What happens as a result?

   - a) The processor enters idle mode  
   - b) The processor resets and begins execution at a predefined address ✅  
   - c) The cache is invalidated  
   - d) Interrupts are disabled  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.21:** What is the maximum size of a segment in 80386 real mode?

   - a) 16 KB  
   - b) 32 KB  
   - c) 64 KB ✅  
   - d) 1 MB  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.22:** You need to access memory by adding the contents of an index register to a constant displacement. Which 80386 addressing mode supports this?

   - a) Base-displacement  
   - b) Indexed with displacement ✅  
   - c) Register indirect  
   - d) Immediate  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.23:** A program requires the sum of a base register, an index register, and a displacement value to compute the memory address. Which addressing mode does this scenario refer to?

   - a) Immediate  
   - b) Direct  
   - c) Base-indexed with displacement ✅  
   - d) Register indirect  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.24:** A software routine needs to fetch data from a memory address calculated as a sum of the contents of a register and an immediate value. Which addressing mode would you use?

   - a) Immediate  
   - b) Base-displacement ✅  
   - c) Register indirect  
   - d) Direct  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.25:** Which addressing mode would you use in 80386 if an instruction needs to fetch data from a memory location whose address is held in a register, with no further modification?

   - a) Direct  
   - b) Register indirect ✅  
   - c) Base-displacement  
   - d) Immediate  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.26:** An application requires accessing a memory location using the value stored in a register. Which addressing mode in 80386 is used?

   - a) Direct  
   - b) Immediate  
   - c) Register indirect ✅  
   - d) Indexed  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">


**Q.27:** A program requires the address of a memory location computed by adding a base register and an index register. Which addressing mode is this?

   - a) Register indirect  
   - b) Indexed addressing  
   - c) Base-indexed addressing ✅  
   - d) Immediate addressing  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.28:** Your program needs to handle large amounts of memory. What is the maximum amount of memory the 80386 can address?

   - a) 1MB  
   - b) 4GB ✅  
   - c) 16MB  
   - d) 64GB  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.29:** A developer is implementing a loop to repeat a set of instructions five times. Which combination of instructions is suitable for this purpose in real mode?

   - a) MOV CX, 5; LOOP start ✅  
   - b) MOV CX, 5; JNZ start  
   - c) ADD CX, 5; LOOP start  
   - d) MOV CX, 0; LOOP start  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.30:** You are writing an instruction that requires fetching data from a memory location using the sum of a base register, an index register, and a displacement. Which 80386 addressing mode fits this scenario?

   - a) Direct  
   - b) Base-indexed with displacement ✅  
   - c) Register indirect  
   - d) Immediate  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.31:** A program needs to directly use a constant value in an instruction, such as moving a specific value into a register. Which addressing mode does this represent?

   - a) Direct  
   - b) Register indirect  
   - c) Immediate ✅  
   - d) Indexed  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.32:** In 80386 real mode, how is the physical address calculated?

   - a) By adding the segment value directly to the offset.  
   - b) By multiplying the segment value by 16 and then adding the offset. ✅  
   - c) By dividing the segment value by 16 and then adding the offset.  
   - d) By subtracting the segment value from the offset.  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.33:** What is the purpose of the LOCK# pin in 80386?

   - a) Indicates system reset  
   - b) Controls data bus operations  
   - c) Prevents other processors from accessing the system bus during certain operations ✅  
   - d) Enables interrupts  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.34:** You need to access a memory location using the value in a general-purpose register without any displacement. Which addressing mode should you use in the 80386?

   - a) Direct  
   - b) Register indirect ✅  
   - c) Immediate  
   - d) Indexed  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">



**Q.35:** A programmer is writing a routine to clear the memory at a specified location. Which of the following sequences of instructions in real mode would achieve this?

   - a) MOV AX, [address]; XOR AX, AX; MOV [address], AX  
   - b) MOV [address], 0  
   - c) MOV AX, 0; MOV [address], AX ✅ 
   - d) SUB [address], [address]  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.36:** Which pin provides the clock signal to the 80386 processor?

   - a) CLK2 ✅  
   - b) READY  
   - c) NMI  
   - d) ADS#  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.37:** Which 80386 register controls the enabling and disabling of paging?

   - a) CR0 ✅  
   - b) GDTR  
   - c) EFLAGS  
   - d) IDTR  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.38:** In real mode, what is the value of the highest possible physical address the 80386 microprocessor can access?

   - a) 0xFFFFF ✅  
   - b) 0xFFFFFF  
   - c) 0x7FFFFF  
   - d) 0x00FFFF  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.39:** Which pin in 80386 indicates that a Non-Maskable Interrupt (NMI) has interrupted the processor?

   - a) INTR  
   - b) NMI ✅  
   - c) HOLD  
   - d) READY  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.40:** A program accesses a memory location based on the contents of the base register, index register, and an additional displacement value. Which addressing mode applies here?

   - a) Direct  
   - b) Base-indexed with displacement ✅  
   - c) Register indirect  
   - d) Immediate  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.41:** A program needs memory protection in a multitasking environment. Which mode of 80386 provides this feature?

   - a) Real mode  
   - b) Protected mode ✅  
   - c) Virtual 8086 mode  
   - d) Flat mode  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.42:** Which pin in the 80386 processor is responsible for managing interrupts?

   - a) INTR ✅  
   - b) READY  
   - c) HOLD  
   - d) CLK2  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">


**Q.43:** What is the purpose of the paging unit in the 80386 architecture?

   - a) Handle hardware interrupts  
   - b) Manage stack operations  
   - c) Translate linear addresses to physical addresses ✅  
   - d) Control input/output operations  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.44:** What does the HOLD pin in 80386 indicate?

   - a) DMA operation ✅  
   - b) Instruction execution  
   - c) Interrupt request  
   - d) Memory access  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.45:** You are working on a loop where you need to access an array using an offset added to the base address stored in a register. Which addressing mode is being utilized?

   - a) Base-displacement ✅  
   - b) Direct  
   - c) Immediate  
   - d) Base-indexed  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.46:** A program uses the general-purpose register to store a return value from a function. Which register is typically used for this?

   - a) EAX ✅  
   - b) EFLAGS  
   - c) EBX  
   - d) CS  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.47:** In the 80386 architecture, how is logical address translated to physical address?

   - a) Paging and Segmentation ✅  
   - b) Direct mapping  
   - c) Cache memory  
   - d) Interrupt vector tables  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.48:** Which addressing mode would be used in 80386 if you want to add a displacement value to an index register to compute a memory address?

   - a) Indexed with displacement ✅  
   - b) Base-displacement  
   - c) Direct  
   - d) Immediate  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.49:** You need to move an immediate value into a general-purpose register. What addressing mode is used in this case?

   - a) Immediate addressing ✅  
   - b) Register indirect  
   - c) Direct  
   - d) Indexed  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.50:** You are running a modern operating system that requires multitasking. Which feature of the 80386 processor enables this?

   - a) Real mode  
   - b) Protected mode ✅  
   - c) Virtual 8086 mode  
   - d) Multitasking is not supported  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">


**Q.51:** A program calculates an effective address using only an index register and a displacement. Which addressing mode is this?

   - a) Indexed with displacement ✅  
   - b) Base-indexed  
   - c) Immediate  
   - d) Direct  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.52:** Which pin is used to handle requests for Direct Memory Access (DMA) in the 80386?

   - a) HLDA   
   - b) M/IO#  
   - c) NMI  
   - d) HOLD ✅

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.53:** Which pin indicates whether the current bus cycle is a memory or I/O operation?

   - a) M/IO# ✅  
   - b) NMI  
   - c) READY  
   - d) LOCK#  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.54:** Which of the following modes is NOT supported by the 80386 microprocessor?

   - a) Real Mode  
   - b) Protected Mode  
   - c) Virtual 8086 Mode  
   - d) Hypervisor Mode ✅  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.55:** What is the size of the data bus in the 80386 microprocessor?

   - a) 8-bit  
   - b) 16-bit  
   - c) 32-bit ✅  
   - d) 64-bit  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.56:** What is the maximum number of segments that can be active simultaneously in the 80386 architecture?

   - a) 6 ✅
   - b) 8   
   - c) 16  
   - d) 32  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.57:** The 80386 enables itself to organize the available physical memory into pages, which is known as

   - a) Segmentation  
   - b) Paging ✅  
   - c) Memory division  
   - d) None of the mentioned  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.58:** The unit in 80386 architecture that drives the execution of all shift and rotate operations is

   - a) Memory management unit  
   - b) Execution unit   
   - c) Instruction unit  
   - d) Barrel shifter ✅

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.59:** The paging unit works under the control of

   - a) Memory management unit   
   - b) Segmentation unit ✅
   - c) Execution unit
   - d). Instruction unit 

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.60:** The 80386DX is a processor that supports

   - a) 8-bit data operand  
   - b) 16-bit data operand  
   - c) 32-bit data operand   
   - d) All of the mentioned ✅

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

**Q.61:** In a 32-bit register, ESP, the lower 16-bits of the register can be represented by

   - a) LSP  
   - b) FSP  
   - c) SP ✅  
   - d) None of the mentioned  

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">


**Q.62:** Which of the following is not a scale factor of addressing modes of the 80386?

   - a) 2  
   - b) 4  
   - c) 6 ✅  
   - d) 8

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">


**Q.63:** The unit that is disabled in real address mode is:

   - a) Central processing unit  
   - b) Memory management unit  
   - c) Paging unit ✅  
   - d) Bus control unit  

