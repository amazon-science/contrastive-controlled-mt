# UMD Submission to IWSLT22 Formality Control

## System Descriptions:

All approaches use some form of [additive interventions](https://aclanthology.org/2021.emnlp-main.535/) with varying pretrained models and amount of synthetic and gold standard supervision. Each system is a one-to-many multilingual translation model with controllable formality (neutral, formal, and informal). mT5 models are all finetuned google/mT5-large models from Hugging Face. The mBART model is a finetuned model based on facebook/mbart-large-50-one-to-many-mmt in Hugging Face. The specifics are as follows:

1. mT5-two-pass-finetuned (primary)

    - In this approach, mT5 is finetuned with two-pass fine-tuning: first on synthetic formality labels for seen languages and masked formality labels for unseen languages, then on gold standard contrastive examples for seen languages and formality-masked non-contrastive examples for unseen languages.

2. mT5-synthetic-finetuned

    - In this approach, mT5 is finetuned only with synthetic formality labels for seen languages and formality-masked examples for unseen languages.

3. mT5-gold-finetuned

    - In this approach, mT5 is finetuned only with gold standard contrastive examples for seen languages and no parallel data for unseen languages.

4. mBART-gold-finetuned

    - In this approach, mBART is finetuned only with gold standard contrastive examples for seen languages and no parallel data for unseen languages.

5. mT5-two-pass-finetuned-supervised

    - In this approach, mT5 is finetuned with two-pass fine-tuning: first on synthetic formality labels for seen languages and masked formality labels for unseen languages, then on gold standard contrastive examples for seen languages and silver standard formality labeled non-contrastive examples for unseen languages.

## Results

For each system we report the BLEU and COMET scores on the generic test set. To better understand the performance across formality levels (i.e., to account for varying formality in the references), we report scores for each formality level that each system can produce. The results are as follows:

### System 1:

| Target (formality) | BLEU (Tokenizer) |  COMET  |
|--------------------|------------------|---------|
| de (neutral)       | 22.4 (13a)       |  0.1610 |
| es (neutral)       | 27.8 (13a)       |  0.3437 |
| hi (neutral)       | 12.1 (13a)       |  0.1922 |
| it (neutral)       | 22.9 (13a)       |  0.2465 |
| ja (neutral)       | 11.6 (ja-mecab)  | -0.0227 |
| ru (neutral)       | 14.4 (13a)       |  0.0748 |
|                    |                  |         |
| de (formal)        | 22.7 (13a)       |  0.1654 |
| es (formal)        | 27.6 (13a)       |  0.3434 |
| hi (formal)        | 12.0 (13a)       |  0.1785 |
| it (formal)        | 22.9 (13a)       |  0.2485 |
| ja (formal)        | 10.6 (ja-mecab)  | -0.0321 |
| ru (formal)        | 14.1 (13a)       |  0.0740 |
|                    |                  |         |
| de (informal)      | 21.6 (13a)       |  0.1434 |
| es (informal)      | 27.8 (13a)       |  0.3628 |
| hi (informal)      | 12.0 (13a)       |  0.1835 |
| it (informal)      | 22.5 (13a)       |  0.2633 |
| ja (informal)      | 12.0 (ja-mecab)  | -0.0324 |
| ru (informal)      | 14.4 (13a)       |  0.0749 |


### System 2:

| Target (formality) | BLEU (Tokenizer) |  COMET  |
|--------------------|------------------|---------|
| de (neutral)       | 20.9 (13a)       |  0.1890 |
| es (neutral)       | 27.3 (13a)       |  0.3784 |
| hi (neutral)       | 13.4 (13a)       |  0.2246 |
| it (neutral)       | 23.8 (13a)       |  0.3328 |
| ja (neutral)       | 11.3 (ja-mecab)  | -0.1025 |
| ru (neutral)       | 15.1 (13a)       |  0.0998 |
|                    |                  |         |
| de (formal)        | 21.1 (13a)       |  0.1807 |
| es (formal)        | 27.1 (13a)       |  0.3691 |
| hi (formal)        | 13.3 (13a)       |  0.2237 |
| it (formal)        | 23.9 (13a)       |  0.3336 |
| ja (formal)        | 11.0 (ja-mecab)  | -0.1020 |
| ru (formal)        | 15.0 (13a)       |  0.1030 |
|                    |                  |       |
| de (informal)      | 20.5 (13a)       |  0.1948 |
| es (informal)      | 27.3 (13a)       |  0.3861 |
| hi (informal)      | 13.4 (13a)       |  0.2268 |
| it (informal)      | 23.7 (13a)       |  0.3391 |
| ja (informal)      | 11.7 (ja-mecab)  | -0.1142 |
| ru (informal)      | 15.2 (13a)       |  0.1021 |

### System 3:

| Target (formality) | BLEU (Tokenizer) |  COMET  |
|--------------------|------------------|---------|
| de (neutral)       | 2.60 (13a)       | -1.6578 |
| es (neutral)       | 2.10 (13a)       | -1.5342 |
| hi (neutral)       | 0.70 (13a)       | -1.4725 |
| it (neutral)       | 0.20 (13a)       | -1.6813 |
| ja (neutral)       | 2.30 (ja-mecab)  | -1.3112 |
| ru (neutral)       | 0.10 (13a)       | -1.8590 |
|                    |                  |         |
| de (formal)        | 3.20 (13a)       | -1.5450 |
| es (formal)        | 2.70 (13a)       | -1.4350 |
| hi (formal)        | 0.90 (13a)       | -1.4452 |
| it (formal)        | 0.30 (13a)       | -1.6047 |
| ja (formal)        | 1.90 (ja-mecab)  | -1.2410 |
| ru (formal)        | 0.20 (13a)       | -1.7797 |
|                    |                  |         |
| de (informal)      | 3.30 (13a)       | -1.5012 |
| es (informal)      | 2.90 (13a)       | -1.3134 |
| hi (informal)      | 0.80 (13a)       | -1.4326 |
| it (informal)      | 0.30 (13a)       | -1.5592 |
| ja (informal)      | 2.60 (ja-mecab)  | -1.2111 |
| ru (informal)      | 0.10 (13a)       | -1.7893 |

### System 4:

| Target (formality) | BLEU (Tokenizer) |  COMET  |
|--------------------|------------------|---------|
| de (neutral)       | 29.0 (13a)       |  0.4867 |
| es (neutral)       | 30.2 (13a)       |  0.5429 |
| hi (neutral)       | 15.2 (13a)       |  0.5800 |
| it (neutral)       | 30.8 (13a)       |  0.5854 |
| ja (neutral)       | 19.3 (ja-mecab)  |  0.4134 |
| ru (neutral)       | 19.0 (13a)       |  0.3863 |
|                    |                  |         |
| de (formal)        | 29.0 (13a)       |  0.4877 |
| es (formal)        | 30.1 (13a)       |  0.5418 |
| hi (formal)        | 15.1 (13a)       |  0.5783 |
| it (formal)        | 30.9 (13a)       |  0.5811 |
| ja (formal)        | 18.4 (ja-mecab)  |  0.4229 |
| ru (formal)        | 19.1 (13a)       |  0.3814 |
|                    |                  |         |
| de (informal)      | 28.2 (13a)       |  0.4805 |
| es (informal)      | 30.3 (13a)       |  0.5452 |
| hi (informal)      | 15.0 (13a)       |  0.5775 |
| it (informal)      | 30.6 (13a)       |  0.5819 |
| ja (informal)      | 19.4 (ja-mecab)  |  0.4155 |
| ru (informal)      | 19.0 (13a)       |  0.3785 |

### System 5:

| Target (formality) | BLEU (Tokenizer) |  COMET  |
|--------------------|------------------|---------|
| de (neutral)       | 22.1 (13a)       |  0.1572 |
| es (neutral)       | 27.7 (13a)       |  0.3429 |
| hi (neutral)       | 12.1 (13a)       |  0.1777 |
| it (neutral)       | 22.8 (13a)       |  0.2638 |
| ja (neutral)       | 11.7 (ja-mecab)  | -0.0129 |
| ru (neutral)       | 14.2 (13a)       |  0.0063 |
|                    |                  |         |
| de (formal)        | 22.8 (13a)       |  0.1679 |
| es (formal)        | 27.6 (13a)       |  0.3332 |
| hi (formal)        | 12.0 (13a)       |  0.1780 |
| it (formal)        | 22.8 (13a)       |  0.2419 |
| ja (formal)        | 10.8 (ja-mecab)  | -0.0439 |
| ru (formal)        | 13.8 (13a)       |  0.0082 |
|                    |                  |         |
| de (informal)      | 21.7 (13a)       |  0.1681 |
| es (informal)      | 27.8 (13a)       |  0.3512 |
| hi (informal)      | 11.9 (13a)       |  0.1776 |
| it (informal)      | 22.6 (13a)       |  0.2441 |
| ja (informal)      | 12.3 (ja-mecab)  | -0.0008 |
| ru (informal)      | 13.9 (13a)       |  0.0039 |

## Data Sources

We sample at most an addtional 15k examples for each language pair from the following data sources (shown by target language):

| Language Pair | Source                       |
|---------------|----------------------------- |
|Japanese       | JParacrawl                   |
|Hindi          | CCMatrix                     |
|Italian        | Paracrawl v8                 |
|Russian        | Paracrawl v8                 |
|German         | CommonCrawl, Europarl v7     |
|Spanish        | CommonCrawl, UN, Europarl v7 |


## Training Conditions

All systems are submitted under the unconstrained setting.

Systems 3 and 4 are fine-tuned solely on task-data and thus are evaluated in completely zero-shot fashion, both for translation and formality transfer.

Systems 1 and 2 are trained on additional out-of-domain data sampled from the various copora described above. The data selection strategy for generating the synthetic datasets for all the language pairs is described below:

The selection strategy is a mixture of rule-based and classifier-based (in the case of German and Spanish), classifier-based only (Japanese, Hindi), and rule-based only (Russian, Italian).  In the case of seen languages, heuristics are applied to give a silver-standard formality label based on morphological features, exact-match keywords, and classifier probabilities of certain formality levels.  In unseen languages, heuristics are applied only to ensure the quality of the data (non-sentences are removed based on crude rules). 

System 2 is fine-tuned with task-data and a small amount of resampled first-pass parallel data for en-it and en-ru to prevent catastrophic forgetting of translation in these language pairs while still masking the formality tag in the additive intervention, resulting in the primary submission, System 1. 

Thus, for systems 1-3 we only use translation supervision signal for the unseen languages, but expect formality to be learned via multilingual transfer. System 4 only uses task data to achieve formality transfer without translation signal for unseen languages.

System 5 is trained on the same first-pass fine-tuning data as systems 1 and 2, but also includes second-pass fine-tuning data sampled from the top 10% and bottom 10% of the formality distribution as learned by our classifier. The labels in the top 10% of P(informal) are given a silver label of informal and similarly for the bottom 10% with a formal label. Thus, this model is submitted as a fully supervised model.

Thus, we expect system 5 to show us what could be gained from some amount of direct supervision (T/V distinction) over zero-shot approaches.

## Participants

- [Elijah Rippeth](mailto:erip@cs.umd.edu)
- [Sweta Agrawal](mailto:sweagraw@cs.umd.edu)

## License

These system outputs are licensed under MIT and the participants hereby consent to their release for future research and human evaluations subject to the license agreement.
