#!/usr/bin/env python3

from statistics import mean
from argparse import ArgumentParser, FileType

from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

def setup_argparse():
    parser = ArgumentParser()
    parser.add_argument("-m", "--model-name", type=str, required=True, help="The path to the XLMR-based formality classifier.")
    parser.add_argument("-t", "--target-formality", choices=("formal", "informal"), required=True, help="The formality level of the generated outputs.")
    parser.add_argument("-i", "--input-stream", type=FileType("r"), default="-", help="The stream of system hypotheses.")
    parser.add_argument("-bs", "--batch-size", type=int, default=32, help="The batch size for inference.")
    parser.add_argument("-d", "--device", type=str, default="cpu", help="The device on which to run inference.")
    return parser 

if __name__ == "__main__":
    args = setup_argparse().parse_args()

    model_name = args.model_name
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    expected_label = "LABEL_0" if args.target_formality == "informal" else "LABEL_1"

    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    
    pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, batch_size=args.batch_size, device=args.device)
    text = [line.strip() for line in args.input_stream]
    scores = pipe(text)
    print(mean((e["label"] == expected_label for e in scores)))
