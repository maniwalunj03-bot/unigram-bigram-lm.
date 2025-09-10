# unigram-bigram-lm.
“Simple Unigram and Bigram Language Model with Laplace smoothing and perplexity calculation in Python.”

Unigram & Bigram Language Model (from Scratch)
A simple implementation of Unigram and Bigram Language Models in Python with:
Laplace (add-one) smoothing
Perplexity calculation
Sentence probability evaluation
This project was built from scratch without external NLP libraries (only Python standard libraries + collections, math).

📌 Features
Tokenization with <s> (start) and </s> (end) markers
Unigram & Bigram frequency counts
Laplace smoothing to handle unseen words
Perplexity and average negative log-likelihood calculation
Compute sequence probability manually

🚀 Example Corpus
"The cat sat on the mat"
"the dog sat on the log"
"the cat saw the dog"
"the dog chased the cat"

🧮 Example Output
Vocabulary: 11
Unigram counts: {'<s>': 4, 'The': 1, 'cat': 3, 'sat': 2, ...}
Bigram counts: {('<s>', 'The'): 1, ('The', 'cat'): 1, ...}
unigram model -> avg -log-likelihood (nats/token): 2.3607, perplexity: 10.6007
bigram model  -> avg -log-likelihood (nats/token): 2.0463, perplexity: 7.7400
Log-prob (bigram) of test sentence: -9.6312
Probability (bigram) of test sentence: 6.55e-05

⚡ How to Run
Clone the repo:
git clone https://github.com/YourUsername/unigram-bigram-lm.git
cd unigram-bigram-lm
Run the script:
python unigram_bigram.py

🎯 Takeaways
Unigram and Bigram models are the foundation of modern NLP.
Perplexity helps measure how well a model predicts unseen text.
Building these models from scratch provides intuition behind LLMs like GPT, which extend these principles with deep learning.

📚 Next Steps
Extend to trigram models
Use a larger corpus (e.g., Wikipedia subset)
Compare results with modern pre-trained models

🔗 Connect
If you find this helpful, feel free to ⭐ the repo and connect with me on LinkedIn.

📊 Results
Model	Avg       -Log Likelihood (nats/token)	    Perplexity
Unigram               	2.3607	                   10.6007
Bigram	                2.0463                    	7.7400
