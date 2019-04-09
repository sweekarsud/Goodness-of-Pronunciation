
import math
import os
import pandas as pd
import numpy as np

path = os.getcwd();

#to generate look up table containing transition-id's, pdf-id's (senones) and transition probability list
import sys, os
os.system('./gen_lookup_table.sh'); 
  
#modifying posterior.ark to posterior.txt
import sys, os
os.system('./modify_post.sh'); 

#creating segment information list, aligned phones list & transition_id's list
import sys, os
os.system('./extract_from_alignments.sh');
                
with open(path + '/tmp_segments.txt','r') as f:
    x = f.readlines();
number_of_segments = [int(tmp.split(' ')[0]) for tmp in x]; 
                      
with open(path + '/tmp_t_ids.txt','r') as f:
    x = f.readlines();
transition_id = [int(tmp.rstrip().split(' ')[0]) for tmp in x];

with open(path + '/tmp_phones.txt','r') as f:
    x = f.readlines();
aligned_phones = [tmp.rstrip().split(' ')[0] for tmp in x];

with open(path + '/reqd_files/posterior.txt','r') as f:
    x = f.readlines();
posterior = [tmp.rstrip().split(' ') for tmp in x];
num_of_senones = len(posterior[0]);
total_num_frames = len(posterior);                    
                      
with open(path + '/reqd_files/lookup_table.txt','r') as f:
    x = f.readlines();
lookup_tab = [tmp.rstrip().split(' ') for tmp in x];
                  
series = pd.Series(number_of_segments);
cum_number_of_segments_tmp = series.cumsum();
cum_number_of_segments=cum_number_of_segments_tmp.tolist();
cum_number_of_segments.insert(0,0);

phone_score = [];

# Code for Proposed GoP formulation :                             
for x in range(len(number_of_segments)):
    
    req_t_id=transition_id[cum_number_of_segments[x]:(cum_number_of_segments[x+1])];
    req_t_id.sort();
    score=0.0;
    
    for y in range(len(req_t_id)-1):
        
        tmp_prob = float(lookup_tab[req_t_id[y]-1][2]);                                
        tmp_pdf = int(lookup_tab[req_t_id[y]-1][1]);
        tmp_post = float(posterior[cum_number_of_segments[x]+y][tmp_pdf]);
        score = score + math.log(tmp_prob) + math.log(tmp_post);
    
    tmp_pdf = int(lookup_tab[req_t_id[-1]-1][1]);
    tmp_post = float(posterior[cum_number_of_segments[x+1]-1][tmp_pdf]);
    score = (score + math.log(tmp_post) + float(number_of_segments[x]-1)*math.log(num_of_senones)) / float(number_of_segments[x]);
    phone_score.append(score);

# Displaying the scores :
print('Forced aligned phonemes : ');                      
print(aligned_phones);
print('GOP formulated score of each phoneme : ');
print(phone_score);   
                      
#The phoneme_list.txt file contains phoneme's in the 1st column and GoP formulated scores in the 2nd column     
f = open('phoneme_list.txt', 'wb')
for i in range(len(phone_score)):
    f.write("%s   %f\n" % (aligned_phones[i], phone_score[i]))
f.close()
