# Beginner track for machine learning

> Where do I start?

My suggestion for beginners is getting two free textbooks for classic machine learning (ML) and enrolling into a video course for deep learning (DL):

- [Mathematics for Machine Learning (MML)][mml] by Marc Peter Deisenroth, A. Aldo Faisal and Cheng Soon Ong;
- [Introduction to Statistical Learning with Python (ISLP)](https://www.statlearning.com/) by Gareth James, Daniela Witten, Trevor Hastie and Rob Tibshirani;
- [Deep Learning Specialization][dls] by Andrew Ng.

Links to other textbooks and supplementary materials are provided below.

## Roadmap

```
Math   ML      DL                Subfields
----   -----   ---------------   -----------------------------

MML -> ISLP -> deeplearning.ai -> NLP and Transformers
        |                      -> CV
        |                      -> Agents, robotics and RL
        |                      -> Tabular data and time series
       Practical manuals:
       - scipy lectures (free)
       - Muller (paid), Geron (paid) or Burkov (paid, free preview)
```

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

For classic machine learning they are [Bishop (2006)](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)
and [Murphy (2022)](https://probml.github.io/pml-book/book1.html).

For deep learning there are several open textbooks:

- [Ian Goodfellow, Yoshua Bengio and Aaron Courville (2016). Deep Learning Book (DLB)](https://www.deeplearningbook.org/)
- [Aston Zhang, Zack Lipton, Mu Li and Alex Smola (2021). Dive into Deep Learning (d2l).](https://d2l.ai/)[^1]
- [Simon Prince (2023). Understanding Deep Learning (UDL).](https://udlbook.github.io/udlbook/)

DLB (2016) is a reference text that enjoys [a continious stream of citations](https://scholar.google.ca/citations?view_op=view_citation&hl=en&user=iYN86KEAAAAJ&citation_for_view=iYN86KEAAAAJ:ZeXyd9-uunAC), while d2l and UDL are newer and keep updating code and content.

[^1]: This open-source book represents our attempt to make deep learning approachable, teaching readers the concepts, the context, and the code. The entire book is drafted in Jupyter notebooks, seamlessly integrating exposition figures, math, and interactive examples with self-contained code. Our goal is to offer a resource that could (i) be freely available for everyone; (ii) offer sufficient technical depth to provide a starting point on the path to actually becoming an applied machine learning scientist; (iii) include runnable code, showing readers how to solve problems in practice; (iv) allow for rapid updates, both by us and also by the community at large; (v) be complemented by a forum for interactive discussion of technical details and to answer questions. \[[arxiv abstract](https://arxiv.org/abs/2106.11342)\]

## What else?

You can supplement the core path above with the following:

- introductory courses on probability
  (like [P4D](https://probability4datascience.com/)
  or [Seeing Theory](https://seeing-theory.brown.edu/basic-probability/index.html))
  and [statistics](https://jverzani.github.io/UsingJ/index.html);

- [scipy lectures](https://lectures.scientific-python.org/) is an
  underappreciated resource by the authors on foundational `scikit-learn`
  package themselves;

- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/),
  including [a chapter on machine learning](https://jakevdp.github.io/PythonDataScienceHandbook/#5.-Machine-Learning)
  and [DSML](https://people.smp.uq.edu.au/DirkKroese/DSML/) textbook;

- practical books that combine machine learning concepts and programming practice
  -- either of
  [Müller](https://amueller.github.io/#book) (paid edition),
  [Géron](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/) (paid edition) or
  [Burkov](https://themlbook.com/) (paid edition with free preview);

- review subfields of machine learning like natural language processing (NLP),
  computer vision (CV), reinforcement learning (RL) or robotics;

- for popular attention and transformer architectures check out talks by
  [Andrej Karpathy](https://karpathy.ai/)
  and his [NanoGPT](https://github.com/karpathy/nanoGPT) sample code;

- familiarize with approaches to data modelling in econometrics (eg. chapter 1, 2, 4, 5 from [Econ 1630](https://github.com/jonathandroth/Econ1630_Github))

- glance at data analysis vocabulary as endorsed by the industry leaders like
  [Google](https://developers.google.com/machine-learning/glossary),
  [Mathworks](https://www.mathworks.com/discovery.html),
  [H2O](https://h2o.ai/wiki/) and
  [NVIDIA](https://www.nvidia.com/en-us/glossary/);

- last but not least [StatQuest videos by Josh Starmer](https://www.youtube.com/channel/UCtYLUTtgS3k1Fg4y5tAhLbw)
  and [3Blue1Brown videos by Grant Sanderson](https://www.3blue1brown.com/) make great study companions.

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
