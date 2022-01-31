# Pre-Trained Models

Pre-trained baseline models are available on the task's GitHub repository.
See the "Assets" section of the [releases page](https://github.com/amazon-research/contrastive-controlled-mt/releases).

Each model is trained on a sample of 20 million lines from the [Paracrawl Corpus (V9)](https://paracrawl.eu/) using the [Sockeye NMT toolkit](https://github.com/awslabs/sockeye).
Models use architectures and training recipes described by Vaswani et al. ([2017](https://papers.nips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)), Ott et al. ([2018](https://aclanthology.org/W18-6301/)), Kim et al. ([2019](https://aclanthology.org/D19-5632/)), and Domhan et al. ([2020](https://aclanthology.org/2020.amta-research.10/)): big transformers with 20 encoder layers, 2 decoder layers, SSRUs in place of decoder self-attention, and large batch training.

For more information, see the [Sockeye GitHub page](https://github.com/awslabs/sockeye) and linked publications.

## Setup

To get started, install the version of [PyTorch](https://pytorch.org/get-started/locally/) for your environment (OS, compute platform, etc.).

Next install [Sockeye](https://github.com/awslabs/sockeye) and the tools used for data pre-processing: [SacreMoses](https://github.com/alvations/sacremoses) and [Subword NMT](https://github.com/rsennrich/subword-nmt).
Specifying the version of SacreMoses is important because tokenization rules can change between versions.

```bash
pip3 install sockeye sacremoses==0.0.43 subword-nmt
```

## Example: Fine-Tuning

In this example, we fine-tune the pre-trained English-German model on formal chat data.
The following steps can be adapted to other language pairs, domains, and formality types.

First we split the data (200 lines total) into train, dev, and test sets.

```bash
head -n100 formality-control.train.topical-chat.en-de.en >train.en
head -n100 formality-control.train.topical-chat.en-de.formal.de >train.de
tail -n100 formality-control.train.topical-chat.en-de.en |head -n50 >dev.en
tail -n100 formality-control.train.topical-chat.en-de.formal.de |head -n50 >dev.de
tail -n100 formality-control.train.topical-chat.en-de.en |tail -n50 >test.en
tail -n100 formality-control.train.topical-chat.en-de.formal.de |tail -n50 >test.de
```

We then pre-process the data using the same settings as the pre-trained model's original training data.

(1) Tokenize the raw data using the appropriate two-letter language code ("en" for English, "de" for German, etc.).

```bash
for SET in train dev test; do
  sacremoses -l en tokenize -x <$SET.en >$SET.en.tok
  sacremoses -l de tokenize -x <$SET.de >$SET.de.tok
done
```

(2) Byte-pair encode the tokenized data using the codes distributed with the pre-trained model.

```bash
for SET in train dev test; do
  subword-nmt apply-bpe --codes model.en-de/bpe_codes <$SET.en.tok >$SET.en.tok.bpe
  subword-nmt apply-bpe --codes model.en-de/bpe_codes <$SET.de.tok >$SET.de.tok.bpe
done
```

Before fine-tuning, we establish a baseline score by translating the test set with the pre-trained model.

```bash
sockeye-translate -m model.en-de --input test.en.tok.bpe --output out.baseline.tok.bpe
sed -re 's/@@( |$)//g' <out.baseline.tok.bpe >out.baseline.tok
sacremoses -l de detokenize -x <out.baseline.tok >out.baseline
sacrebleu test.de <out.baseline
```

The baseline result is 33.2 BLEU.

Next we convert the training data into Sockeye's binary format using the vocabulary from the pre-trained model.

```bash
sockeye-prepare-data --source train.en.tok.bpe --target train.de.tok.bpe --source-vocab model.en-de/vocab.src.0.json --target-vocab model.en-de/vocab.trg.0.json --shared-vocab --output prepared
```

Now we're ready to run Sockeye training.  We use the following key settings:

- By default, copy all settings from the pre-trained model (`--config model.en-de/args.yaml`)
- Initialize model parameters with the values from the pre-trained model, our starting point for fine-tuning (`--params model.en-de/params.best`)
- Because our data is small (100 lines), use a small learning rate with frequent checkpoints (`--initial-learning-rate 0.00001 --checkpoint-interval 10`)
- Train until we see no improvement on dev set perplexity for 5 checkpoints (`--max-num-checkpoint-not-improved 5`)

```bash
torchrun --no_python --nproc_per_node 1 sockeye-train --config model.en-de/args.yaml --prepared-data prepared --validation-source dev.en.tok.bpe --validation-target dev.de.tok.bpe --output model.en-de.adapt --params model.en-de/params.best --learning-rate-scheduler none --initial-learning-rate 0.00001 --batch-size 1024 --update-interval 1 --checkpoint-interval 10 --max-num-checkpoint-not-improved 5
```

Once training finishes, we use the fine-tuned model to translate the test set and compare the result to the baseline.

```bash
sockeye-translate -m model.en-de.adapt --input test.en.tok.bpe --output out.adapt.tok.bpe
sed -re 's/@@( |$)//g' <out.adapt.tok.bpe >out.adapt.tok
sacremoses -l de detokenize -x <out.adapt.tok >out.adapt
sacrebleu test.de <out.adapt
```

We see that the BLEU score improves from 33.2 to 48.2--not bad for 100 lines of training data!
