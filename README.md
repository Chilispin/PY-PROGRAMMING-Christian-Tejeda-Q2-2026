This repository contains Python-based implementations, developed as part of Unit 2 for the Programming course (Q2-2026). The objective of this assignment is to establish a professional development environment using Git for version control and GitHub for remote collaboration.

## Project Descriptions

### Classwork 08: Numerical Integration
The script `CW08.py` focuses on **Numerical Integration**, implementing algorithms to approximate the definite integral of a function over a specified interval. 

The program dynamically handles mathematical inputs and lets the user choose between several classical Riemann sum approaches and quadrature rules:
* **Endpoint Conversions:** Automatically evaluates inputs containing mathematical constants like $\pi$ (using the `math` library).
* **Supported Methods:** Includes Left Riemann Sum (**LRM**), Right Riemann Sum (**RRM**), Midpoint Riemann Sum (**MRM**), and the Trapezoidal Rule (**TRAP**).
* **Documentation:** Accompanied by a structured pseudocode file (`PPP CW08.txt`) and a programmatic flowchart (`Flowchart CW08.png`) outlining the logic workflow.

### Classwork 09: Verb Conjugator
The script `CW09.py` handles automatic text processing to conjugate regular Spanish verbs in the present tense. It isolates the grammatical components and links structures efficiently:
* **Slicing Operations:** Dynamically separates the verb stem from its dynamic ending (`-ar`, `-er`, `-ir`).
* **Data Mapping:** Couples a list of Spanish personal pronouns with a multi-level endings dictionary to output clean, structured conjugations.

### Classwork 10: School Management System
The script `CW10.py` simulates a simplified educational control interface structured strictly within a single looped linear flow (without functions) using native Python data structures:
* **Multi-Attempt Login Validation:** Protects access using an iterative validation cycle matching user inputs against a multi-key dictionary containing academic profiles.
* **Role-Based Menus (Polymorphic Logic):** Separates system flows into customized operations based on user privileges:
  * *Student:* Displays user grades by looping through a fixed tuple of subjects and filters academic status using set operations (`aprobadas` and `pendientes`).
  * *Teacher:* Grants administrative controls to view student directories and safely overwrite numerical targets inside nested gradebooks.
  * *Coordinator:* Generates hierarchical, read-only analytical logs summarizing active teachers, plans of study, and global scores.

## Environment & Tools

* **Language:** Python 3.x
* **Version Control:** Git
* **Hosting Platform:** GitHub

## How to Run the Programs

1. Ensure you have Python installed on your system.
2. Clone this repository or download the source files:
   ```bash
   git clone [https://github.com/Chilispin/PY-PROGRAMMING-Christian-Tejeda-Q2-2026.git](https://github.com/Chilispin/PY-PROGRAMMING-Christian-Tejeda-Q2-2026.git)

   AI Use Declaration
No AI tools were used during the development or version control setup of these specific assignments.