![](https://github.com/felixoder/bug_detection_ml_project/blob/master/logo.png?raw=true)

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](https://github.com/felixoder/bug_detection_ml_project/blob/master/LICENSE)
[![Documentation](https://img.shields.io/badge/Documentation-github-brightgreen.svg?style=for-the-badge)](xyz.html)


This project is a powerful fine tune model crafted in google colab to detect and fix all kinds of bugs of a python code in realtime. This is integrated in a VS code extenstion through [felix-detect-fix](https://github.com/felixoder/felix-detect-fix). It's fast with it's GPU/CPU based workflow and compatible with all the Operating System. thanks to the new [codebert-base](microsoft/codebert-base) model and [deepseek](deepseek-ai/deepseek-coder-1.3b-instruct).

![](https://github.com/felixoder/bug_detection_ml_project/blob/master/demo_running.png?raw=true)

# Getting Started

## Installation

If you want to use this model locally then you should have installed python 3+ on your machine. And for model usage if you have a good GPU it will be cherry on the top. But if you don't have any GPU please make sure to use google colab or kaggle notebook or other services. Alternatively You can use any popular cloud services such that AWS, GCP, Azure etc.

<details><summary>Instructions</summary>

The both bug detecting and fixing model is available on the [Huggingface-bug-detection](https://huggingface.co/felixoder/bug_detector_model) and [Huggingface-bug-fixing](https://huggingface.co/felixoder/bug_fixer_model) if you want to install them you are good to go.


1. Open the `usingModel.ipynb` and test this model.
2. Check the accuracy score, F1, Precesion and other metrics for better understanding.
3. Next, Check for the graphical section to understand confusion matrix, box-plot, histogram etc.


</details>

## Usage

If you want to explore the extension please refer to this repository
https://github.com/felixoder/felix-detect-fix

<details><summary>Instructions How to use this</summary>

Open the extension tab in your VS code and find this [felix-detect-fix](https://marketplace.visualstudio.com/items?itemName=DebayanGhosh.felix-detect-fix) and install this.


1. Now create a python file having extension of `.ipynb`.
2. Write some code and press `Ctrl/cmd + shift + p` and type `Detect Bug`. after running this wait for couple of second and if there is a bug you can see a pop up and if you want to click `Fix Bug`.
3. Next, Click the `Fix Bug` [you can do this either by running the `Ctrl/cmd + shift + p` and type `Detect Bug` or the steps in step 2 and do fix likewise]

![](https://github.com/felixoder/bug_detection_ml_project/blob/master/images/e1.png?raw=true)
![](https://github.com/felixoder/bug_detection_ml_project/blob/master/images/e2.png?raw=true)
![](https://github.com/felixoder/bug_detection_ml_project/blob/master/images/e3.png?raw=true)
![](https://github.com/felixoder/bug_detection_ml_project/blob/master/images/e4.png?raw=true)
![](https://github.com/felixoder/bug_detection_ml_project/blob/master/images/e5.png?raw=true)


</details>

## Documentation

Here are some useful documentation links:
- Getting started guide:  index.html
- VS code extension library: https://marketplace.visualstudio.com/items?itemName=DebayanGhosh.felix-detect-fix
- Mixture graph examples: https://alelievr.github.io/Mixture/manual/Examples.html
- Known issues: https://alelievr.github.io/Mixture/manual/KnownIssues.html

## Evaluation

we have evaluated the evaluation matrics of the fine tune model please check the following graphs 

and from the evaluation matrics our scores are follows - 

Accuracy: 80.00%
Precision: 1.00
Recall: 0.60
F1 Score: 0.75

![](https://github.com/felixoder/bug_detection_ml_project/blob/master/images/t1.png?raw=true)
![](https://github.com/felixoder/bug_detection_ml_project/blob/master/images/t2.png?raw=true)
![](https://github.com/felixoder/bug_detection_ml_project/blob/master/images/t3.png?raw=true)
![](https://github.com/felixoder/bug_detection_ml_project/blob/master/images/t4.png?raw=true)
![](https://github.com/felixoder/bug_detection_ml_project/blob/master/images/t5.png?raw=true)

# Community 

## Discord

Join the [Mixture Discord](https://discord.gg/DGxZRP3qeg)! 

## Feedback

To give feedback, ask a question or make a feature request, you can either use the [Github Discussions](https://github.com/felixoder/bug_detection_ml_project/discussions).

Bugs are logged using the github issue system. To report a bug, simply [open a new issue](https://github.com/felixoder/bug_detection_ml_project/issues/new/choose).

## Contributions 

All contributions are welcomed.

For new nodes, check out [this documentation page on how to create a new shader-based node](index.html). Once you have it working, prepare a pull request against this repository.  
In case you have any questions about a feature you want to develop of something you're not sure how to do, you can still create a draft pull request to discuss the implementation details.

# Gallery / Cool things

You can install the extension and detect the bug like
![](https://github.com/felixoder/bug_detection_ml_project/blob/master/image/d1.gif?raw=true)

And fix the bug like
![](https://github.com/felixoder/bug_detection_ml_project/blob/master/image/d2.gif?raw=true) 

Use the model in google colab like this 
![](https://github.com/felixoder/bug_detection_ml_project/blob/master/image/d3.gif?raw=true) 





![full video how to use the model in vs code](https://github.com/felixoder/bug_detection_ml_project/blob/master/image/full.mp4?raw=true) 

@source - The idea and the project is done from my industrial training of Intel Unnati where I am selected among 50 students in my college.

## Developer 
Debayan Ghosh @felixoder
uni student code - BWU/BTA/22/157
