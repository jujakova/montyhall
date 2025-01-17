"""
Simulating the Monty Hall problem using Monte Carlo methods
"""

import numpy as np
import matplotlib.pyplot as plt

class Simulation:
    """ Class to run simulations of the Monty Hall problem and aggregate results.

        This implementation formulates the Monty Hall problem such that: 
            1. The contestant always choses Door 1, 
            2. The host opens either Door 2 or 3 to reveal an empty door, 
            3. The contestant is given the choice to either stay on Door 1 or to switch to the other remaining door.

        Attributes:
            samples: number of simulations run.
            winning_doors: array of sampled integers ranging from [1,3] representing the winning door containing the game show prize for given sample.
            win_if_staying: array of booleans, where True corresponds to the contestant winning if they chose to stay on Door 1.
            win_if_switching:: array of booleans, where True corresponds to the contestant winning if they chose to switch to Door 2/3.
    """

    def __init__(self):
        """ Initialize simulation result arrays.
        """
        self.samples = 0
        self.winning_doors = np.ndarray([]).astype(int)
        self.win_if_staying = np.ndarray([]).astype(bool)
        self.win_if_switching = np.ndarray([]).astype(bool)
        self.num_wins_if_staying = 0
        self.num_wins_if_switching = 0

    def sample(self, n: int):
        """ Perform n number of simulations.
        """
        self.samples += n

        # Sample which door contains a prize using a discrete uniform distribution of [1,3], equivalently [1,4)
        winning_doors = np.random.randint(1, 4, n)

        # Sample which doors host will be presented as a choice. If winning door is 2 or 3, then present winning door as only choice
        # as host will only open a door not containing the prize. If winning door is 1, choose either 2 or 3 on a 50/50 basis.
        switch_doors = np.where(winning_doors == 1, np.random.randint(2,4), winning_doors)
        
        win_if_staying = winning_doors == np.ones(n).astype(int)
        win_if_switching = winning_doors == switch_doors 

        self.num_wins_if_staying += len(win_if_staying[win_if_staying == True])
        self.num_wins_if_switching += len(win_if_switching[win_if_switching == True])

    def plot_results(self):
        """
        """
        if self.samples > 0:
            plt.bar(["Win If Staying", "Win If Switching"], [self.num_wins_if_staying, self.num_wins_if_switching])
            #plt.show()
        else:
            raise Exception("No results to plot. Must sample first.")
        



if __name__ == "__main__":
    sim = Simulation()
    n_samples = 1_000_000
    sim.sample(n_samples)
    sim.plot_results()

    print('Probability of winning if staying: {0:.2f}'.format(sim.num_wins_if_staying / sim.samples * 100.))
    print('Probability of winning if switching: {0:.2f}'.format(sim.num_wins_if_switching / sim.samples * 100.))