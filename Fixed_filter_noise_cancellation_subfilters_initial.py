# Fixed filter noise cancellation by Sample
# With initial control filter

import torch
from scipy.io import loadmat


class Fixed_filter_controller():
    def __init__(self, Filter_vector, fs):
        self.Filter_vector = torch.from_numpy(Filter_vector).type(torch.float)# torch.Size([Xseconds, 1024])
        Len = self.Filter_vector.shape[1]
        self.fs = fs
        self.Xd = torch.zeros(1, Len, dtype=torch.float)
        mat_contents = loadmat('models/Initial_Control_Filter.mat')
        Initial = mat_contents['Initial']
        self.Current_Filter = torch.from_numpy(Initial) #torch.Size([1, 1024])
        self.Current_Filter = self.Current_Filter.to(torch.float32)
    
    def noise_cancellation(self, Dis, Fx):
        Erro = torch.zeros(Dis.shape[0])
        j = 0
        for ii, dis in enumerate(Dis):
            self.Xd = torch.roll(self.Xd,1,1)
            self.Xd[0,0] = Fx[ii] # Fx[ii]: fixed-x signal
            yt = self.Current_Filter @ self.Xd.t()
            e = dis - yt
            Erro[ii] = e.item()
            if (ii + 1) % self.fs == 0:
                self.Current_Filter = self.Filter_vector[j]
                j += 1
        return Erro