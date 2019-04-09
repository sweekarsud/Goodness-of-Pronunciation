#the posterior.ark is modified to posterior.txt for the python code

cat reqd_files/posterior.ark | sed -e '1d' | sed -e 's/^[ \t]*//' > reqd_files/posterior.txt 
