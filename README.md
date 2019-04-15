# Goodness-of-Pronunciation
This code reflects the work described in the InterSpeech 2019 submitted paper on "An improved goodness of pronunciation (GoP) measure for pronunciation evaluation with DNN-HMM system considering HMM transition probabilities"

# Requirements
* Python (tested with v.2.7.5 & v.3.5.7)
* Kaldi ASR toolkit (for documentation checkout : http://kaldi-asr.org/)
* The _Native Acoustic Model_ used for computing the GoP formulated score needs to be trained with _nnet2_ considering the architecture provided in Dan's recipe (refer kaldi documentation).

# Placement of the downloaded folder
* Once the _Goodness-of-Pronunciation-master.zip_ file is downloaded it needs to be placed in _/home/user/kaldi/egs/Native_Acoustic_Model/s5/_ and needs to unzipped as _Extract_Here_ which will result in the creation of the following path _/home/user/kaldi/egs/Native_Acoustic_Model/s5/Goodness-of-Pronunciation-master/_. The native acoustic model needs to be trained on _nnet2_ with all paths functional in _exp_ folder.
* Once the path is created it will have the following file structure :
```bash
├── your kaldi folder
│   ├── Native_Acoustic_Model
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
* First run the following shell script to generate the lookup table for the native acoustic model. It only needs to be generated once for a trained acoustic model. A sample lookup-table has been placed in the reqd_files folder for reference.
```shell
./gen_lookup_table.sh
```
After generating  the lookup table, run the following code to compute the GoP formulated score for a learner's uttered _wav_ file by passing _alignment_infile.txt_ and _posterior_infile.ark_ as the file arguments to the python script. 
```python
python prop_gop_eqn.py posterior_infile.ark alignment_infile.txt gop_outfile.txt
```
* The _alignment_infile.txt_ file is the forced-alignment of the learner's uttered speech which can be generated using _align.sh_ (refer kaldi documentation). After generating the file it needs to be placed inside the _reqd_files_ folder.
* The _posterior_infile.ark_ file is the posterior-probability of the learner's uttered speech which can be generated using _nnet_am_compute.cc_ (refer kaldi documentation). After generating the file it needs to be placed inside the _reqd_files_ folder.
* The GoP formulated score is  printed in the _gop_outfile.txt_ file.


