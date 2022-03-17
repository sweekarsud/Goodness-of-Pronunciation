# Goodness of Pronunciation (GoP)
This code reflects the work described in the **[INTERSPEECH 2019](https://www.interspeech2019.org/)** published paper on **["An improved goodness of pronunciation (GoP) measure for pronunciation evaluation with DNN-HMM system considering HMM transition probabilities"](https://www.isca-speech.org/archive/pdfs/interspeech_2019/sudhakara19_interspeech.pdf)**.

# Requirements :
* Python (tested with v.2.7.5 & v.3.5.7).
* Kaldi ASR toolkit (for documentation checkout : http://kaldi-asr.org/) considering acoustic models trained with _nnet2_ (Dan's recipe) (tested with nnet2 & nnet3) on LibriSpeech.

# How to run the code : 
Run the below code (**_prop_gop_eqn.py_**) to compute the score using the proposed GoP formulation by passing **_alignment_infile.txt_** and **_posterior_infile.ark_** generated for a given learner's utterance. 
```python
python prop_gop_eqn.py posterior_infile.ark alignment_infile.txt gop_outfile.txt
```
* The **_alignment_infile.txt_** file is the output of the forced-alignment of the learner's uttered speech (.wav file) and this is  obtained using **_align.sh_**.
* The **_posterior_infile.ark_** file contains the frame level posterior-probabilities of the learner's uttered speech (.wav file) and this is obtained using **_nnet_am_compute.cc_**. 
* The **_gop_outfile.txt_** file contains the score for each phoneme.

**NOTE** :
* The above python script requires a lookup table to generate the scores for an acoustic model as discussed in the paper, which can be generated using the following code :
```shell
./gen_lookup_table.sh
```

# Placement of the downloaded folder :
* Once the _Goodness-of-Pronunciation-master.zip_ file is downloaded it needs to be placed in _/home/user/kaldi/egs/Native_Acoustic_Model/s5/_ and needs to unzipped as _Extract Here_ which will result in the creation of the following path _/home/user/kaldi/egs/Native_Acoustic_Model/s5/Goodness-of-Pronunciation-master/_. The native acoustic model needs to be trained on _nnet2_ with all paths functional in _exp_ folder.
* Once the path is created it will have the following file structure :
```bash
├── kaldi_folder
│   ├── native_acoustic_model
│   │   ├── s5
│   │   │   ├── Goodness-of-Pronunciation-master
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

# Citing: 
If you find our work useful, please cite:
```
@inproceedings{Sudhakara2019,
  author={Sweekar Sudhakara and Manoj Kumar Ramanathi and Chiranjeevi Yarra and Prasanta Kumar Ghosh},
  title={{An Improved Goodness of Pronunciation (GoP) Measure for Pronunciation Evaluation with DNN-HMM System Considering HMM Transition Probabilities}},
  year=2019,
  booktitle={Proc. Interspeech 2019},
  pages={954--958},
  doi={10.21437/Interspeech.2019-2363},
  url={http://dx.doi.org/10.21437/Interspeech.2019-2363}
}
```
