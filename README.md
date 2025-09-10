# Unigram-Bigram Language Model

A simple **Unigram and Bigram Language Model** implemented in Python with Laplace smoothing and perplexity calculation.  

## 📌 Features
- Tokenization with `<s>` and `</s>` markers  
- Unigram & Bigram frequency counts  
- Laplace (add-one) smoothing  
- Perplexity and average negative log-likelihood calculation  
- Sentence probability evaluation  
- Uses only Python standard libraries  

📖 Example Corpus
The cat sat on the mat
the dog sat on the log
the cat saw the dog
the dog chased the cat

📊 Example Output
Vocabulary: 11
Unigram counts: {'<s>': 4, 'The': 1, 'cat': 3, 'sat': 2, ...}
Bigram counts: {('<s>', 'The'): 1, ('The', 'cat'): 1, ...}

Unigram model -> avg -log-likelihood (nats/token): 2.3607, perplexity: 10.6007
Bigram model -> avg -log-likelihood (nats/token): 2.0463, perplexity: 7.7400

Log-prob (bigram) of test sentence: -9.6312
Probability (bigram) of test sentence: 6.55e-05

🚀 How to Run
git clone https://github.com/YourUsername/unigram-bigram-lm.git
cd unigram-bigram-lm

# Run the script
python unigram_bigram.py

📝 Takeaways

Unigram and Bigram models are the foundation of modern NLP

Perplexity measures how well a model predicts unseen text

These ideas extend to deep learning models like GPT

📈 Next Steps

Extend to Trigram models

Train on a larger corpus

Compare with pre-trained transformer models
