# Bigrams and Disappointment: 
## A Very Short AI Adventure

date: 2025-04-30 

## 1. Setup: Curiosity Begins

I got really excited about all this AI stuff. Everyone kept saying, "It's just predicting the next word." Cool. But *why* does that work?

So I started from the beginning: **Statistical Language Models**, specifically **bigrams**. Predict the next word based on the last. Like T9, but with hope.

By the way, according to Dr. Lisa Feldman Barrett, the human brain works a bit like T9 too. What a funny coincidence!

---

## 2. The Plan

Let’s keep it simple:

* Use **NewsAPI** to get recent semiconductor headlines
* Tokenise them using **NLTK**
* Count the most frequent bigrams

Result? Total nonsense.

```
['chip shortage', 'market growth', 'Q3 earnings', 'quarter quarter']
```

Some of these make sense. Most don’t. “Quarter quarter”? Really?

!\[Bigrams wordcloud goes here]

---

## 3. I Refuse to Give Up

Next up: **sentiment analysis** with `TextBlob`.

It gives you:

* **Polarity**: is it positive or negative?
* **Subjectivity**: is it fact or opinion?

Cool. Except… again, not much to show. Turns out news headlines are pretty neutral most of the time. Even the spicy ones.

```json
{"headline": "NVIDIA soars on new chip", "polarity": 0.3, "subjectivity": 0.5}
```

Doesn’t tell you much.

---

## 4. A Final Push: Stock Data

Alright, let’s *really* try:

* Pull daily stock prices from `yfinance`
* Match those to daily average sentiment
* Look for correlation

Polarity vs. price change? Nothing. Volume vs. subjectivity? Nope.

!\[Empty correlation matrix]

---

## 5. What I Learned

So yeah—it didn’t work. At all.

But here’s what I took away:

* **Bigram models** are too shallow for modern news
* **TextBlob sentiment** struggles with finance headlines
* **News-to-market correlation** is messy, subtle, or nonexistent

That doesn’t mean the effort was wasted. It means I now understand *why* bigrams got left behind.

Like dial-up. Important, but not something you’d want to use today.

---

## 6. What’s Next

Stage II: **Neural Language Models (2000s)** Before ChatGPT, there were RNNs and early LSTM models.

Can I do anything interesting with them? Let’s find out.

*(Spoiler: I have no idea what I’m doing, and I like it that way.)*

---

## Repo: [GitHub - Bigram Financial News Experiment](https://github.com/med4kat/financial-event-detection-bigrams)

Includes:

* Scripts for collecting and analysing news headlines
* Sentiment results
* Stock data correlation attempts
* Everything that didn’t work (plus notes about why)

---
