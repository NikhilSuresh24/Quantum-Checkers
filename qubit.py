import numpy as np


class Qubit:
    def __init__(self, init_wavefunction=-1, rows=5, cols=5, maxtime=1, N=10):
        self.wavefunction = init_wavefunction
        self.rows = rows  # first index
        self.cols = cols  # second index
        self.xcenter = int(np.ceil(self.rows/2))
        self.ycenter = int(np.ceil(self.cols/2))

        self.k = 0
        self.N = N
        self.timesteps = maxtime*self.N+1

        self.psi = []
        if self.wavefunction == -1:
            self.wavefunction = [
                [0 for i in range(self.rows)] for j in range(self.cols)]
            self.wavefunction[int(np.ceil(rows/2)) -
                                  1][int(np.ceil(cols/2))-1] = 1
        print("k=0", self.wavefunction)
        self.psi.append(self.wavefunction)
        self.generate_wavefunction()

    def __str__(self):
        return "x: "+str(1-self.xcenter)+" -> "+str(self.xcenter-1)+"\n"+"y: "+str(1-self.ycenter)+" -> "+str(self.ycenter-1)+"\n"+"k: 0 -> "+str(self.timesteps)+"\n"+"N="+str(self.N)

    def propogate_wavefunction(self):
        new_wavefunction = [
            [0 for i in range(self.rows)] for j in range(self.cols)]
        for x in range(self.rows):
            for y in range(self.cols):
                for u in range(self.rows):
                    for v in range(self.cols):
                        new_wavefunction[x][y] += self.wavefunction[u][v] * \
                            np.e**((self.N*1j*((u-x)**2+(v-y)**2))/2)
        self.wavefunction = new_wavefunction
        self.psi.append(self.wavefunction)
        print("k="+str(self.k), self.wavefunction)

    def generate_wavefunction(self):
        if self.timesteps-self.k > 0:
            self.k += 1
            self.propogate_wavefunction()
        else:
            print("All done")
            return(self.psi)

    def Psi(self, t, x, y):
        print(int(t*self.N), x+self.xcenter, self.ycenter)
        return self.psi[int(t*self.N)][x+self.xcenter]  # [y+self.ycenter]

    def Prob(self, t, x, y): return np.absolute(self.Psi(t, x, y))


q1 = Qubit(N=2)
print(q1)
print(q1.Psi(0.9, 1, 3)