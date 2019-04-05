path = "/home/srinivasa/sweekar_wav/Python_Wrap/";
add_path = "reqd_files/";

name = "Intonation_L1_001"

with open(path + add_path + name + '_post.txt','r') as f:
    x = f.readlines();
posterior = [tmp.rstrip().split(' ') for tmp in x];
             
import subprocess
import shlex
subprocess.call(shlex.split('./extract_from_alignments.sh /home/srinivasa/sweekar_wav/Python_Wrap/reqd_files/Intonation_L1_001_alignments.txt'));
               
with open(path + 'tmp_segments.txt','r') as f:
    x = f.readlines();
number_of_segments = [int(tmp.split(' ')[0]) for tmp in x]; 
                      
with open(path + 'tmp_t_ids.txt','r') as f:
    x = f.readlines();
transition_id = [int(tmp.rstrip().split(' ')[0]) for tmp in x];

with open(path + 'tmp_phones.txt','r') as f:
    x = f.readlines();
aligned_phones = [tmp.rstrip().split(' ')[0] for tmp in x];
                  
