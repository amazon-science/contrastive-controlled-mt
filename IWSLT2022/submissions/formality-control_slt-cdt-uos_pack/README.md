<!-- README.md with the following information

    Brief description of each system submitted, including which system they prefer for final evaluation by the organizers
    System performance on the generic test set as computed by the participant
    Training data conditions (constrained/unconstrained; full/zero-shot)
    List of the data sources used for training the system
    Institution and contact person
 -->
 # Team slt-cdt-uos Submission to the Special Task on Formality Control in SLT
 ------------
 ## General information
 
 All our submitted systems concern the following language pairs:
 - EN-DE
 - EN-ES
 - EN-RU
 - EN-IT
 
 We assumed the following task/track split:
 - constrained task:
    - full supervision track
    - zero-shot track
 - unconstrained task:
    - full supervision track
    - zero-shot track
 
 Within this repository we submit **one final system per each track** within each task. No other systems are submitted as part of this campaign; the system description paper, however, will include some internally computed results on the validation set (made available on 14/01/22 by IWSLT-22) and MuST-C development test.

## Brief description of each system submitted

Note: all submitted systems are essentially the same architecture/idea adapted to different data/supervision configurations.\
Description of Systems 2-4 is provided in two ways: i) how it is different w.r.t. previous descriptions, esp. System 1 (for brevity), and ii) a full, independent description of that system (e.g. for Findings).

 ### System 1: constrained, full supervision
 This system used a sentence-level tagging system for formality marking; one multilingual system (the standard 6-layer Transformer architecture; EN-to-DE,ES,RU,IT) is pretrained on the MuST-C corpus and then fine-tuned in a fully supervised way on data annotated as formal/informal. The data itself comes from the MuST-C corpus. Most similar samples from this corpus to the formal/informal IWSLT data are labelled as formal/informal; similarity is computed with the Moore-Lewis algorithm; most similar sentence pairs are extracted using a relative position difference method. The final model is an average of 10 consecutive checkpoints which achieve the best formal/informal accuracy on the IWSLT data (for EN-DE,ES). During inference, we use a large beam width k for beam search and generate k-best hypotheses; we use a relative frequency model trained on the IWSLT data to re-rank the k hypotheses before choosing the top1 as the output hypothesis. For the "zero-shot" pairs (EN-RU, EN-IT) we use a sample of our own extracted training data for the relative frequency model.

 ### System 2: constrained, zero shot
 This system follows all specification of System 1, but during fine-tuning we **only** use EN-DE, EN-ES formality-labelled data. We repeat the model selection and reranking steps.
 
 (Full description, if needed for Findings)
 This system used a sentence-level tagging system for formality marking; one multilingual system (the standard 6-layer Transformer architecture; EN-to-DE,ES,RU,IT) is pretrained on the MuST-C corpus and then fine-tuned in a fully supervised way on data annotated as formal/informal for the fully supervised language pairs (EN-DE, EN-ES). The data itself comes from the MuST-C corpus. Most similar samples from this corpus to the formal/informal IWSLT data are labelled as formal/informal; similarity is computed with the Moore-Lewis algorithm; most similar sentence pairs are extracted using a relative position difference method. The final model is an average of 10 consecutive checkpoints which achieve the best formal/informal accuracy on the IWSLT data (for EN-DE,ES). During inference, we use a large beam width k for beam search and generate k-best hypotheses; we use a relative frequency model trained on the IWSLT data to re-rank the k hypotheses before choosing the top1 as the output hypothesis. The "zero-shot" language pairs (EN-RU, EN-IT) are never fine-tuned in the formality aspect, but are included in the re-ranking step. Since no training data was provided for these pairs, we use a sample of our own extracted training data for the relative frequency model for EN-RU and EN-IT.
 
 
 ### System 3: unconstrained, fully supervised
 This system follows all specifications of System 1, with the following differences:
 - it uses all corpora permitted for the unconstrained task
 - We extract the formality data not from the entire training set, but from 5M sentence pairs most similar to the MuST-C corpus (per language pair).
 
  (Full description, if needed for Findings)
 This system is trained on a large concatenation of permitted corpora. This dataset is cleaned using BiCleaner; one multilingual system (the standard 6-layer Transformer architecture; EN-to-DE,ES,RU,IT) is pre-trained on this dataset. It is then fine-tuned on a formality-labelled corpus, using formality tags appended to each source sentence. To create the formality-labelled corpus, we first prune the training set, seeing as most of it is not dialogue: we extract 5M most similar sentence pairs to the MuST-C corpus using the Moore-Lewis algorithm, yielding corpus U_5M. Most similar samples from U_5M to the formal/informal IWSLT data are labelled as formal/informal; similarity is computed with the Moore-Lewis algorithm; most similar sentence pairs are extracted using a relative position difference method. The final model is an average of 10 consecutive checkpoints which achieve the best formal/informal accuracy on the IWSLT data (for EN-DE,ES). During inference, we use a large beam width k for beam search and generate k-best hypotheses; we use a relative frequency model trained on the IWSLT data to re-rank the k hypotheses before choosing the top1 as the output hypothesis. For the "zero-shot" pairs (EN-RU, EN-IT) we use a sample of our own extracted training data for the relative frequency model.

 ### System 4: unconstrained, zero shot
 This system follows all specifications of System 2 and the adaptations to the unconstrained task of System 4.
 
  (Full description, if needed for Findings)
 This system is trained on a large concatenation of permitted corpora. This dataset is cleaned using BiCleaner; one multilingual system (the standard 6-layer Transformer architecture; EN-to-DE,ES,RU,IT) is pre-trained on this dataset. It is then fine-tuned in a fully supervised way on data annotated as formal/informal for the fully supervised language pairs (EN-DE, EN-ES). To create the formality-labelled corpus, we first prune the training set, seeing as most of it is not dialogue: we extract 5M most similar sentence pairs to the MuST-C corpus using the Moore-Lewis algorithm, yielding corpus U_5M. Most similar samples from U_5M to the formal/informal IWSLT data are labelled as formal/informal; similarity is computed with the Moore-Lewis algorithm; most similar sentence pairs are extracted using a relative position difference method. The final model is an average of 10 consecutive checkpoints which achieve the best formal/informal accuracy on the IWSLT data (for EN-DE,ES). During inference, we use a large beam width k for beam search and generate k-best hypotheses; we use a relative frequency model trained on the IWSLT data to re-rank the k hypotheses before choosing the top1 as the output hypothesis. The "zero-shot" language pairs (EN-RU, EN-IT) are never fine-tuned in the formality aspect, but are included in the re-ranking step. Since no training data was provided for these pairs, we use a sample of our own extracted training data for the relative frequency model for EN-RU and EN-IT.
 
 ## System performance: constrained task

 ### Automatic metrics against MuST-C generic test set (tst-COMMON)
