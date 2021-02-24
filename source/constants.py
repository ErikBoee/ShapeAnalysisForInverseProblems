import numpy as np
N_TIME = 100
PIXELS = 300
N_ALPHAS = PIXELS
EXACT_RADON_TRANSFORM = "exact_radon_transform"
ALPHAS = "alphas"
EPSILON = 10**(-7)
STEPSIZE = 1
TOL = 10**(-6)
DELTA = 7 * 10**(-3)
LAMDA = 100
ANGLES = np.linspace(0, np.pi, 10)[:-1]
MAX_LAMDA = 1000000
C_1 = 0.001
C_2 = 0.9
TAU = 0.1
BETA = 0.1
ITERATOR = "Iterator = "
PENALTY_TOL = 10**(-6)
NUMBER_OF_FULL_LOOPS = 5
