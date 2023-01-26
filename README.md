## CoCoA-MT: A Dataset and Benchmark for Contrastive Controlled MT with Application to Formality

The machine translation (MT) task is typically formulated as that of returning a single translation for an input segment. However, in many cases, multiple different translations are valid and the appropriate translation may depend on the intended target audience, characteristics of the speaker, or even the relationship between speakers. Specific problems arise when dealing with honorifics, particularly translating from English into languages with formality markers. For example, the sentence "Are you sure?" can be translated in German as "Sind Sie sich sicher?" (formal register) or "Bist du dir sicher?" (informal). Using wrong or inconsistent tone may be perceived as inappropriate or jarring for users of certain cultures and demographics. This work addresses the problem of learning to control target language attributes, in this case formality, from a small amount of labeled contrastive data. We introduce an annotated dataset (CoCoA-MT) and an associated evaluation metric for training and evaluating formality-controlled MT models for six diverse target languages.

## IWSLT 2022 shared task 
Participants to the [Formality Control for SLT](https://iwslt.org/2022/formality) shared task can find the annotated dataset and evaluation script under [IWSLT2022/](/IWSLT2022/). 


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This project is licensed under the CDLA-Sharing-1.0 License.

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
