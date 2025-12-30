# Probability and statistics

## Beginner

- [Seeing Theory](https://seeing-theory.brown.edu/basic-probability/index.html) visual textbook.
- [Probability distributions](https://jverzani.github.io/UsingJ/Inference/distributions.html).

### Bayes' Theorem

Bayes' Theorem is a fundamental result in probability that describes how to update the probability of a hypothesis when given new evidence. It is expressed as:

\[
P(A|B) = \frac{P(B|A) P(A)}{P(B)}
\]

where:
- \( P(A|B) \) is the posterior probability of hypothesis \( A \) given evidence \( B \).
- \( P(B|A) \) is the likelihood of observing evidence \( B \) given that \( A \) is true.
- \( P(A) \) is the prior probability of hypothesis \( A \) before seeing evidence \( B \).
- \( P(B) \) is the marginal probability (or evidence) of observing \( B \) under all possible hypotheses.

#### Intuition

Bayes' Theorem provides a mathematical framework for updating beliefs in light of new data. The prior represents our initial belief about the hypothesis; the likelihood quantifies how consistent the new evidence is with the hypothesis; and the posterior is our revised belief after incorporating the evidence.

#### Worked Example: Medical Testing

Suppose a certain disease affects 1% of the population. A test for the disease has a 95% true positive rate (sensitivity) and a 90% true negative rate (specificity). That is:
- If a person has the disease, the test will be positive with probability 0.95.
- If a person does not have the disease, the test will be negative with probability 0.90 (so false positive rate = 0.10).

If a randomly selected individual tests positive, what is the probability they actually have the disease?

Let:
- \( D \) = event that the person has the disease.
- \( T^+ \) = event that the test is positive.

We know:
- Prior: \( P(D) = 0.01 \)
- Sensitivity: \( P(T^+|D) = 0.95 \)
- False positive rate: \( P(T^+|\neg D) = 0.10 \)

We need the posterior \( P(D|T^+) \). Using Bayes' Theorem:

\[
P(D|T^+) = \frac{P(T^+|D) P(D)}{P(T^+)}
\]

Compute the marginal probability of a positive test:
\[
P(T^+) = P(T^+|D)P(D) + P(T^+|\neg D)P(\neg D) = 0.95 \times 0.01 + 0.10 \times 0.99 = 0.0095 + 0.099 = 0.1085
\]

Now plug into Bayes' formula:
\[
P(D|T^+) = \frac{0.95 \times 0.01}{0.1085} \approx \frac{0.0095}{0.1085} \approx 0.0876
\]

Thus, even with a positive test result, the probability of actually having the disease is only about 8.8%. This illustrates the importance of considering base rates (prior) when interpreting test results.

#### Common Pitfalls

1. **Confusing \( P(A|B) \) with \( P(B|A) \)** – the "prosecutor's fallacy" in legal contexts.
2. **Ignoring the prior** – assuming that a test with high sensitivity/specificity guarantees a high posterior probability, which is not true when the prior is low.
3. **Misinterpreting the marginal probability** – forgetting to compute \( P(B) \) correctly, which requires the law of total probability.

#### Applications

- **Machine Learning**: Naive Bayes classifiers for text classification.
- **Statistics**: Bayesian inference, where prior beliefs are updated with observed data to obtain posterior distributions.
- **Decision Making**: Medical diagnosis, spam filtering, risk assessment, and many real‑world problems where uncertainty must be quantified.

## Courses

- [Statistics 110 (Probability) by Joe Blitzstein](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo).

## Reference

- [Chapter 6 "Probability and Distributions"](https://mml-book.github.io/book/mml-book.pdf) in the MML book.
- [P4D](https://probability4datascience.com/).

## Advanced

- [Aubrey Clayton](https://www.youtube.com/watch?v=rfKS69cIwHc&list=PL9v9IXDsJkktefQzX39wC2YG07vw7DsQ_&index=1&t=102s) reading of
  [The Logic of Science by E.T. Jaynes](http://www.med.mcgill.ca/epidemiology/hanley/bios601/GaussianModel/JaynesProbabilityTheory.pdf).