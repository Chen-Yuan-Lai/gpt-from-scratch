"""Extension — add a KV cache to generate() and benchmark it.

Plan:
1. Head keeps cached K/V from previous steps; each step only computes Q/K/V
   for the newest token and appends K/V to the cache.
2. Handle position embedding for the new token's absolute position.
3. Compare wall-clock time for generating N tokens with / without cache.
4. Verify both paths produce identical tokens with greedy decoding.
"""
import time

# TODO: implement cached generate
# TODO: benchmark for N in (100, 500, 1000); write results/kv_cache.md


def kv_cache_bytes(n_layer: int, n_kv_head: int, head_dim: int, bytes_per_elem: int = 2) -> int:
    """Bytes of KV cache per token: 2 (K,V) x layers x kv_heads x head_dim x dtype bytes."""
    return 2 * n_layer * n_kv_head * head_dim * bytes_per_elem
