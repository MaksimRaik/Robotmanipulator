import numpy as np

class parametrs:

    def __init__(self, x, y, L1, L2, L3):

        self.x = x
        self.y = y
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3

    def calc_ungle(self):

        theta_1 = np.arccos( (self.L2**2 - self.L1**2 - self.y**2 - (self.x - self.L3)**2) /
                             (2 * self.L1 * np.sqrt( self.y**2 +(self.x - self.L3)**2 ) ) ) - np.arctan( self.y / (self.x - self.L3) )

        theta_2 = np.arccos( (self.y**2 +(self.x - self.L3)**2 - self.L2**2 - self.L1**2) / 2. / self.L1 / self.L2 )

        theta_3 = theta_1 + theta_2

        return theta_1 / np.pi * 180., theta_2 / np.pi * 180., theta_3 / np.pi * 180.

ungle1 = parametrs(3., 4., 3.2, 2., 0.2)

print(ungle1.calc_ungle())

