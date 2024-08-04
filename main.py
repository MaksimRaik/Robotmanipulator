import numpy as np

class parametrs:

    def __init__(self, x, y, L1, L2, L3):

        self.x = x
        self.y = y
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3

    def coordinate_test_start(self):

        if np.sqrt(self.x**2 + self.y**2) > self.L1 +self.L2 + self.L3:

            print( f'Error x = {self.x} and y= {self.y} out of range' )

            return False

        return True

    def coordinate_test_end(self, un1, un2, un3):

        x = self.L1 * np.cos(un1) + self.L2 * np.cos(un3) + self.L3

        y = self.L1 * np.sin(un1) + self.L2 * np.sin(un3)

        if x != self.x or y!= self.y:

            print( f'Error x = {self.x} and y= {self.y} out of range' )

            return False

        return True

    def calc_ungle(self):

        if self.coordinate_test_start():

            theta_1 = np.arccos( (self.L2**2 - self.L1**2 - self.y**2 - (self.x - self.L3)**2) /
                             (2 * self.L1 * np.sqrt( self.y**2 +(self.x - self.L3)**2 ) ) ) - np.arctan( self.y / (self.x - self.L3) )

            theta_2 = np.arccos( (self.y**2 +(self.x - self.L3)**2 - self.L2**2 - self.L1**2) / 2. / self.L1 / self.L2 )

            theta_3 = theta_1 + theta_2

            if theta_1 >= 3. * np.pi / 2. or theta_1 < 0.0:

                print( f'Error theta_1 = {theta_1 / np.pi * 180.} out of range' )

            elif theta_2 < 0.0 or theta_2 >= 3. * np.pi / 4.:

                print( f'Error theta_2 = {theta_2 / np.pi * 180.} out of range' )

            elif theta_3 < 0.0 or theta_3 >= 5. * np.pi / 4.:

                print( f'Error theta_2 = {theta_3 / np.pi * 180.} out of range' )

            elif self.coordinate_test_end(theta_1, theta_2, theta_3):

                return theta_1 / np.pi * 180., theta_2 / np.pi * 180., theta_3 / np.pi * 180.

        else:

            return False

ungle1 = parametrs(2., 4., 3.2, 2., 0.2)

print(ungle1.calc_ungle())

