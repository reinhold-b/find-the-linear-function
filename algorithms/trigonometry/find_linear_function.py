"""
Given two coordinates, this algorithm will find the linear function
those two coordinates lay on:

Example:
X [1, 3], Y [2, 5] --> f(x) = 2x + 1

"""


class equationFinder:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def validate(self, X, Y):
        """Validate if the X and Y coordinates aren't the same"""
        if (X == Y):
            return False
        return True

    def find_slope(self, X, Y):
        """Find the slope of the function"""
        self.slope = (Y[1] - X[1]) / (Y[0] - X[0])
        return round(self.slope) if self.slope % 1 == 0 else self.slope

    def find_axis_intercept(self, slope, X):
        """Find the y-intercept by solving the equation"""
        y, x = X[1], X[0]
        self.axis_intercept = y - self.slope * x
        if self.axis_intercept % 1 == 0:
            self.axis_intercept = round(self.axis_intercept)
        if self.axis_intercept > 0:
            self.axis_intercept = f"+ {self.axis_intercept}"
        else:
            self.axis_intercept = str(self.axis_intercept)
        return f"{self.axis_intercept}" if self.axis_intercept != "0" else ""

    def find_equation(self):
        """Call this method to solve find the equation"""
        validiation = self.validate(self.X, self.Y)
        if validiation:
            slope = self.find_slope(self.X, self.Y)
            axis_intercept = self.find_axis_intercept(slope, self.X)
            return f"\n\nEquation: {round(slope, 3)}x " + (str(axis_intercept)) + "\n\n"

        return "No function!"
