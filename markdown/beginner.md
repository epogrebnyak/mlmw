# Beginner track

When asked about how can one study machine learning (ML) and deep learning (DL),
here is a suggested path that involves two free open textbooks and
an open video course.

## Prerequisites

You will need a working knowledge of Python and ability
to operate with mathematical concepts from linear algebra and calculus.

## Core path

1. Check you math knowledge with
   [Mathematics for Machine Learning (MML)](https://mml-book.github.io/) Part 1.
2. Read chapter 8 "When Models Meet Data" in MML for introduction to machine learning.
3. Proceed to
   [Introduction to Statistical Learning with Python (ISLP)](https://www.statlearning.com/)
   textbook.
4. For neural nets start Andrew Ng [Deep Learning Specialization][dls].

[dls]: https://www.deeplearning.ai/courses/deep-learning-specialization/

## Reference texts

There are more dense textbooks than ISLP or Andrew Ng course that you can use as references.

For machine learning they are
[Bishop](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf)
and [Murphy](https://probml.github.io/pml-book/book1.html),
and also [DSML](https://people.smp.uq.edu.au/DirkKroese/DSML/) as a summary.

For deep learning there are three major open textbooks:

- [Ian Goodfellow, Yoshua Bengio and Aaron Courville (2016). Deep Learning Book (DLB)](https://www.deeplearningbook.org/)
- [Aston Zhang, Zack Lipton, Mu Li and Alex Smola (2021). Dive into Deep Learning (d2l).](https://d2l.ai/)
- [Simon Prince (2023). Understanding Deep Learning (UDL).](https://udlbook.github.io/udlbook/)

`d2l` and `UDL` are actively maintained with new content being added.

## What else?

You can supplement the core path above with the following:

- modern introductory courses on [probability](https://probability4datascience.com/)
  and [statistics](https://jverzani.github.io/UsingJ/index.html);

- [scipy lectures](https://lectures.scientific-python.org/) is an
  underappreciated resource by authors on foundational `scikit-learn`
  package themselves;

- practical books that involve both machine learning theory and programming
  -- either of the [Muller](https://amueller.github.io/#book),
  [Geron](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/)
  or [Birukov](https://themlbook.com/) (all paid editions);

- pick a subfield of machine learning like natural language processing (NLP),
  computer vision (CV), reinforcement learning (RL) or robotics;

- for popular attention and transformers architectures check out talks by
  [Andrej Karpathy](https://karpathy.ai/)
  and his [NanoGPT](https://github.com/karpathy/nanoGPT) sample code;

- check out data modelling angle in econometrics (eg. chapter 1, 2, 4 from [Econ 1630](https://github.com/jonathandroth/Econ1630_Github)).

## Roadmap

```
Math   ML      DL                Subfields
----   -----   ---------------   ----------------------

MML -> ISLP -> deeplearning.ai -> NLP and Transformers (hot)
        |                      -> CV
        |                      -> Agents, robotics and RL
       Practical:              -> Tabular data and time series
       - scipy lectures (free)
       - Muller, Geron or Birukov (paid)


Python packages:

       ML             DL
       ------------   ----------
       scikit-learn   PyTorch
                      TensorFlow
                      Keras
```

## Does reading this make you a machine learning engineer?

Not until you make projects for real tasks on real data
(where textbook examples do not play out that well).

## Not in scope

This page puts no recommendation for various skills
that are also important for a quantitative modeller or an engineer:

- Python programming, Linux and cloud computing;
- data pipelines and model productisation;
- experiment design and iterative workflows;
- advanced topics in statistics and machine learning;
- business outcomes and metrics of ML adoption.

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
