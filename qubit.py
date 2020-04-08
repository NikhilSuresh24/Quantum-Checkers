
class Qubit:
    def __init__(self, init_wavefunction=-1, rows=5, columns=5):
        self.wavefunction = init_wavefunction
        if self.wavefunction==-1:
            self.wavefunction = [[0 for i in range(rows)] for j in range(columns)]
            self.wavefunction[3][3] = 1

    def at(self, x, y): # Calculate the probability amplitude at (x,y)
        return self.wavefunction[x-3][y-3]

    def get_next_location(self, delta_time): #TODO:implement
        '''Use get_probability to get probability of being at any locations, uses those probabilities to get the next position, then finally updates position'''
        pass
