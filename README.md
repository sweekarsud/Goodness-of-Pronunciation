# Goodness-of-Pronunciation
This code reflects the work described in the InterSpeech 2019 submitted paper on "An improved goodness of pronunciation (GoP) measure for pronunciation evaluation with DNN-HMM system considering HMM transition probabilities"

# Requirements
* Python (tested with v.2.7.5 & v.3.5.7)
* Kaldi ASR toolkit (for documentation checkout : http://kaldi-asr.org/)

# Placement of the downloaded folder
* Once the _Goodness-of-Pronunciation-master.zip_ file is downloaded it needs to be placed in _/home/user/kaldi/egs/Acoustic_Model/s5/_ and needs to unzipped as _Extract_Here_ which will result in the creation of the following path _/home/user/kaldi/egs/Acoustic_Model/s5/Goodness-of-Pronunciation-master/_. The acoustic model needs to be trained on nnet2 with all paths functional in _exp_ folder.
* Once the path is created it will have the following file structure :
```bash
├── your kaldi folder
│   ├── Acoustic_Model
│   │   ├── s5
│   │   │   │   ├── extract_from_alignments.sh
│   │   │   │   ├── gen_lookup_table.sh
│   │   │   │   ├── modify_post.sh
│   │   │   │   ├── extract_from_alignments.sh
│   │   │   │   ├── gop_outfile.txt
│   │   │   │   ├── prop_gop_eqn.py
│   │   │   │   ├── reqd_files
│   │   │   │   │   ├── alignment_infile.txt
│   │   │   │   │   ├── posterior.txt
│   │   │   │   │   ├── posterior_infile.ark
│   │   │   │   │   ├── show_transitions.txt
│   │   │   │   │   ├── lookup_table.txt
│   │   │   │   │   ├── tmp_t_ids.txt
│   │   │   │   │   ├── tmp_phones.txt
│   │   │   │   │   ├── tmp_segments.txt
```

# How to run the code : 
* First run the following shell script to generate the lookup table for the trained acoustic model. It only needs to be generated once for a trained acoustic model. A sample lookup-table has been placed in the reqd_files folder for reference.
```shell
./gen_lookup_table.sh
```
After generating  the lookup table, run the following code to compute the GoP formulated score for a learner's uttered wav file by passing _alignment.txt_ and _posterior.ark_ as the file arguments to the python script. 
```python
python prop_gop_eqn.py posterior_infile.ark alignment_infile.txt gop_outfile.txt
```
* The _alignment.txt_ file needs to be generated and should be placed inside _reqd_files_ folder, it contains the forced-alignment of the learner's uttered speech which can be generated using _align.sh_ (refer kaldi documentation).
* The _posterior.ark_ file also needs to be generated and should be placed inside _reqd_files_ folder, it contains the posterior-probability of the learner's uttered speech which can be generated using _nnet_am_compute.cc_ (refer kaldi documentation).
* The _Acoustic_Model_ (Eg: Librispeech, Fisher-English, etc.) used for computing the score for the GoP formulation needs to be trained on _nnet2_ (refer Dan's recipe in kaldi documentation).
* The GoP formulated score is  printed in the _gop_outfile.txt_ file.


