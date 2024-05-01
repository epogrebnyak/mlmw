# Beginner track

Below is a suggested path to study machine learning (ML) and deep learning (DL).
The path involves two open textbooks and an open video course:

- [Mathematics for Machine Learning (MML) by Marc Peter Deisenroth, A. Aldo Faisal and Cheng Soon Ong][mml];
- [Introduction to Statistical Learning with Python (ISLP) by Gareth James, Daniela Witten, Trevor Hastie and Rob Tibshirani](https://www.statlearning.com/);
- Andrew Ng [Deep Learning Specialization][dls].

Links to reference textbooks and supplementary materials are also provided below.
All resources listed at this page are free to access and download
unless specifically marked as paid edition.

## Prerequisites

You will need a working knowledge of Python and ability
to operate with mathematical concepts from linear algebra and calculus.

## Core path

1. Check you math knowledge with [Mathematics for Machine Learning (MML)][mml] Part 1.
2. Read chapter 8 "When Models Meet Data" in [MML][mml] for introduction to machine learning.
3. Proceed to
   [Introduction to Statistical Learning with Python (ISLP)](https://www.statlearning.com/)
   textbook.
4. Read from `scikit-learn` documentation about [neural network models](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#neural-network-models-supervised).
5. Start Andrew Ng [Deep Learning Specialization][dls].

[dls]: https://www.deeplearning.ai/courses/deep-learning-specialization/
[mml]: https://mml-book.github.io/

## Reference texts

There are more dense textbooks than ISLP or Andrew Ng course that you can use as references.

For machine learning they are
[Bishop (2006)](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)
and [Murphy (2022)](https://probml.github.io/pml-book/book1.html).

For deep learning there are three major open textbooks,
`d2l` and `UDL` were updated in 2023-2024:

- [Ian Goodfellow, Yoshua Bengio and Aaron Courville (2016). Deep Learning Book (DLB)](https://www.deeplearningbook.org/)
- [Aston Zhang, Zack Lipton, Mu Li and Alex Smola (2021). Dive into Deep Learning (d2l).](https://d2l.ai/)
- [Simon Prince (2023). Understanding Deep Learning (UDL).](https://udlbook.github.io/udlbook/)

## What else?

You can supplement the core path above with the following:

- modern introductory courses on [probability](https://probability4datascience.com/)
  and [statistics](https://jverzani.github.io/UsingJ/index.html);

- [scipy lectures](https://lectures.scientific-python.org/) is an
  underappreciated resource by the authors on foundational `scikit-learn`
  package themselves;

- [Python Data Science Handbook by Jake VanderPlas](https://jakevdp.github.io/PythonDataScienceHandbook/), including [machine learning chapter](https://jakevdp.github.io/PythonDataScienceHandbook/#5.-Machine-Learning) and [DSML](https://people.smp.uq.edu.au/DirkKroese/DSML/) textbook;

- practical books that further combine machine learning concepts and programming practice
  -- either of [Muller](https://amueller.github.io/#book),
  [Geron](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/)
  or [Burkov](https://themlbook.com/) (all are paid editions);

- review subfields of machine learning like natural language processing (NLP),
  computer vision (CV), reinforcement learning (RL) or robotics;

- for popular attention and transformer architectures check out talks by
  [Andrej Karpathy](https://karpathy.ai/)
  and his [NanoGPT](https://github.com/karpathy/nanoGPT) sample code;

- check out approaches to data modelling in econometrics (eg. chapter 1, 2, 4, 5 from [Econ 1630](https://github.com/jonathandroth/Econ1630_Github))

- to glance what vocabulary in data analysis the industry leaders endorse see links to
  [Mathworks](https://www.mathworks.com/discovery.html),
  [H2O](https://h2o.ai/wiki/) and
  [NVIDIA](https://www.nvidia.com/en-us/glossary/).

## Roadmap

```
Math   ML      DL                Subfields
----   -----   ---------------   -----------------------------

MML -> ISLP -> deeplearning.ai -> NLP and Transformers
        |                      -> CV
        |                      -> Agents, robotics and RL
       Practical:              -> Tabular data and time series
       - scipy lectures (free)
       - Muller, Geron or Burkov (paid)
```

## Python packages

Machine learning:

- [scikit-learn](https://scikit-learn.org/stable/index.html)

<!-- - xgboost -->

Deep learning:

- [PyTorch](https://pytorch.org/) (most popular)
- [TensorFlow](https://www.tensorflow.org/) and [Keras](https://www.tensorflow.org/guide/keras) (easier to learn)

## Does reading these materials make you a machine learning engineer?

Not until you make projects for real tasks on real data
(where textbook examples do not play out that well).

## Not in scope

This page puts no recommendation for various skills
that are also important for a quantitative modeller or an engineer:

- Python programming, Linux and cloud computing;
- data processing, pipelines and model productisation;
- experiment design and iterative workflows;
- advanced topics in statistics and machine learning;
- domain knowledge, business sense and outcomes of ML adoption.

Please refer to larger [MLMW guide](mlmw.md) for coverage of these topics.

<!--

## Engineering and data path

```
Linux -> Python -> Data processing -> Cloud -> Orchestration
                   - SQL/NoSQL        - AWS    - Apache Airflow
                   - Hadoop/Spark     - GCS
                                      - Azure

```
-->
