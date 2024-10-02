# Bayesian Belief Networks

## Problem Statement for the Project
Construct a causal network and follow the reasoning in the following story. 
Mr. Holmes is working in his office when he receives a phone call from his neighbour informing him that his burglar alarm is ringing. Convinced that a burglar has broken into his house, Holmes rushes home in his car. On the way, he hears on the radio that there has been an earthquake in the area where his home is located. Earthquakes have a tendency to trigger burglar alarms. Now, Holmes must decide whether to continue going home or return to the office. Incorporate this scenario and explain his decisions.
![[causal_network.png]]
![[causal_network_with_probs.png]]
# Sources
### Wikipedia
1. [Conditional probability](https://en.wikipedia.org/wiki/Conditional_probability)
2. [Bayes' theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem)
3. [Bayesian network](https://en.wikipedia.org/wiki/Bayesian_network)
# Background
## Conditional probability
- **Conditional probability** is a measure of the probability of an event occurring, given that another event (by assumption, presumption, assertion or evidence) is already known to have occurred. 
- This particular method relies on event $A$ occurring with some sort of relationship with another event $B$. In this situation, the event $A$ can be analysed by a conditional probability with respect to $B$. If the event of interest is $A$ and the event $B$ is known or assumed to have occurred, "the conditional probability of $A$ given $B$", or "the probability of $A$ under the condition $B$", is usually written as $P(A|B)$.
- This can also be understood as the fraction of probability $B$ that intersects with $A,$ or the ratio of the probabilities of both events happening to the "given" one happening (how many times $A$ occurs rather than not assuming $B$ has occurred):
$$
P(A|B) = \frac{P(A \cap B)}{P(B)}.
$$
## Bayes' theorem
- **Bayes' theorem** gives a mathematical rule for inverting conditional probabilities, allowing us to find the probability of a cause given its effect.
- For example, if the risk of developing health problems is known to increase with age, Bayes' theorem allows the risk to an individual of a known age to be assessed more accurately by conditioning it relative to their age, rather than assuming that the individual is typical of the population as a whole.
### Statement of theorem
- Bayes' theorem is stated mathematically as the following equation:
$$P(A|B) = \frac {P(B|A)P(A)}{P(B)}$$
where $A$ and $B$ are and $P(B)\neq0$.
- $P(A|B)$ is a conditional probability: the probability of event $A$ occurring given that $B$ is true. It is also called the posterior probability of $A$ given $B$.
- $P(B|A)$ is also a conditional probability: the probability of event $B$ occurring given that $A$ is true. It can also be interpreted as the likelihood of $A$ given a fixed $B$ because $P(B|A)=L(A|B)$.
- $P(A)$ and $P(B)$ are the probabilities of observing $A$ and $B$ respectively without any given conditions; they are known as the prior probability and marginal probability.
#### Proof
Bayes' theorem may be derived from the definition of conditional probability:
$$
P(A|B) = \frac{P(A \cap B)}{P(B)}, \text{ if } P(B) \neq 0,
$$
where $P(A \cap B)$ is the probability of both $A$ and $B$ being true. Similarly,
$$
P(B|A) = \frac{P(A \cap B)}{P(A)}, \text{ if } P(A) \neq 0.
$$
Solving for $P(A \cap B)$ and substituting into the above expression for $P(A|B)$ yields Bayes' theorem:
$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}, \text{ if } P(B) \neq 0.
$$
![[visual-proof-of-bayes.png]]
# Bayesian network
- A **Bayesian network** (also known as a **belief network**) is a probabilistic graphical model that represents a set of variables and their conditional dependencies via a directed acyclic graph (DAG).
- Bayesian networks are ideal for taking an event that occurred and predicting the likelihood that any one of several possible known causes was the contributing factor. For example, a Bayesian network could represent the probabilistic relationships between diseases and symptoms. Given symptoms, the network can be used to compute the probabilities of the presence of various diseases.
## Graphical model
- Formally, Bayesian networks are directed acyclic graphs whose nodes represent variables in the Bayesian sense: they may be observable quantities, latent variables, unknown parameters or hypotheses. Each edge represents a direct conditional dependency. Any pair of nodes that are not connected (i.e. no path connects one node to the other) represent variables that are conditionally independent of each other. Each node is associated with a probability function that takes, as input, a particular set of values for the node's parent variables, and gives (as output) the probability (or probability distribution, if applicable) of the variable represented by the node. 
## Example
- Let us use an illustration to enforce the concepts of a Bayesian network. Suppose we want to model the dependencies between three variables: the sprinkler (or more appropriately, its state - whether it is on or not), the presence or absence of rain and whether the grass is wet or not. Observe that two events can cause the grass to become wet: an active sprinkler or rain. Rain has a direct effect on the use of the sprinkler (namely that when it rains, the sprinkler usually is not active). This situation can be modelled with a Bayesian network (shown to the right). Each variable has two possible values, T (for true) and F (for false).
The joint probability function is, by the chain rule of probability,
$$
\Pr(G,S,R) = \Pr(G \mid S,R) \Pr(S \mid R) \Pr(R)
$$
where G = "Grass wet (true/false)", S = "Sprinkler turned on (true/false)", and R = "Raining (true/false)".
- The model can answer questions about the presence of a cause given the presence of an effect (so-called inverse probability) like "What is the probability that it is raining, given the grass is wet?" by using the conditional probability formula and summing over all nuisance variables:
$$
\displaystyle 
\Pr(R = T \mid G = T)= {\frac {\Pr(G=T,R=T)}{\Pr(G=T)}} = {\frac {\sum _{x\in \{T,F\}}\Pr(G=T,S=x,R=T)}{\sum _{x,y\in \{T,F\}}\Pr(G=T,S=x,R=y)}}
$$
- Using the expansion for the joint probability function $\Pr(G,S,R)$ and the conditional probabilities from the conditional probability tables (CPTs) stated in the diagram, one can evaluate each term in the sums in the numerator and denominator. For example, 
$$P(G,S,R) = \text{Probablility that the grass is wet and the sprinkler is on and it is raining}$$
$$
\begin{aligned}
\Pr(G = T,S = T,R = T)
&= \Pr(G = T \mid S = T, R = T) \Pr(S = T \mid R = T) \Pr(R = T)\\
&= 0.99 \times 0.01 \times 0.2\\
&= 0.00198\\
&= 0.198\%.
\end{aligned}
$$
![[simple-bayesian-network-example.png]]
