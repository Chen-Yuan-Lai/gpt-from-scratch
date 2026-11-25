"""Step 2 — Bigram baseline."""
import torch
import torch.nn as nn
from torch.nn import functional as F


class BigramLanguageModel(nn.Module):
    def __init__(self, vocab_size: int):
        super().__init__()
        # TODO: token embedding table (vocab_size x vocab_size)

    def forward(self, idx, targets=None):
        # TODO: logits, loss (cross entropy)
        raise NotImplementedError

    @torch.no_grad()
    def generate(self, idx, max_new_tokens: int):
        # TODO: sample one token at a time
        raise NotImplementedError


if __name__ == "__main__":
    # TODO: training loop, estimate_loss(), print a generated sample
    pass
