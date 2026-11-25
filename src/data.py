"""Step 1 — char-level tokenizer, train/val split, batching."""
import torch

# TODO: read data/input.txt
# TODO: build vocab (sorted set of chars), stoi / itos
# TODO: encode(s) -> list[int], decode(ids) -> str
# TODO: train/val split (90/10)


def get_batch(split: str, block_size: int, batch_size: int, device: str):
    """Return (x, y) of shape (batch_size, block_size)."""
    # TODO
    raise NotImplementedError
