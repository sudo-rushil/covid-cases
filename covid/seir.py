
import numpy as np
import matplotlib.pyplot as plt


class SEIR:
    def __init__(self, beta, gamma, sigma):
        '''
        Initializes Markov Chain SEIR solver.
        Params:
         - beta: infectious rate
         - gamma: recovery rate
         - sigma: incubation rate
        '''
        self.beta, self.gamma, self.sigma = beta, gamma, sigma
        self.transitions = np.array([
            [1, 0, 0, 0],
            [0, 1 - sigma, 0, 0],
            [0, sigma, 1 - gamma, 0],
            [0, 0, gamma, 1]
        ])

    def update_transitions(self, I, N):
        '''
        Updates parameters of state transition
        to reflect changes in number of infectious
        individuals in population.
        '''
        self.transitions[0, 0] = 1 - self.beta * I/N
        self.transitions[1, 0] = self.beta * I/N

    def run(self, S, E, I, R, days):
        '''
        Runs simulation on input of population's initial
        distribution, for a given number of days.
        '''
        self.state = np.zeros((days, 4))
        self.state[0] = [S, E, I, R]
        self.update_transitions(I, S + E + I + R)

        for i in range(1, days):
            self.state[i] = self.transitions.dot(self.state[i - 1])
            self.update_transitions(self.state[i, 2], self.state[i].sum())

    def predict(self, S, E, I, R):
        '''
        Uses SEIR simulation to predict when the outbreak
        will die out.
        '''
        state = np.array([S, E, I, R])
        update = lambda I: self.update_transitions(I, sum(state))
        update(I)
        days = 0

        while state[-1]/state.sum() < 0.95:
            state = self.transitions.dot(state)
            update(state[2])
            days += 1

        return days

    def plot(self):
        '''
        Plot SEIR model results after call to self.run.
        '''
        plt.plot(self.state[:, 1])
        plt.plot(self.state[:, 0])
        plt.plot(self.state[:, 3])
        plt.plot(self.state[:, 2])
        plt.legend(['exposed', 'susceptible', 'recovered', 'infected'], loc='upper center')

        return plt.show()
