# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 14:20:51 2025

@author: Manisha
"""

# Simple unigram and bigram LM with Laplace smoothing and perplexity 
# calculation.
from collections import Counter, defaultdict
import math

# 1) Example corpus (small to keep numbers clear)
corpus = [
    "The cat sat on the mat",
    "the dog sat on the log",
    "the cat saw the dog",
    "the dog chased the cat"
    ]

# Tokanise and start token (<s>) and end token (</s>) for sequence boudries.
def tokenize(sentence):
    tokens = sentence.strip().split()
    return ["<s>"] + tokens + ["</s>"]

tokenized = [tokenize(s) for s in corpus]
# tokanised is a list of tokans

# Build unigram and bigram counts
unigram_counts = Counter()
bigram_counts = Counter()
vocab = set()

for sent in tokenized:
    for i, tok in enumerate(sent):
        unigram_counts[tok] += 1
        vocab.add(tok)
        if i > 0:
            prev = sent[i-1]
            bigram_counts[(prev, tok)] += 1

V = len(vocab)            # Vocabulary length

# Convert counts to smoothed probabilities (laplace / add one smooth)
def unigram_prob(token, alpha=1.0):
    # p(token) = count(token) + alpha / total counts + alpha * V
    total = sum(unigram_counts.values())
    return (unigram_counts[token] + alpha) / (total + alpha * V)

def bigram_prob(prev, token, alpha=1.0):
    # p(prev, token) = (count(prev, token)+alpha) / (count(prev) +alpha * V)
    prev_count = unigram_counts[prev]
    num = bigram_counts[(prev, token)] + alpha
    den = prev_count + alpha * V
    return num / den

# Function to compute sequence log probability under a nodel.
def sequence_logprob(tokens, model="bigram", alpha=1.0):
    # tokens is a list like ["<s>", "the", "cat", "</s>"]
    
    logp = 0.0
    for i in range(1, len(tokens)):
        prev, tok = tokens[i - 1], tokens[i]
        if model == "unigram":
            p = unigram_prob(tok, alpha)
        else: # model == "bigram"
            p = bigram_prob(prev, tok, alpha)
        logp += math.log(p)
    return logp

# Cross-entropy and perplexity of the corpus
def corpus_perplexity(tokanized_corpus, model="bigram", alpha=1.0):
    total_logprob = 0.0
    total_tokens = 0
    for sent in tokanized_corpus:
        total_tokens += (len(sent) - 1)  
        # number of predicted tokens (exclude first <s>)
        total_logprob += sequence_logprob(sent, model=model, alpha=alpha)
    # Average negetive log-likelihood (nats per tokens)
    avg_neg_log_likelihood = - total_logprob / total_tokens
    perplexity = math.exp(avg_neg_log_likelihood)
    
    return avg_neg_log_likelihood, perplexity

print("Vocabulary: {}".format(V))
print()
print("Unigram_counts: {}".format(dict(unigram_counts)))
print()
print("Bigram counts: ",{k:v for k,v in bigram_counts.items() if v>0})
print()    
# Compute perplexity

for m in ["unigram", "bigram"]:
    nll, ppl = corpus_perplexity(tokenized, model=m, alpha=1.0)
    print("{} model -> avg -log-likelihood (nats/token): {:.4f}, perplexity: {:.4f}"
          .format(m, nll, ppl))

# 8) Example: compute probability of a particular sentence
test_sent = tokenize("the cat sat on the mat")
print()
print("Log-prob (bigram) of test sentence: {}"
      .format(sequence_logprob(test_sent, model="bigram")))
print()
print("Probability (bigram) of test sentence: {}"
      .format(math.exp(sequence_logprob(test_sent, model="bigram"))))






















            