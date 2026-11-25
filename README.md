# GPT from Scratch

跟著 Andrej Karpathy〈[Let's build GPT: from scratch, in code, spelled out](https://youtu.be/kCc8FmEb1nY)〉從零實作 decoder-only Transformer，並延伸實作 KV cache，作為學習 LLM 推論 / vLLM 的起點。

## 結構

```
src/
  data.py            # tokenizer、split、get_batch
  bigram.py          # bigram baseline
  gpt.py             # GPT 模型與訓練
  kv_cache_bench.py  # 延伸：KV cache + benchmark
scripts/download_data.py
notes/learnings.md   # 學習筆記
results/             # loss 紀錄、生成範例、benchmark
```

## 執行

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate   Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/download_data.py
python src/bigram.py
python src/gpt.py
python src/kv_cache_bench.py
```

## 進度

- [ ] 1. Tokenizer、train/val split
- [ ] 2. Bigram baseline
- [ ] 3. Self-attention 數學技巧
- [ ] 4. Single-head attention
- [ ] 5. Multi-head + FeedForward
- [ ] 6. Residual + LayerNorm + Dropout
- [ ] 7. 放大模型（GPU）
- [ ] 延伸：KV cache

## 結果

| 模型 | 參數量 | val loss | 硬體 / 訓練時間 |
| --- | --- | --- | --- |
| Bigram |  |  |  |
| GPT（小） |  |  |  |
| GPT（放大） |  |  |  |

### 生成範例

```
（貼上 results/samples/ 中的一段）
```

### KV cache benchmark

| 生成 tokens | 無 cache (s) | 有 cache (s) | 加速 |
| --- | --- | --- | --- |
| 100 |  |  |  |
| 500 |  |  |  |
| 1000 |  |  |  |

## 學到的事

1.
2.
3.

## 參考

- [karpathy/ng-video-lecture](https://github.com/karpathy/ng-video-lecture)
- [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)
