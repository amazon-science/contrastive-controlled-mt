# CoCoA-MT: A Dataset and Benchmark for Contrastive Controlled MT with Application to Formality

This directory contains the CoCoA-MT (**Co**ntrastive **Co**ntrolled **MT** by **A**WS AI) dataset from the NAACL 2022 paper: [CoCoA-MT: A Dataset and Benchmark for Contrastive Controlled MT with Application to Formality](https://aclanthology.org/2022.findings-naacl.47/).

## Dataset

Each English source segment was choosen from one of three domains: Topical-Chat, Telephony or Call Center. 
- Topical-Chat consists of text-based conversations about various topics, such as fashion, books, sports, and music.
- Telephony contains transcribed spoken general conversations with unrestricted topic. 
- Call Center data is comprised of transcribed spoken data, where the conversations come from simulated customer support scenarios.

For each source segment, we collected one reference translation for each level of formality (formal and informal). For Japanese, where more than two formality levels are possible, informal was mapped to kudaketa and formal to teineigo. Reference translations were created by professional translators who were native speakers of the specified language and geographic variant.  Translators were instructed to generate natural translations that preserve the meaning and tone of the original sentence while addressing formality with minimal required changes. Such changes included swapping pronouns, editing verb forms, and additional lexical changes to obtain natural-sounding translations.  Annotators also provided phrase-level annotations of formality markers in the target segments in order to facilitate evaluation and analysis

For each language pair, we release test data for all three domains (Topical-Chat, Telephony, and Call Center), and training data for Topical-Chat and Telephony. All segments in the test data have distinct formal/informal references, while the training data contains some segments with identical references for both formality levels.

For further details see the [paper](https://aclanthology.org/2022.findings-naacl.47/).


## Citing
If you use this dataset in your research, please cite the following publication:
```
@inproceedings{nadejde-etal-2022-cocoa,
    title = "{C}o{C}o{A}-{MT}: A Dataset and Benchmark for Contrastive Controlled {MT} with Application to Formality",
    author = "Nadejde, Maria  and
      Currey, Anna  and
      Hsu, Benjamin  and
      Niu, Xing  and
      Federico, Marcello  and
      Dinu, Georgiana",
    booktitle = "Findings of the Association for Computational Linguistics: NAACL 2022",
    month = jul,
    year = "2022",
    address = "Seattle, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-naacl.47",
    pages = "616--632"
}
```

## License

This project is licensed under the CDLA-Sharing-1.0 License.
