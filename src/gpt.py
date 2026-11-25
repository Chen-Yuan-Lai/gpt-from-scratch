"""Steps 4–7 — GPT (decoder-only Transformer)."""
import torch
import torch.nn as nn
from torch.nn import functional as F

# hyperparameters (start small on CPU, scale up on GPU in step 7)
batch_size = 32
block_size = 8
max_iters = 5000
eval_interval = 500
learning_rate = 1e-3
n_embd = 32
n_head = 4
n_layer = 3
dropout = 0.0
device = "cuda" if torch.cuda.is_available() else "cpu"


class Head(nn.Module):
    """Step 4 — one head of causal self-attention."""
    def __init__(self, head_size: int):
        super().__init__()
        # TODO: key, query, value projections; register_buffer('tril', ...)

    def forward(self, x):
        # TODO: scaled dot-product attention with causal mask
        raise NotImplementedError


class MultiHeadAttention(nn.Module):
    """Step 5"""
    # TODO


class FeedForward(nn.Module):
    """Step 5"""
    # TODO


class Block(nn.Module):
    """Step 6 — attention + ffwd with residual, LayerNorm (pre-norm), dropout."""
    # TODO


class GPTLanguageModel(nn.Module):
    """Step 7"""
    # TODO: token + position embedding, blocks, final LayerNorm, lm_head

    @torch.no_grad()
    def generate(self, idx, max_new_tokens: int):
        # NOTE: recomputes the whole context every step (no KV cache).
        # Keep this version — kv_cache_bench.py compares against it.
        raise NotImplementedError


if __name__ == "__main__":
    # TODO: training loop; save loss log + a sample to results/
    pass
