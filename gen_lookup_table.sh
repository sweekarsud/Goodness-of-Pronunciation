#! /bin/bash

path="../exp/nnet2_online/nnet_ms_a_online"
#source directory for final.mdl and phones.txt

../../../../src/bin/show-transitions $path/phones.txt $path/final.mdl > reqd_files/show_transitions.txt
#the binary show-transitions will be available in kaldi/src/bin/

echo "Generating lookup-table......."

while read -r line;
do

	decider=$(echo "$line" | grep "Transition-id =")

	if [ -n "$decider" ]
	then
		t_id=$(echo "$line" | cut -d' ' -f3)
		t_prob=$(echo "$line" | cut -d' ' -f6)
		echo "$t_id $pdf $t_prob"
	else
		pdf=$(echo "$line" | rev | cut -d' ' -f1 | rev)
	fi

done < reqd_files/show_transitions.txt > reqd_files/lookup_table.txt


