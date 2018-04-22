# ARM LEGv8 CPU Simulators

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/nextseto/ARM-LEGv8/master/LICENSE)

This is a repository that contains the source code for a Verilog based ARM LEGv8 CPU.

## To Run & Test

There are two ways to run and simulate the projects below. Either use the **Xilinx Vivado** or an online tool called **EDA Playground**.

##### Option 1. Xilinx Vivado

- Run the Xilinx Vivado Suite with the module and testbench files for each project. More instructions can be found [here](https://www.xilinx.com/support/university/students.html#overview).

##### Option 2. [EDA Playground](http://www.edaplayground.com/home)
- Login with a Google or Facebook account to save and run modules and testbenches
- Testbench + Design: SystemVerilog/Verilog
- Tools & Simulators: Icarus Verilog 0.9.7

## CPU Versions

- [ARM LEGv8 Simulator](/Single-Cycle): This project simulates an ARM LEGv8 single cycle CPU which supports a subset of instructions for the ARM LEGv8 ISA. Supported instructions include: ``LDUR``, ``STUR``, ``ADD``, ``SUB``, ``ORR``, ``AND``, ``CBZ`` and ``B``. This project is based on the ARM architecture from the textbook: *Computer Organization and Design: The Hardware/Software Interface ARM Edition by D. Patterson and J. Hennessy, Morgan Kaufmann, 2016* [ISBN: 978-012-8017333](https://www.amazon.com/Computer-Organization-Design-Interface-Architecture/dp/0128017333/ref=sr_1_1?ie=UTF8&qid=1483051663&sr=8-1&keywords=9780128017333)

- [ARM LEGv8 Simulator with Pipelining](/Pipelined-Only): This project simulates an ARM LEGv8 multi-cycle/pipelined CPU which supports a subset of instructions for the ARM LEGv8 ISA. Supported instructions include: ``LDUR``, ``STUR``, ``ADD``, ``SUB``, ``ORR``, ``AND``, ``CBZ`` and ``B``. This project is based on the ARM architecture from the textbook: *Computer Organization and Design: The Hardware/Software Interface ARM Edition by D. Patterson and J. Hennessy, Morgan Kaufmann, 2016* [ISBN: 978-012-8017333](https://www.amazon.com/Computer-Organization-Design-Interface-Architecture/dp/0128017333/ref=sr_1_1?ie=UTF8&qid=1483051663&sr=8-1&keywords=9780128017333)

- [ARM LEGv8 Simulator with Pipelining, Hazard Detection, and Forwarding Unit](/Pipeline-With-Hazard-And-Forwarding): This project simulates an ARM LEGv8 multi-cycle/pipelined CPU with hazard detection and forwarding capabilities which supports a subset of instructions for the ARM LEGv8 ISA. Supported instructions include: ``LDUR``, ``STUR``, ``ADD``, ``SUB``, ``ORR``, ``AND``, ``CBZ`` and ``B``. This project is based on the ARM architecture from the textbook: *Computer Organization and Design: The Hardware/Software Interface ARM Edition by D. Patterson and J. Hennessy, Morgan Kaufmann, 2016* [ISBN: 978-012-8017333](https://www.amazon.com/Computer-Organization-Design-Interface-Architecture/dp/0128017333/ref=sr_1_1?ie=UTF8&qid=1483051663&sr=8-1&keywords=9780128017333)

## License

All source code in **ARM-LEGv8** are released under the MIT license. See LICENSE for details.
