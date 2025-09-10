# unigram-bigram-lm.
“Simple Unigram and Bigram Language Model with Laplace smoothing and perplexity calculation in Python.”

# unigram-bigram-lm.
“Simple Unigram and Bigram Language Model with Laplace smoothing and perplexity calculation in Python.”

# unigram-bigram-lm

**Simple Unigram and Bigram Language Model with Laplace smoothing and perplexity calculation in Python.**

---

## 📌 Features
- Tokenization with `<s>` (start) and `</s>` (end) markers  
- Unigram & Bigram frequency counts  
- Laplace (add-one) smoothing  
- Perplexity and average negative log-likelihood calculation  
- Compute sequence probability manually  
- Built from scratch using only Python standard libraries (`collections`, `math`)  

---

## 📝 Example Corpus
"the cat sat on the mat"
"the dog sat on the log"
"the cat saw the dog"
"the dog chased the cat"

yaml
Copy code

---

## 📊 Example Output
Vocabulary: 11
Unigram counts: {'<s>': 4, 'The': 1, 'cat': 3, 'sat': 2, ...}
Bigram counts: {('<s>', 'The'): 1, ('The', 'cat'): 1, ...}

Unigram model -> avg -log-likelihood: 2.3607, perplexity: 10.6007
Bigram model -> avg -log-likelihood: 2.0463, perplexity: 7.7400
Log-prob (bigram) of test sentence: -9.6312
Probability (bigram) of test sentence: 6.55e-05

yaml
Copy code

---

## 🚀 How to Run
```bash
# Clone the repo
git clone https://github.com/YourUsername/unigram-bigram-lm.git
cd unigram-bigram-lm

# Run the script
python unigram_bigram.py
🎯 Takeaways
Unigram and Bigram models are the foundation of modern NLP.

Perplexity helps measure how well a model predicts unseen text.

These ideas extend into transformers & LLMs (e.g., GPT).

📌 Next Steps
Extend to trigram models

Use a larger corpus (e.g., Wikipedia subset)

Compare results with modern pre-trained models

📬 Connect
If you find this helpful, feel free to ⭐ the repo and connect with me on LinkedIn.

📊 Results
Model	Avg -            Log Likelihood (nats/token)	   Perplexity
Unigram	                  2.3607	                      10.6007
Bigram	                  2.0463	                      7.7400