| System      | Lang. pair  | BLEU         | COMET v1.0.1 |
| ----------- | ----------- | ------------ | ------------ | 
| System 1    | EN-DE       | 31.50        | 0.4477       | 
|             | EN-ES       | 36.53        | 0.6076       | 
|             | EN-RU       | 21.41        | 0.3311       | 
|             | EN-IT       | 33.28        | 0.5676       | 
| System 2    | EN-DE       | 31.25        | 0.4368       | 
|             | EN-ES       | 36.65        | 0.6108       | 
|             | EN-RU       | 21.43        | 0.3298       | 
|             | EN-IT       | 33.15        | 0.5525       | 

 ### Scores computed by scorer.py on train IWSLT formality-annotated data (used by us as the development set):
(Note: we report the value for the style that was used as desired in output. e.g. for formal translation, we report Formal Acc)
System 1:
- EN-DE:
	- formal: 1.000
	- informal: 0.956
- EN-ES:
	- formal: 0.899
	- informal: 0.990

System 2:
- EN-DE:
	- formal: 0.996
	- informal: 0.942
- EN-ES:
	- formal: 0.850
	- informal: 0.990

 ## System performance: unconstrained task

# Automatic metrics against MuST-C generic test set (tst-COMMON)
| System      | Lang. pair  | BLEU         | COMET v1.0.1 |
| ----------- | ----------- | ------------ | ------------ |
| System 3    | EN-DE       | 32.50        | 0.4972       | 
|             | EN-ES       | 36.98        | 0.6349       | 
|             | EN-RU       | 22.01        | 0.3846       | 
|             | EN-IT       | 33.56        | 0.5927       | 
| System 4    | EN-DE       | 32.47        | 0.4851       | 
|             | EN-ES       | 36.83        | 0.6209       | 
|             | EN-RU       | 21.45        | 0.3565       | 
|             | EN-IT       | 33.12        | 0.5623       | 

 ### Scores computed by scorer.py on train IWSLT formality-annotated data (used by us as the development set):
(Note: we report the value for the style that was used as desired in output. e.g. for formal translation, we report Formal Acc)
System 3:
- EN-DE:
	- formal: 1.000
	- informal: 1.000
- EN-ES:
	- formal: 0.995
	- informal: 1.000

System 4:
- EN-DE:
	- formal: 1.000
	- informal: 1.000
- EN-ES:
	- formal: 0.991
	- informal: 0.996


 
 ## List of data sources used for training the systems
 
 ### Constrained task
 - The MuST-C v1.2 corpus (textual)
 - Annotated IWSLT-22 formality data (used mainly for validation)

 ### Unconstrained task
 All data from the Constrained task plus
 - Paracrawl v9
 - WMT*:
    - EN-DE
        - Europarl v10
        - NewsCommentary v16
        - WikiTitles v3
        - TildeRapid 2016
        - WikiMatrix v1
        - CommonCrawl
    - EN-ES
        - Europarl v7
        - NewsCommentary v16
        - UN (2000)
        - CommonCrawl
    - EN-RU
        - NewsCommentary v16
        - WikiTitles v3
        - WikiMatrix v1
        - Yandex
        - CommonCrawl
    - EN-IT
        - Europarl v7
        - NewsCommentary v16
 
 \* All corpora listed here are **all** the available WMT corpora listed by the organisers of this task.
 
 ## Institution and contact person
 **Team name:**         Speech and Language Technologies CDT @ The University of Sheffield\
 **Short team name:**   slt-cdt-uos

 #### Institution:
 
 Department of Computer Science at The University of Sheffield\
 Regent Court, The University of Sheffield,\
 211 Portobello\
 Sheffield \
 S1 4DP\
 United Kingdom
 
 #### Consent
 We consent with the system outputs being released under an MIT license.
 
 #### Contact Person:
 Sebastian Vincent\
 e-mail: stvincent1@sheffield.ac.uk
 
 #### 2nd Contact Person:
 Carolina Scarton\
 e-mail: c.scarton@sheffield.ac.uk
 

