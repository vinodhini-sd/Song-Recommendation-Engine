# definie class similarity
class similarity:

    # Class instantiation
    def __init__(self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ

    # Minkowski Distance between two vectors
    def minkowski(self, r):
        # calcualte minkowski distance
        distance = 0
        for k in (set(self.ratings1.keys()) & set(self.ratings2.keys())):
            p = self.ratings1[k]
            q = self.ratings2[k]
            distance += pow(abs(p - q), r)

        # return value of minkowski distance
        return round(pow(distance, 1 / r), 2)

    # Pearson Correlation between two vectors
    def pearson(self):
        n = 0
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_y2 = 0
        for item in (set(self.ratings1.keys()) & set(self.ratings2.keys())):
            x = self.ratings1[item]
            y = self.ratings2[item]
            n += 1
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += (x * x)
            sum_y2 += (y * y)
        if n == 0:
            # print("No common keys. Returning error code -2")
            return -2
        else:
            denominator = pow(sum_x2 - (pow(sum_x, 2) / n), 1 / 2) * pow(sum_y2 - pow(sum_y, 2) / n, 1 / 2)
            if denominator == 0:
                # print("Denominator is zero. Returning error code -2")
                return -2
            else:
                numerator = (sum_xy - (sum_x * sum_y) / n)
                return round(numerator / denominator, 2)
