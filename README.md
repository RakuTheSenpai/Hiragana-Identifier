![Hiragana](http://i.imgur.com/rFEs2jM.png "Hiragana")
# Hiragana-Identifier
Machine Learning project to identify Japanese characters (hiragana) from a data set. 

## Introduction
 Image recognition is crucial in the evolution of artificial intelligence. Specifically, finding an efficient model for reading handwritten characters is an ongoing research for very different alphabets, whose symbols vary drastically. In this poster the problem of reading Japanese characters (hiragana) will be solved using Convolutional Neural Networks (CNN). The data set used was taken from a Github repository, which contained 50 different characters and 20 different samples for each one. While sample size is small, a considerable level of certainty can be obtained utilizing a good learning model. 
 
 ## Objective
 The objective of this project is to demonstrate that despite utilizing a small sample as training data, its possible to create a learning model utilizing convolutional neural networks to classify 50 different Japanese hiragana characters. The following algorithm is proposed in order to solve the problem:
 
 ![Flowchart](https://github.com/RakuTheSenpai/Hiragana-Identifier/blob/master/img/flowchart.png "Flowchart")

 ## Methodology
Our convolutional neural network consists of: 

- A convolutional layer with 50 kernels of size 5x5 with activation function ReLU
- A maxpooling layer in order to reduce computational workload.
- A fully connected layer consisting of 128 nodes with activation function ReLU.
- A fully connected output layer with 50 nodes and activation function softmax.

![CNN](https://github.com/RakuTheSenpai/Hiragana-Identifier/blob/master/img/model.png "CNN")

## Results
An accuracy of around 88% was obtained by training the model through the CNN with five iterations (epochs) without further improvement. There were 200 samples in the test data.
![results](https://github.com/RakuTheSenpai/Hiragana-Identifier/blob/master/img/realResults.png "Results")

## Conclusions
From the results obtained by this model (85% accuracy) it has been partially proved that it is not necessary to have a data set of great magnitude to get exceptional classification results through convolutional neural networks. Furthermore, the advantage of having a very small sample is that applications based on this model will have a short running time. On the other side, there is still a lot of room for improvement, given that the model has not been tested on other data sets or by using re-sampling methods such as bootstrap or cross-validation.

Data set available at: [Hiragana73](https://lab.ndl.go.jp/cms/hiragana73?fbclid=IwAR2isHvlc2sxjzytRbHRXDaNQM__sevaA9azydGpcrUqlgXdK8LcMpXi13E) and 
[HiraganaGit](https://github.com/inoueMashuu/hiragana-dataset)

Project by [@RakuTheSenpai](https://github.com/RakuTheSenpai), [@TheChouzenOne](https://github.com/TheChouzanOne) and [@KillerFarmer](https://github.com/KillerFarmer)
