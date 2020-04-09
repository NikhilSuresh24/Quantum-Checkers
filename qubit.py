import numpy as np

class Qubit:
    def __init__(self, init_wavefunction=-1, rows=5, cols=5, timesteps=1, N=10):
        self.wavefunction = init_wavefunction
        self.rows = rows # first index
        self.cols = cols # second index
        self.k = 0
        self.psi = []
        self.timesteps = timesteps
        self.N = N
        if self.wavefunction==-1:
            self.wavefunction = [[0 for i in range(self.rows)] for j in range(self.cols)]
            self.wavefunction[round(rows/2)][round(cols/2)] = 1
        self.generate_wavefunction()

    def propogate_wavefunction(self):
        new_wavefunction =  [[0 for i in range(self.rows)] for j in range(self.cols)]
        for x in range(self.rows):
            for y in range(self.cols):
                for u in range(self.rows):
                    for v in range(self.cols):
                        new_wavefunction[x][y] += self.wavefunction[u][v] * np.e**((self.N*1j*((u-x)**2+(v-y)**2))/2)
        self.psi.append(self.wavefunction)
        self.wavefunction = new_wavefunction
        print(self.wavefunction)

    def generate_wavefunction(self):
        if self.timesteps > 0:
            self.timesteps -= 1
            self.k += 1
            self.propogate_wavefunction()
        else:
            print("All done")
            return(self.psi)

    def Psi(self, t, x, y): return self.psi[t*self.N][x][y]
    def Prob(self, t, x, y): return 

q1 = Qubit(timesteps = 3)