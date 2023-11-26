This is the code of the paper '**Delayless Generative Fixed-filter Active Noise Control based on Deep Learning and Bayesian Filter**' accepted by IEEE Transactions on Audio, Speech and Language Processing (TASLP).

<p align="center">
  <img src="https://github.com/Luo-Zhengding/GFANC-Bayes/assets/95018034/6cfdd241-9fbb-41dd-a535-fa216dcc0f56" alt="" width="700" height="600">
</p>
<p align="center">
</p>

This paper is an improvement upon my ICASSP paper 'Deep Generative Fixed-Filter Active Noise Control (GFANC)'.
The code of GFANC: https://github.com/Luo-Zhengding/GFANC-Generative-fixed-filter-active-noise-control

1. In our ICASSP 2023 paper, GFANC generates its control filter solely using information from the current noise frame. Compared to GFANC in the ICASSP paper, the GFANC-Bayes approach improves the generation of control filters by exploiting the correlation between adjacent noise frames based on Bayesian filter.
   
2. A lightweight one-dimensional CNN is developed to automatically predict the combination weights of sub control filters given the input noise. The combination weights are then filtered by a Bayesian decision module using prior weights and predicted weights.

3. Due to the efficient collaboration between the co-processor and real-time processor, the GFANC system can achieve delayless noise reduction. Additionally, the GFANC method requires only one pre-trained broadband control filter as prior data to generate various control filters.

* You can easily run the "Main-GFANC-Bayes.ipynb" file to get the noise reduction results.

If you are interested in the works, you can read and cite our papers. Thanks!
