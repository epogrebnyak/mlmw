# Interviews

<a name="rc">

## `randomlyCoding` on production pipelines, engineering skills and job roles

[randomlyCoding](https://www.reddit.com/user/randomlyCoding/), a head of AI at a startup who has been working in the field for over a decade: "I certainly don't know everything, but I like to get my feet wet and touch on anything I find interesting. I've trained ML models to do all sorts of tasks and will likely have at least heard of most things."

`MLMW`: **Can one summarize a production pipeline as the following: choosing a business and then a modelling hypothesis -- dataset -- model selection -- training -- validation -- model rollout followed by business metrics? What are the weak links in this process and where a pipeline may break?**

`randomlyCoding`: In general that's about on point. I'd say there's certainly a lot more recursion. For example you might pick a dataset, build a model and train it, only to realize you've massively overfitting because you don't have enough data -- thus you go looking for a bigger additional dataset. Weak links often occur at either end of the process -- you pick a dataset that isn't suited to your problem and thus end up with a solution that solves a problem you weren't trying to solve or the model is 100% perfect but the business case requires inference to happen in real time and it takes 20 minutes based on the size of the model. I've also seen cases of trying to extend a model to do more than it was initially designed for. This isn't always a bad idea but if the person leading this doesn't understand the underlying model there can often be misalignment between their expectations and reality.

`MLMW`: **What skills would you expect an ML engineer (MLE) to know? How can an decent econometrician upgrade to an MLE?***

`randomlyCoding`: I would expect any ML engineer to know one of three Python packages that are the core of most ML processes (either pytorch, tensorflow or keras), but on top of that I'd expect familiarity with some domain specific packages, that might be NLTK if you're working on natural language processing; it might be scikit-learn if you're looking at random forests. One thing I would say is usually a _must_ is familiarity with Linux and a cloud provider (AWS, GCP, Azure). You don't need to know all 3 cloud providers (pick AWS if you don't know any yet -- it has 50% market share) but if you don't know any of them it'll be harder to on board you and your first few weeks would be a lot more overwhelming -- even knowing a different one to the one you use at a specific job will help as they all have similar functionality.

`MLMW`: **Who puts and ML model into production? You got the weights after training, validation stage passed ok, then it always becomes a small API? Who wraps a notebook into API, a designated engineer?**

`randomlyCoding`: Who puts the ML model into production can vary depending on the system in use, it's often an API but not always. I would expect any ML engineer to at least be able to put together a notebook (or similar) that can be used to run inference on the model; in some cases if the organisation is small enough it will be someone who has directly worked on the model; in other cases they may be using a specific orchestration packages that abstracts away this process; in yet other cases it could be hidden behind a message broker. Obviously not all ML models need to be hosted all the time, some are run periodically and they might not require anything more than ingesting a CSV file into a single python script.

`MLMW`: **Does a full-stack data scientist role still exist?**

`randomlyCoding`: I think the full-stack data scientist role does still exist, it will always exists as long as there are start-ups that have limited budgets and big ideas. If you're in a larger team your remit will often be constrained to a specific task, but depending on the organisation your within that task could change regularly (eg. today you're handling data ingestion because the model we're working on is a transformer and you don't have much experience with transformers, but tomorrow we're building a reinforcement learning system and you're the team's expert in RL). In most teams I'd expect the architect of the model to also do a fair amount of the modelling itself; anyone doing modelling will have to work closing with the data engineers, etc. I think this mean the roles aren't as well defined as in SWE and I think this is because there's a lot of trial and error in ML so it's not as simple as for example ingest the data and pass the process on.

`MLMW`: **What is the most unexpected case of a model you thought would not work but it did?**

`randomlyCoding`: Diffusion feels like it shouldn't work. In general it's a multi-step process of removing noise from an image until you end up with the image without any noise; but to do that you start with a completely noisy image and then predict a small percentage of the noise that was added (the previous step of noise added) and then subtract that noise from the image. The maths behind it is reasonably simple, but it just feels like it shouldn't work!
