## Formality-annotated data

This repository contains the dataset and benchmark used for the shared task on [Formality Control for SLT](https://iwslt.org/2022/formality).
The targeted train and test sets comprise of source segments paired with two contrastive reference translations, one for each formality level (informal and formal), and phrase-level annotations.
Formality distinctions are expressed by the use of grammatical register or honorific language.
Table 1 gives examples of annotated contrastive translations from the dataset and Table 2 reports the number of source segments used for training and evaluation.


**Table 1** Contrastive reference translations with different formality levels. Phrase-level formality markers in the target languages are annotated with [F]text[/F].

|Language	|	|Text	|
|---	|---	|---	|
|HI	|Source	|Yeah but don't blame yourself if society has it set up that way.	|
|	|Informal	|हाँ यदि समाज ने ही इस तरह स्थापित किया है तो खुद को दोष न **[F]दे[/F]**	|
|	|Formal	|हाँ यदि समाज ने ही इस तरह स्थापित किया है तो खुद को दोष न **[F]दें[/F]**	|
|DE	|Source	|Do you like Legos? did you ever play with them as a child or even later?|
|	|Informal |**[F]Magst du[/F]** Legos? **[F]Hast du[/F]** jemals als Kind mit ihnen gespielt oder sogar später?  |
|	|Formal	|**[F]Mögen Sie[/F]** Legos? **[F]Haben Sie[/F]** jemals als Kind mit ihnen gespielt oder sogar später? |
|JA	|Source	|I'm very sorry to hear that. You may go back and see if the chef can try to make meal again.	|
|	|Informal (_Kudaketa_)	|それを聞いて大変 **[F]残念に思う[/F]** 。 **[/F]戻って[/F]** 、シェフがもう一度食事を作り直せるかどうかを **[F]確認して[/F]** 。	|
|	|Formal (_Teineigo_)	|それを聞いて大変 **[F]残念に思います[/F]** 。 **[F]戻って[/F]** 、シェフがもう一度食事を作り直せるかどうかを **[F]確認してください[/F]** 。	|
|	|High-formal (_Sonkeigo / Kenjōgo_)	|それを聞いて大変 **[F]残念に思います[/F]** 。 **[F]お戻りになって[/F]** 、シェフがもう一度食事を作り直せるかどうかを **[F]確認なさってください[/F]** 。	|

**Table 2**. Number of source segments in the released dataset.

|setting	|language pair	|train	|test		|
|---	|---	|---	|---		|
|supervised	|EN-JA	|1,000	|600		|
|supervised	|EN-DE	|400	|600		|
|supervised	|EN-ES	|400	|600		|
|supervised	|EN-HI	|400	|600		|
|zero-shot	|EN-IT	|0	|600		|
|zero-shot	|EN-RU	|0	|600		|

This shared task will offer two training scenarios: **supervised** and **zero-shot**. For the **supervised** training scenario, participants can use the labeled training set for training and development. For the **zero-shot** task, we will release only test data.

### Dataset structure
The train and test splits are found in the `data/` directory: `data/train` and `data/test`. 
Each language pair has a dedicate subdirectory.
The data splits will be released according to the [shared task schedule](https://iwslt.org/2022/formality#important-dates).

The file naming conventions for the train split are: 
- source files: `formality-control.train.[domain].[en-tl].[en]`
- plain reference files: `formality-control.train.[domain].[en-tl].[formality-level].[tl]`
- annotated reference files: `formality-control.train.[domain].[en-tl].[formality-level].annotated.[tl]`

where the target language `tl` is one of: `de,es,hi,ja`; \
domain refers to the data sources and is one of: `topical-chat`, `telephony`; \
formality level is one of: `formal` or `informal`.

## Evaluation

We provide an evaluation sript `scorer.py` for computing the `matched-formal` and `matched-informal` accuracy scores for a given system output. Requires python>=3.7.

### Command-line Usage

The scorer takes system hypotheses and annotated formal and informal references as inputs. A list of options can be found with `python scorer.py --help`.

```
usage: scorer.py [-h] [-hyp HYPOTHESES] [-f FORMAL_REFS] [-if INFORMAL_REFS]
                 [-nd]

optional arguments:
  -h, --help            show this help message and exit
  -hyp HYPOTHESES, --hypotheses HYPOTHESES
                        File containing system detokenized output translations
  -f FORMAL_REFS, --formal_refs FORMAL_REFS
                        File containing formal references with annotated
                        grammatical formality
  -if INFORMAL_REFS, --informal_refs INFORMAL_REFS
                        File containing informal references with annotated
                        grammatical formality.
  -nd, --non_whitespace_delimited
                        If the target language tokens are non-whitespace
                        delimited (e.g. for Japanese)
```
System hypotheses should be detokenized text, with one prediction per line, and formal, informal references should be detokenized with grammatical formality annotated with `[F],[/F]` tags. Benchmark references are provided under `data/`. For example, to score an en-de system with _formal_ hypotheses:
```
python scorer.py \
-hyp formality-control-1.formal.de \
-f formality-control.test.en-de.formal.annotated.de \
-if formality-control.test.en-de.informal.annotated.de
Formal Acc: 0.923, Informal Acc: 0.077
```

For non-whitespace delimited languages (e.g. Japanese), users should specify (by passing the `--non_whitespace_delimited` flag) that tokens should _not_ be split on whitespace before phrase matching when computing the number of matched reference annotations. For example, to score an en-ja system with _informal_ hypotheses:
```
python scorer.py \
-hyp formality-control-1.informal.ja \
-f formality-control.test.en-ja.formal.annotated.ja \
-if formality-control.test.en-ja.informal.annotated.ja \
-nd
Formal Acc: 0.160, Informal Acc: 0.840
```

## Pre-trained models

Pre-trained baseline models are available on the task's GitHub repository.
See the "Assets" section of the [releases page](https://github.com/amazon-research/contrastive-controlled-mt/releases).

Each model is trained on open datasets using the [Sockeye 3 PyTorch NMT toolkit](https://github.com/awslabs/sockeye). For further details see [Pre-trained models](./models/README.md#setup)

### License

If you use any of the pre-trained models, please note that the datasets that they were trained on come with the following licensing:

|Dataset	|Language pair	|	License	|
|---	|---	|---		|
|Paracrawl v9 |EN-DE,ES	| CC0
|CCMatrix |EN-HI	| CC0
|Wikimatrix	|EN-JA	|CC BY SA 3.0
|JESC  |EN-JA	| CC BY SA 4.0

Note, EN-JA models were also trained on the news commentary dataset and users should cite [6] in addition to [4,5] if using the EN-JA models. Please cite [1,2] if you use the EN-HI model and [3] if you use the EN-DE,ES models.

## Citation

If you are a participant in the IWSLT shared task on Formality Control for SLT, or are otherwise using the resources 
from this repository in your work, please cite `[citation instructions to follow]`

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

## References

[1] Angela Fan, Shruti Bhosale, Holger Schwenk, Zhiyi Ma, Ahmed El-Kishky, Siddharth Goyal, Mandeep Baines, Onur Celebi, Guillaume Wenzek, Vishrav Chaudhary, Naman Goyal, Tom Birch, Vitaliy Liptchinsky, Sergey Edunov, Edouard Grave, Michael Auli, and Armand Joulin. [Beyond English-Centric Multilingual Machine Translation](https://arxiv.org/abs/2010.11125)

[2] Holger Schwenk, Guillaume Wenzek, Sergey Edunov, Edouard Grave and Armand Joulin, [CCMatrix: Mining Billions of High-Quality Parallel Sentences on the WEB](https://arxiv.org/abs/1911.04944)

[3] Marta Bañón, Pinzhen Chen, Barry Haddow, Kenneth Heafield, Hieu Hoang, Miquel Esplà-Gomis, Mikel L. Forcada, Amir Kamran, Faheem Kirefu, Philipp Koehn, Sergio Ortiz Rojas, Leopoldo Pla Sempere, Gema Ramírez-Sánchez, Elsa Sarrías, Marek Strelec, Brian Thompson, William Waites, Dion Wiggins, Jaume Zaragoza, [ParaCrawl: Web-Scale Acquisition of Parallel Corpora](https://aclanthology.org/2020.acl-main.417/)

[4] Pryzant, R. and Chung, Y. and Jurafsky, D. and Britz , D. [JESC: Japanese-English Subtitle Corpus](https://arxiv.org/abs/1710.10639)

[5] Holger Schwenk, Vishrav Chaudhary, Shuo Sun, Hongyu Gong and Paco Guzman,[WikiMatrix: Mining 135M Parallel Sentences in 1620 Language Pairs from Wikipedia](https://arxiv.org/abs/1907.05791) arXiv, July 11 2019.

[6] J. Tiedemann, 2012, [Parallel Data, Tools and Interfaces in OPUS.](https://opus.nlpl.eu/News-Commentary.php) In Proceedings of the 8th International Conference on Language Resources and Evaluation (LREC 2012)