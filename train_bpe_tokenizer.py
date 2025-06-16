#!/usr/bin/env python3
"""
Script to train a byte-level BPE tokenizer on TinyStories dataset.
"""

import time
import pickle
from pathlib import Path
from tests.adapters import run_train_bpe


def train_tokenizer():
    """Train BPE tokenizer and measure performance."""

    # Configuration
    input_path = "data/TinyStoriesV2-GPT4-train.txt"
    vocab_size = 10000
    special_tokens = ["<|endoftext|>"]

    # Check if input file exists
    if not Path(input_path).exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Start timing
    start_time = time.time()

    # Train the tokenizer
    print("Starting BPE training...")
    vocab, merges = run_train_bpe(
        input_path=input_path, vocab_size=vocab_size, special_tokens=special_tokens
    )

    # End timing
    end_time = time.time()
    training_time = end_time - start_time

    print(f"Training completed!")
    print(
        f"Training time: {training_time:.2f} seconds ({training_time/60:.2f} minutes)"
    )

    vocab_path = "data/results/vocab.pkl"
    merges_path = "data/results/merges.pkl"

    with open(vocab_path, "wb") as f:
        pickle.dump(vocab, f)

    with open(merges_path, "wb") as f:
        pickle.dump(merges, f)

    print(f"Vocabulary saved to: {vocab_path}")
    print(f"Merges saved to: {merges_path}")


if __name__ == "__main__":
    try:
        train_tokenizer()

    except Exception as e:
        print(f"Error during training: {e}")
        raise
