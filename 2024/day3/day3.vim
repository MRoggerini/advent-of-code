%s/mul(\d\+,\d\+)\|do\(n't\)\?()/\r§\0\r/g
%s/^[^§].*\n//g
%s/\n\n/\r/g
%s/§//g
%s/mul(\(\d\+\),\(\d\+\))/\1*\2/
%s/do()/+/
%s/don't()/-/
%s/\s*//g
:w input_modified.txt
:qa!
