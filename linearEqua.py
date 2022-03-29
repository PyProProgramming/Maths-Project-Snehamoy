# Author: Snehashish Laskar
# Date of Creation : 29/3/22
# Project Subject: Maths
# Project Topic: How mathematics can be simulated with computer science


# Creating a class term
class Term:

    def __init__(self, num_coef, variable, sign) -> None:

        self.num_coef = num_coef
        self.variable  = variable
        self.sign = sign

    def __str__(self):

        return self.sign+str(self.num_coef)+self.variable
        
term1  = Term(5, "x", "-")


