import numpy as np

class Qubit:
    def __init__(self, init_wavefunction=-1, rows=5, cols=5, maxtime=1, N=10):
        '''
        Give an initial wavefunction state, the size of the 2D field, the extent of the paremetising t-variable, and the level of discretization
        It then runs ::propogate_wavefunction maxtime*N+1 times (cf. ::generate_wavefunction) to create a 3D array of the wavefunction (.psi) in three variables: k, x, y
        With x:0->rows-1 and y:0->cols-1 and k:0->maxtime*N+1
        But ::Psi corrects for this and translates .psi to a reasonable format:
        ::Psi takes three variables: t, x, y. t is "real time" (i.e. discretisation ignored) and x,y are defined so that they are centered at 0 (e.g. -2, -1, 0, 1, 2)
        ::Prob calculates the probability based on the probability amplitude (i.e. |Psi(t,x,y)|^2)
        '''

        self.wavefunction = init_wavefunction
        self.rows = rows # first index
        self.cols = cols # second index
        self.xcenter = int(np.ceil(self.rows/2))
        self.ycenter = int(np.ceil(self.cols/2))
        if round(rows/2)==rows/2 or round(cols/2)==cols/2: print("Even dimensions will make things look strange, proceeding anyway")

        self.k = 0
        self.N = N
        self.timesteps = maxtime*self.N+1

        self.psi = []
        if self.wavefunction==-1:
            self.wavefunction = [[0 for i in range(self.rows)] for j in range(self.cols)]
            self.wavefunction[int(np.ceil(rows/2))-1][int(np.ceil(cols/2))-1] = 1
        print("k=0",self.wavefunction)
        self.psi.append(self.wavefunction)
        self.generate_wavefunction()
    
    def __str__(self):
        return "x: "+str(1-self.xcenter)+" -> "+str(self.xcenter-1)+"\n"+"y: "+str(1-self.ycenter)+" -> "+str(self.ycenter-1)+"\n"+"t: 0 -> "+str((self.timesteps-1)/self.N)+"\n"+"N="+str(self.N)

    def propogate_wavefunction(self):
        new_wavefunction =  [[0 for i in range(self.rows)] for j in range(self.cols)]
        for x in range(self.rows):
            for y in range(self.cols):
                for u in range(self.rows):
                    for v in range(self.cols):
                        new_wavefunction[x][y] += self.wavefunction[u][v] * np.e**((self.N*1j*((u-x)**2+(v-y)**2))/2)
        self.wavefunction = new_wavefunction
        self.psi.append(self.wavefunction)
        print("k="+str(self.k),self.wavefunction)

    def generate_wavefunction(self):
        if self.timesteps-self.k > 0:
            self.k += 1
            self.propogate_wavefunction()
        else:
            print("All done")
            return(self.psi)

    def Psi(self, t, x, y):
        print(int(t*self.N), x+self.xcenter-1, y+self.ycenter-1)
        return self.psi[int(t*self.N)][x+self.xcenter-1][y+self.ycenter-1]
        
    def Prob(self, t, x, y): return np.absolute(self.Psi(t, x, y))