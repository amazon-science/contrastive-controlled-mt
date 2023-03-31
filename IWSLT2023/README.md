## Formality-annotated data

This repository contains the dataset and benchmark used for the IWSLT 2023 shared task on [Formality Control for SLT](https://iwslt.org/2023/formality).
The targeted train and test sets comprise of source segments paired with two contrastive reference translations, one for each formality level (informal and formal), and phrase-level annotations.
Formality distinctions are expressed by the use of grammatical register or honorific language.
Table 1 gives examples of annotated contrastive translations from the dataset and Table 2 reports the number of source segments used for training and evaluation.


**Table 1** Contrastive reference translations with different formality levels. Phrase-level formality markers in the target languages are annotated with [F]text[/F].

|Language	|	|Text	|
|---	|---	|---	|
|KO	|Source	|Yeah Did your mom know you were throwing the party?	|
|	|Informal	|그, 어머님은 **[F]네가[/F]** 그 파티 연 거 **[F]아셔[/F]**?|
|	|Formal	|그, 어머님은 **[F]님이[/F]** 그 파티 연 거 **[F]아세요[/F]**?|
|VI |Source	|Is the sun blocking your internet signal tonight?|
|	|Informal |Tối nay mặt trời có chặn tín hiệu internet của **[F]bạn[/F]** không? |
|	|Formal	|Tối nay mặt trời có chặn tín hiệu internet của **[F]quý vị[/F]** không **[F]ạ[/F]**?|

**Table 2**. Number of source segments in the released dataset.

|setting	|language pair	|train	|test		|
|---	|---	|---	|---		|
|supervised	|EN-KO	|400	|600		|
|supervised	|EN-VI	|400	|600		|
|zero-shot	|EN-PT	|0	|600		|
|zero-shot	|EN-RU	  |0	|600		|

This shared task will offer two training scenarios: **supervised** and **zero-shot**. For the **supervised** training scenario, participants can use the labeled training set for training and development. For the **zero-shot** task, we will release only test data.

### Dataset structure
The train and test splits are found in the `data/` directory: `data/train` and `data/test`. 
Each language pair has a dedicate subdirectory.
The data splits will be released according to the [shared task schedule](https://iwslt.org/2023/formality#important-dates).

The file naming conventions for the train split are: 
- source files: `formality-control.train.[domain].[en-tl].[en]`
- plain reference files: `formality-control.train.[domain].[en-tl].[formality-level].[tl]`
- annotated reference files: `formality-control.train.[domain].[en-tl].[formality-level].annotated.[tl]`

where the target language `tl` is one of: `ko, vi, pt, ru`; \
domain refers to the data sources and is one of: `topical-chat`, `telephony`; \
formality level is one of: `formal` or `informal`.

### Additional Resources

We [release](https://github.com/amazon-science/contrastive-controlled-mt/releases/tag/classifier-v1.0.0) a multilingual classifier trained to predict the formality of a text for the language pairs: EN-KO, EN-VI, EN-RU and EN-PT. We finetune [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) model on human-written formal and informal text following the setup from [Briakou et al., EMNLP 2021](https://aclanthology.org/2021.emnlp-main.100.pdf). The returned scores are probabilities corresponding to each label with `label0` and `label1` corresponding to the `informal` and `formal` classes respectively.

Assuming the classifier has been extracted to `/tmp/`, the evaluation can be performed as follows (after installing [transformers](https://pypi.org/project/transformers/)):

```bash
python formality_classifier.py -m /tmp/xlmr-classifier -t formal -i /path/to/formality-control-1.formal.ko
```

For a full list of options including device settings and batch size, see `python formality_classifier.py --help`.



## Citation

If you are a participant in the IWSLT shared task on Formality Control for SLT, or are otherwise using the resources 
from this repository in your work, please cite:
```
@inproceedings{nadejde-etal-2022-coca-mt,
    title = "{C}o{C}o{A}-{MT}: A Dataset and Benchmark for {Co}ntrastive {Co}ntrolled {MT} with Application to Formality",
    author = "N\u{a}dejde, Maria  and Currey, Anna  and Hsu, Benjamin  and Niu, Xing and Federico, Marcello and Dinu, Georgiana",
    booktitle = "Findings of the Association for Computational Linguistics: NAACL 2022",
    month = jul,
    year = "2022",
    address = "Seattle, USA",
    publisher = "Association for Computational Linguistics",
}
```

If you use the [topical-chat](https://github.com/alexa/Topical-Chat) part of the dataset, in addition to the citation above, please also cite:
```
@inproceedings{Gopalakrishnan2019, 
  author={Karthik Gopalakrishnan and Behnam Hedayatnia and Qinlang Chen and Anna Gottardi and Sanjeev Kwatra and Anu Venkatesh and Raefer Gabriel and Dilek Hakkani-Tür},
  title={{Topical-Chat: Towards Knowledge-Grounded Open-Domain Conversations}},
  year=2019,
  booktitle={Proc. Interspeech 2019},
  pages={1891--1895},
  doi={10.21437/Interspeech.2019-3079},
  url={http://dx.doi.org/10.21437/Interspeech.2019-3079}
}
```
