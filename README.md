This is the code of the paper '**Delayless Generative Fixed-filter Active Noise Control based on Deep Learning and Bayesian Filter**' accepted by IEEE Transactions on Audio, Speech and Language Processing (TASLP).

<p align="center">
  <img src="https://github.com/Luo-Zhengding/GFANC-Bayes/assets/95018034/6cfdd241-9fbb-41dd-a535-fa216dcc0f56" alt="" width="700" height="400">
</p>
<p align="center">
</p>

**HIGHLIGHTS:**
1. To address this limitation of the SFANC method and generate more appropriate control filters, a generative fixed-filter active noise control approach based on Bayesian filter (GFANC-Bayes) is proposed in this paper.
   
2. The GFANC-Bayes method can automatically generate suitable control filters by combining sub control filters. The combination weights of sub control filters are predicted via a 1D CNN. The predicted combination weights are then filtered by a Bayesian filtering module, which exploits the correlation information between adjacent noise frames to improve the prediction accuracy and robustness.

3. To achieve delayless noise control, the co-processor operates at the frame rate while the real-time controller performs at the sample rate in parallel. Simulations on real-world noises indicate that the GFANC-Bayes method achieves superior noise reduction performance than SFANC and a faster response time than FxLMS. Moreover, experiments on different acoustic paths demonstrate its robustness and transferability.

**How to use the code:**

If you don't want to retrain the 1D CNN ('M5_Network.py'), the trained model can be found in 'models/M6_res_Synthetic.pth', you can easily run the 'Main-GFANC-Bayes.ipynb' file to get the noise reduction results.

Especially, the pre-trained sub control filters are obtained on synthetic acoustic paths, where the primary and secondary paths are bandpass filters. If you want to use the GFANC-Bayes system on new acoustic paths only requires obtaining the corresponding broadband control filter and decomposing it into sub control filters. Noticeably, the trained 1D CNN in the GFANC-Bayes system remains unchanged. The detailed information can be found in Section 'Noise Cancellation on Measured Acoustic Paths' in the paper.

**RELATED PAPERS:**
- [Deep Generative Fixed-Filter Active Noise Control](https://arxiv.org/pdf/2303.05788)
- [GFANC-Kalman: Generative Fixed-Filter Active Noise Control with CNN-Kalman Filtering](https://ieeexplore.ieee.org/document/10323505)
- [A hybrid sfanc-fxnlms algorithm for active noise control based on deep learning](https://arxiv.org/pdf/2208.08082)
- [Performance Evaluation of Selective Fixed-filter Active Noise Control based on Different Convolutional Neural Networks](https://arxiv.org/pdf/2208.08440)
If you are interested in this work, you can read and cite our papers. Thanks!
