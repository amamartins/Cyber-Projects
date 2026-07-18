## Overview
A Python-based security lab demonstrating how a weak password could be recovered through a dictionary attack

## Objectives
- Understand password hashing
- Demonstrate dictionary attacks
- Analyze password strengths

## Process
1. Created Wordlist
<img width="515" height="205" alt="wordlist photo" src="https://github.com/user-attachments/assets/4e7cf6e7-651e-4ef4-97b8-0aa4ba3c3e9c" />

2. Then I created the hash converter -- passwords are converted into SHA-256 hashes and then stored within a file
<img width="583" height="279" alt="hash creation photo" src="https://github.com/user-attachments/assets/6d836302-b90c-4125-83fd-2a7dbad3e2de" />

3. Also created the dictionary attack to find vulnerable passwords
<img width="550" height="383" alt="dictionary attack photo" src="https://github.com/user-attachments/assets/456c25ee-2e44-4f75-9aa6-76bb8fdff091" />

4. After the first testing attempt, it said no match found. I went back into hash_passwords file and while there were no syntax errors, there seemed to be no need for the f' string. So I removed that
<img width="539" height="252" alt="realized error" src="https://github.com/user-attachments/assets/09263ed0-7e0d-4c0d-a6e8-5312726015a7" />

5. That seemed to work. But I also thought to revise it because I didn't want it to say it found a match, but also show what they are
So, I went back to dictionary attack and added this.
<img width="519" height="222" alt="revising code" src="https://github.com/user-attachments/assets/0230bba3-a24a-4431-ac6e-d80c0b29a00f" />

6. Finally, it worked
<img width="544" height="83" alt="success" src="https://github.com/user-attachments/assets/26371d69-bd1b-4149-89bd-3c2278f95912" />

