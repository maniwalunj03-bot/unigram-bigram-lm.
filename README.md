# Unigram and Bigram Language Model with Laplace Smoothing

**Author:** Manisha Walunj
**Date:** September 2025  

---

## 📖 Project Overview

This project implements a **simple Unigram and Bigram Language Model (LM)** in Python with **Laplace (add-one) smoothing**. It calculates **log-probabilities**, **cross-entropy**, and **perplexity** for given text corpora.  

The model helps demonstrate how statistical language models predict word sequences and quantify the uncertainty of text generation.

## 🔑 Features

- Tokenization with `<s>` (start) and `</s>` (end) markers.
- Calculation of **Unigram** and **Bigram frequency counts**.
- Laplace (add-one) smoothing to handle unseen words.
- Compute **log-probabilities** for sequences.
- Compute **cross-entropy** and **perplexity** for evaluation.
- Easily extendable for larger corpora or more complex n-grams.

## 🛠️ Technologies & Libraries

- Python 3.x
- Standard libraries: `collections`, `math`

## ⚙️ Usage

1. Clone or download the repository.  
2. Run the script `unigram_bigram_lm.py` in Python:  

Example output:

Vocabulary and counts for unigrams and bigrams

Average negative log-likelihood and perplexity for the corpus

Probability and log-probability of a test sentence

🧪 Example
Input sentence:

the cat sat on the mat

Output (Bigram Model):

Log-probability: -10.1234

Probability: 4.5e-05

🔍 How It Works
Tokenization: Each sentence is tokenized with <s> and </s> markers.

Count Frequencies: Unigram and bigram counts are computed.

Laplace Smoothing: Adds 1 to every count to handle unseen events.

Sequence Probability: Log-probability for each sentence is calculated.

Perplexity: Evaluates the model's performance on a corpus:

Perplexity = e−N1​∑i=1N​logp(wi​∣wi−1​)
 
📁 Project Structure
.
├── unigram_bigram_lm.py       # Main script
└── README.md                  # Project documentation

📬 Contact
LinkedIn: https://www.linkedin.com/in/manisha-walunj

GitHub: https://github.com/manishawalunj

✅ Notes
This project is perfect as a portfolio example for:
Machine Learning fundamentals
NLP basics
Probability-based language modeling

