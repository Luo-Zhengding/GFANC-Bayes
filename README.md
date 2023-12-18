# Delayless Generative Fixed-filter Active Noise Control based on Deep Learning and Bayesian Filter (GFANC-Bayes)

This is the code of the paper '**Delayless Generative Fixed-filter Active Noise Control based on Deep Learning and Bayesian Filter**' accepted by IEEE Transactions on Audio, Speech and Language Processing (TASLP). You can find the paper at [https://ieeexplore.ieee.org/document/10339836/](https://ieeexplore.ieee.org/document/10339836/).

<p align="center">
  <img src="https://github.com/Luo-Zhengding/GFANC-Bayes/assets/95018034/6cfdd241-9fbb-41dd-a535-fa216dcc0f56" alt="" width="700" height="400">
</p>
<p align="center">
</p>

**HIGHLIGHTS:**
1. To address this limitation of the SFANC method and generate more appropriate control filters, a generative fixed-filter active noise control approach based on Bayesian filter (GFANC-Bayes) is proposed in this paper.
   
2. The GFANC-Bayes method can automatically generate suitable control filters by combining sub control filters. The combination weights of sub control filters are predicted via a 1D CNN. The predicted combination weights are then filtered by a Bayesian filtering module, which exploits the correlation information between adjacent noise frames to improve the prediction accuracy and robustness.

3. To achieve delayless noise control, the co-processor operates at the frame rate while the real-time controller performs at the sample rate in parallel.

**How to use the code:**

If you don't want to retrain the 1D CNN ('M5_Network.py'), the trained model can be found in 'models/M6_res_Synthetic.pth', you can easily run the 'Main-GFANC-Bayes.ipynb' file to get the noise reduction results.

The 1D CNN is trained using a synthetic noise dataset, its label files are 'Soft_Index.csv' and 'Hard_Index.csv'. The entire dataset is available at https://drive.google.com/file/d/1hs7_eHITxL16HeugjQoqYFTs-Cm7J-Tq/view?usp=sharing

Especially, the pre-trained sub control filters are obtained on synthetic acoustic paths, where the primary and secondary paths are bandpass filters. If you want to use the GFANC-Bayes system on new acoustic paths only requires obtaining the corresponding broadband control filter and decomposing it into sub control filters. Noticeably, the trained 1D CNN in the GFANC-Bayes system remains unchanged. The detailed information can be found in Section 'Noise Cancellation on Measured Acoustic Paths' in the paper.

**RELATED PAPERS:**
- [Deep Generative Fixed-Filter Active Noise Control](https://arxiv.org/pdf/2303.05788)
- [Delayless Generative Fixed-filter Active Noise Control based on Deep Learning and Bayesian Filter](https://ieeexplore.ieee.org/document/10339836/)
- [GFANC-Kalman: Generative Fixed-Filter Active Noise Control with CNN-Kalman Filtering](https://ieeexplore.ieee.org/document/10323505)
- [A hybrid sfanc-fxnlms algorithm for active noise control based on deep learning](https://arxiv.org/pdf/2208.08082)
- [Performance Evaluation of Selective Fixed-filter Active Noise Control based on Different Convolutional Neural Networks](https://arxiv.org/pdf/2208.08440)
- If you are interested in this work, you can read and cite our papers. Thanks!
