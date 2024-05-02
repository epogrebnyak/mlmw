# Beginner track for machine learning

> Where do I start?

My suggestion for making a start in machine learning is getting two free textbooks and enrolling into a video course:

- [Mathematics for Machine Learning (MML)][mml] by Marc Peter Deisenroth, A. Aldo Faisal and Cheng Soon Ong;
- [Introduction to Statistical Learning with Python (ISLP)](https://www.statlearning.com/) by Gareth James, Daniela Witten, Trevor Hastie and Rob Tibshirani;
- [Deep Learning Specialization][dls] by Andrew Ng.

Links to other textbooks and supplementary materials are provided below.

## Prerequisites

You will need a working knowledge of Python and ability to operate with mathematical concepts from linear algebra and calculus.

## Core path

1. Check you math knowledge with [Mathematics for Machine Learning (MML)][mml] Part 1.
2. Read chapter 8 "When Models Meet Data" in [MML][mml] for introduction to machine learning.
3. Proceed to [Introduction to Statistical Learning with Python (ISLP)](https://www.statlearning.com/) textbook.
4. Read from `scikit-learn` documentation about [neural network models][nn].
5. Start Andrew Ng [Deep Learning Specialization][dls].

[dls]: https://www.deeplearning.ai/courses/deep-learning-specialization/
[mml]: https://mml-book.github.io/
[nn]: https://scikit-learn.org/stable/modules/neural_networks_supervised.html#neural-network-models-supervised

## Reference texts

There are more dense textbooks than ISLP or Andrew Ng course that you can use as references.

For machine learning they are
[Bishop (2006)](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)
and [Murphy (2022)](https://probml.github.io/pml-book/book1.html).

For deep learning there are three major open textbooks:

- [Ian Goodfellow, Yoshua Bengio and Aaron Courville (2016). Deep Learning Book (DLB)](https://www.deeplearningbook.org/)
- [Aston Zhang, Zack Lipton, Mu Li and Alex Smola (2021). Dive into Deep Learning (d2l).](https://d2l.ai/)
- [Simon Prince (2023). Understanding Deep Learning (UDL).](https://udlbook.github.io/udlbook/)

Note that `d2l` and `UDL` were updated in 2023-2024.

## What else?

You can supplement the core path above with the following:

- introductory courses on probability
  (like [P4D](https://probability4datascience.com/)
  or [Seeing theory](https://seeing-theory.brown.edu/basic-probability/index.html))
  and [statistics](https://jverzani.github.io/UsingJ/index.html);

- [scipy lectures](https://lectures.scientific-python.org/) is an
  underappreciated resource by the authors on foundational `scikit-learn`
  package themselves;

- [Python Data Science Handbook by Jake VanderPlas](https://jakevdp.github.io/PythonDataScienceHandbook/),
  including [machine learning chapter](https://jakevdp.github.io/PythonDataScienceHandbook/#5.-Machine-Learning)
  and [DSML](https://people.smp.uq.edu.au/DirkKroese/DSML/) textbook;

- practical books that further combine machine learning concepts and programming practice
  -- either of [Muller](https://amueller.github.io/#book),
  [Geron](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/)
  or [Burkov](https://themlbook.com/) (all are paid editions);

- review subfields of machine learning like natural language processing (NLP),
  computer vision (CV), reinforcement learning (RL) or robotics;

- for popular attention and transformer architectures check out talks by
  [Andrej Karpathy](https://karpathy.ai/)
  and his [NanoGPT](https://github.com/karpathy/nanoGPT) sample code;

- familiarize with approaches to data modelling in econometrics (eg. chapter 1, 2, 4, 5 from [Econ 1630](https://github.com/jonathandroth/Econ1630_Github))

- glance vocabulary in data analysis as endorsed by the industry leaders like
  [Google](https://developers.google.com/machine-learning/glossary),
  [Mathworks](https://www.mathworks.com/discovery.html),
  [H2O](https://h2o.ai/wiki/) and
  [NVIDIA](https://www.nvidia.com/en-us/glossary/);

- last but not least [StatQuest videos by Josh Starmer](https://www.youtube.com/channel/UCtYLUTtgS3k1Fg4y5tAhLbw)
  and [3Blue1Brown videos by Grant Sanderson](https://www.3blue1brown.com/) make great study companions.

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

- [scikit-learn](https://scikit-learn.org/stable/index.html), see also [Gaël Varoquaux 2023 interview](https://youtu.be/MaJRf9E-jtQ?t=223).

Deep learning:

- [PyTorch](https://pytorch.org/) (most popular)
- [TensorFlow](https://www.tensorflow.org/) and [Keras](https://www.tensorflow.org/guide/keras) (easier to learn)

## Does reading these materials make you a machine learning engineer?

Not until you make projects for real tasks on real data (where textbook examples do not play out that well).

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
