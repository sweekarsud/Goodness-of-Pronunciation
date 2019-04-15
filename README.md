# Goodness-of-Pronunciation
This code reflects the work described in the InterSpeech 2019 submitted paper on "An improved goodness of pronunciation (GoP) measure for pronunciation evaluation with DNN-HMM system considering HMM transition probabilities"

# Requirements
* Python (tested with v.2.7.5 & v.3.5.7)
* Kaldi ASR toolkit (for documentation checkout : http://kaldi-asr.org/)

# Placement of the downloaded folder
* Once the _Goodness-of-Pronunciation-master.zip_ file is downloaded it needs to be placed in _/home/user/kaldi/egs/AcousticModel/s5/_ and needs to unzipped as _Extract_Here_ which will result in the creation of the following path _/home/user/kaldi/egs/AcousticModel/s5/Goodness-of-Pronunciation-master/_. The acoustic model needs to be trained on nnet2 with all paths functional in _exp_ folder.
* Once the path is created it will have the following file structure :

# How to run the code : 
* First run the following shell script to generate the lookup table for the trained acoustic model. It only needs to be generated once for a trained acoustic model. A sample lookup-table has been placed in the reqd_files folder for reference.
```shell
./gen_lookup_table.sh
```
After generating  the lookup table, run the following code to compute the GoP formulated score for a learner's uttered wav file by passing _alignment.txt_ and _posterior.ark_ as the file arguments to the python script. 
```python
python prop_gop_eqn.py posterior.ark alignment.txt
```
* A file by the name _alignment.txt_ needs to be generated which should contain the forced-alignment of the learner's uttered speech.
* Another file by the name _posterior.ark_ needs to be generated which should contain the posterior-probability of the learner's uttered speech.
* A completely _Trained Acoustic Model_ on _NNET2_ (For example : Librispeech, Fisher-English, etc.).


