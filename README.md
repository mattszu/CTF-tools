# CTF-tools
tools used to help/solve challenges

Collection of small tools used in CTF that I'll add here when I remember to.

<b>buffovr_exploit</b>
<br>
generic simple template for buffer overflow exploit - hardcode shellcode to execute shell (/bin/sh)
just need to modify buffer size and possibly NOPsled


<b>fmtstr_search.py</b>
<br>
quickly scripted tool used to find the modfiable paramater in a vulnerable print format strong.
Hardcoded to use 'AAAABBBB', so I use by coupling with grep and searching for
"41414141" or "42424242" hexidecimal values of 'A' and 'B'
<br>
<b>Example:</b><br>
python fmtstr_search.py | grep "41414141"

outputs the corresponding paramater index
*change "program =" to desired program 
