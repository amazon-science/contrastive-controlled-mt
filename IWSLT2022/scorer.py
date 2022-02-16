# Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import argparse
from collections import defaultdict
import re
from typing import List, Pattern, Tuple

FORMALITY_PHRASES = re.compile("(\[F\](.*?)\[/F\])")

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-hyp",
        "--hypotheses",
        type=str,
        help="File containing system detokenized output translations"
    )
    parser.add_argument(
        "-f",
        "--formal_refs",
        type=str,
        help="File containing formal references with annotated grammatical formality"
    )
    parser.add_argument(
        "-if",
        "--informal_refs",
        type=str,
        help="File containing informal references with annotated grammatical formality."
    )
    parser.add_argument(
        "-nd",
        "--non_whitespace_delimited",
        action="store_true",
        help="If the target language tokens are non-whitespace delimited (e.g. for Japanese)"
    )

    return parser.parse_args()

def compute_score(
    hypotheses: str,
    annotated_formal_refs: str,
    annotated_informal_refs: str,
    tok_split: bool=True
) -> Tuple[float, float]:
    """
    Compute formal and informal matched-accuracy scores.

    Args:
        hypothesis: file containing system detokenized output translations
        annotated_formal_refs: formal reference file with annotated grammatical formality
        annotated_informal_refs: informal reference file with annotated grammatical formality
        tok_split: Split hypotheses and references into tokens before phrase matching.

    Returns:
        (formal_acc, informal_acc), the formal accuracy and informal matched-accuracy scores respectively.
    """
    hypotheses = _read_lines(hypotheses)
    annotated_references_formal = _read_lines(annotated_formal_refs)
    annotated_references_informal = _read_lines(annotated_informal_refs)

    if not (len(hypotheses) == len(annotated_references_formal) == len(annotated_references_informal) > 0):
        raise RuntimeError("Empty or mismatched hypotheses and reference files.")

    scores = defaultdict(int)
    for hyp, ref_formal, ref_informal in zip(hypotheses, annotated_references_formal, annotated_references_informal):
        formal_phrases = get_matching_phrases(hyp, ref_formal, tok_split, FORMALITY_PHRASES)
        informal_phrases = get_matching_phrases(hyp, ref_informal, tok_split, FORMALITY_PHRASES)

        label = predict_formality_label(formal_phrases, informal_phrases)
        
        scores[f"ref_matched_count_{label}"] += 1

    n_matched = scores["ref_matched_count_INFORMAL"] + scores["ref_matched_count_FORMAL"]
    formal_acc = scores["ref_matched_count_FORMAL"]/n_matched if n_matched>0 else 0
    informal_acc = scores["ref_matched_count_INFORMAL"]/n_matched if n_matched>0 else 0

    return formal_acc, informal_acc


def get_matching_phrases(
    hyp: str,
    anno_ref: str,
    tok_split: bool=True,
    phrase_regex: Pattern=FORMALITY_PHRASES
):
    """
    Get annotated phrases that match in the hypothesis.

    Args:
        hyp: system hypothesis
        anno_ref: reference translation with annotated grammatical register
        tok_split: whether phrases should be split (on whitespace) into tokens before phrase matching
        phrase_regex: regular expression for finding references.

    Returns:
        list of annotated phrases occuring in the hypothesis.
    """
    anno_ph = re.findall(phrase_regex, anno_ref)
    if not tok_split:
        anno_ph_hyp = [ph for _, ph in anno_ph if ph in hyp]
    else:
        anno_ph_hyp = [ph for _, ph in anno_ph if set(ph.split(" ")).issubset(hyp.split(" "))]
    return anno_ph_hyp


def predict_formality_label(
    ph_formal_hyp: List[str],
    ph_informal_hyp: List[str]
) -> str:
    """
    Predict the formality label depending on the number of matched formal/informal phrases.

    Args:
        ph_formal_hyp: list of phrases in the hypothesis matching annotated formal reference phrases
        ph_informal_hyp: list of phrases in the hypothesis matching annotated informal reference phrases

    Returns:
        formality label, "FORMAL","INFORMAL","OTHER","NEUTRAL"
    """
    if ph_formal_hyp and not ph_informal_hyp:
        return "FORMAL"
    elif ph_informal_hyp and not ph_formal_hyp:
        return "INFORMAL"
    elif not ph_informal_hyp and not ph_formal_hyp:
        return "NEUTRAL"
    return "OTHER"

def _read_lines(file: str) -> List[str]:
    with open(file, "r", encoding="utf-8") as file:
        raw_text = [line.strip() for line in file.readlines()]

    return raw_text


if __name__ == "__main__":
    args = parse_args()
    whitespace_delimited_tokens = not args.non_whitespace_delimited

    formal_acc, informal_acc = compute_score(
        args.hypotheses, args.formal_refs, args.informal_refs, tok_split=whitespace_delimited_tokens
    ) 
    print(f"Formal Acc: {formal_acc:.3f}, Informal Acc: {informal_acc:.3f}")
