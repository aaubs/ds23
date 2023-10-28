---
title: "Exercise Session 3"
weight: 3
disableToc: true
draft: true
---

In this session, you will learn how to finetune SBERT embeddings and use them in downstream tasks. They will also practice using SBERT in a variety of business scenarios.


## Hate Speech Dataset

![](/ds22/images/corgi-protest.png)

> Online hate speech on social media networks can influence hate violence and even crimes against a certain group of people in this digital age. According to FBI statistics, hate-related attacks on specific groups of people are at a 16-year high [[1]](https://www.nytimes.com/2019/11/12/us/hate-crimes-fbi-report.html). Due to this, there is a growing need to eradicate hate speech through automatic detection to reduce the burden on moderators Datasets were obtained from Reddit and a white supremacist forum, Gab, where human-labeled comments are classified as hate speech [[2]](https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech). 


### Overview

The dataset used for this project consists of Tweets labeled as hate_speech, offensive_language, or neither. In the dataset:

* count = number of CrowdFlower users who coded each tweet (min is 3, sometimes more users coded a tweet when judgments were determined to be unreliable by CF).
* hate_speech = number of CF users who judged the tweet to be hate speech.
* offensive_language = number of CF users who judged the tweet to be offensive.
* neither = number of CF users who judged the tweet to be neither offensive nor non-offensive.
* class = class label for majority of CF users.
* 0 - hate speech 1 - offensive language 2 - neither



### Tasks

* First step: Performance comparison of Transformer models and traditional embedding models
* Second step: SBERT for semantic similarity (Patent Search using PatentSBERTa)


## Notebooks

Here you will find the notebooks for this session:


### Core contents
* [SetFit Hatespeech vs bert and distilroberta](https://colab.research.google.com/drive/16HQiC0prlNUABusajZN4Fp71op0e6YuR?usp=sharing)

* [SBERT for Patent Search using PatentSBERTa in PyTorch](https://colab.research.google.com/github/aaubs/ds-master/blob/main/notebooks/M4_PatentSBERTa_For_PatentSearch.ipynb)


### Classification with various vectorization approaches
* [TF-IDF and W2V Multi-Class Text Classification](https://colab.research.google.com/github/aaubs/ds-master/blob/main/notebooks/M4_TFIDF_W2V_multiclass_text_classification.ipynb)
* [BERT Multi-Class Text Classification](https://colab.research.google.com/github/aaubs/ds-master/blob/main/notebooks/M4_BERT_multiclass_text_classification.ipynb)
* [Implementing Multi-Class Text Classification LSTMs using PyTorch](https://colab.research.google.com/github/HamidBekamiri/ds-master/blob/main/notebooks/M4_LSTM_multiclass_text_classification_PyTorch_v1.ipynb)



### Add-on
* [Implementing LSTMs using PyTorch - Text Generation](https://github.com/aaubs/ds-master/blob/main/notebooks/M3_Character_Level_LSTM_PyTorch.ipynb)
* [Basic LSTMs using PyTorch](https://colab.research.google.com/github/aaubs/ds-master/blob/main/notebooks/M4_Basic_LSTM_PyTorch.ipynb)

