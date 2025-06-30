# CSE221: Algorithm Analysis & Design - BRAC UNIVERSITY

Pre-requisite: CSE220

This course addresses the study of efficient algorithms, their analyses and effective algorithm design techniques. Standard algorithm design strategies, such as, Divide and Conquer paradigm, Greedy method, Dynamic programming, Backtracking, Basic search and traversal techniques, Graph algorithms, Elementary parallel algorithms, Algebraic simplification and transformations, Lower bound theory, NP-hard and NP-complete problems are discussed in the course. Examples of data structures and algorithms studied in details are Heaps; Hashing; Graph algorithms: Shortest paths, Depth-first and Breadth-first search, Network flow, Computational geometry, Minimum Spanning Tree; Integer arithmetic: GCD, primality; polynomial and matrix calculations; Sorting; Performance bounds, asymptotic analysis, worst case and average case behavior, correctness and complexity. The course includes a compulsory 3 hour laboratory work every week.
Course Objectives

a. Introduce students to time and space complexity of algorithms.

b. Teach students different sorting and searching methods and make them understand which is effective to use.

c. Make them familiar with different problem solving paradigms as described in the course catalog above.
List of Books

1. Introduction to Algorithms,Charles E. Leiserson, Clifford Stein, Ronald Rivest, and Thomas H. Cormen,2009,3rd edition,The MIT Press,ISBN: 9780262033848

2. Algorithm Design,Eva Tardos and John Kleinberg,(March 26, 2005),1st edition ,Pearson,ISBN-13: 978-0321295354

3. Algorithms,Dasgupta, Vazirani, Papadimitriou,July 2006,1st edition,McGraw Hill,ISBN: 9780073523408

4. Algorithms Illuminated,Tim Roughgarden,2022,1st edition,Cambridge,ISBN: 9780999282984

flowchart TB
    Repo["CSE221-Course Repository"]:::root
    README["README.md"]:::doc
    Python["Python Interpreter"]:::env

    Repo --> README
    Repo --> Python

    Repo --> A1["Package: Assignment-1"]:::package
    A1 --> T101["Module: Task-01.py"]:::task
    A1 --> T102["Module: Task-02.py"]:::task
    A1 --> T103["Module: Task-03.py"]:::task
    A1 --> T104["Module: Task-04.py"]:::task
    A1 --> T105["Module: Task-05.py"]:::task
    A1 --> T106["Module: Task-06.py"]:::task
    A1 --> T107["Module: Task-07.py"]:::task

    Repo --> A2["Package: Assignment-2"]:::package
    A2 --> T201["Module: Task 01.py"]:::task
    A2 --> T202["Module: Task 02.py"]:::task
    A2 --> T203["Module: Task 03.py"]:::task
    A2 --> T204["Module: Task 04.py"]:::task
    A2 --> T205["Module: Task 05.py"]:::task

    Repo --> A3["Package: Assignment-3"]:::package
    Repo --> A4["Package: Assignment-4"]:::package

    Repo --> A5["Package: Assignment-5"]:::package
    A5 --> T501["Module: Task 01.py"]:::task
    A5 --> T502["Module: Task 02.py"]:::task
    A5 --> T503["Module: Task 03.py"]:::task
    A5 --> T504["Module: Task 04.py"]:::task
    A5 --> T505["Module: Task 05.py"]:::task
    A5 --> T506["Module: Task 06.py"]:::task

    Repo --> A6["Package: Assignment-6"]:::package

    Repo --> A7["Package: Assignment-7"]:::package
    A7 --> T701["Module: Task 01.py"]:::task
    A7 --> T702["Module: Task 02.py"]:::task
    A7 --> T703["Module: Task 03.py"]:::task
    A7 --> T704["Module: Task 04.py"]:::task
    A7 --> T705["Module: Task 05.py"]:::task
    A7 --> T706["Module: Task 06.py"]:::task

    click Repo "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/tree/main//"
    click README "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//README.md"
    click A1 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/tree/main//Assignment-1/"
    click T101 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-1/Task-01.py"
    click T102 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-1/Task-02.py"
    click T103 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-1/Task-03.py"
    click T104 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-1/Task-04.py"
    click T105 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-1/Task-05.py"
    click T106 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-1/Task-06.py"
    click T107 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-1/Task-07.py"
    click A2 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/tree/main//Assignment-2/"
    click T201 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-2/Task 01.py"
    click T202 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-2/Task 02.py"
    click T203 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-2/Task 03.py"
    click T204 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-2/Task 04.py"
    click T205 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-2/Task 05.py"
    click A5 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/tree/main//Assignment-5/"
    click T501 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-5/Task 01.py"
    click T502 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-5/Task 02.py"
    click T503 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-5/Task 03.py"
    click T504 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-5/Task 04.py"
    click T505 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-5/Task 05.py"
    click T506 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-5/Task 06.py"
    click A7 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/tree/main//Assignment-7/"
    click T701 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-7/Task 01.py"
    click T702 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-7/Task 02.py"
    click T703 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-7/Task 03.py"
    click T704 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-7/Task 04.py"
    click T705 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-7/Task 05.py"
    click T706 "https://github.com/musfiquerprottoy/cse221-algorithm-analysis-design/blob/main//Assignment-7/Task 06.py"

    classDef root fill:#ffffff,stroke:#000000,stroke-width:2px;
    classDef package fill:#e0f7fa,stroke:#006064,stroke-width:1.5px;
    classDef task fill:#e8f5e9,stroke:#1b5e20,stroke-width:1px;
    classDef doc fill:#fff3e0,stroke:#e65100,stroke-dasharray:5 5;
    classDef env fill:#f3e5f5,stroke:#4a148c,stroke-width:1px;
