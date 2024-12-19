#------------------------------------------------------------------------------------------------#
# Title: Basic Arithmetic Demo (Processing Classes Script)
# Description: Multi-line Textbox that displays results of arithmetic operations on two operands
# ChangeLog (Who, When, What)
# Rucha Nimbalkar, 12/18/2024, Created Script
# Rucha Nimbalkar, 12/18/2024, Created class MathProcessor
# Rucha Nimbalkar, 12/18/2024, Added methods in the class MathProcessor
#------------------------------------------------------------------------------------------------#

class MathProcessor(object):

    @staticmethod
    def add(n1,n2): return (n1+n2)

    @staticmethod
    def subtract(n1, n2): return (n1 - n2)

    @staticmethod
    def multiply(n1, n2): return (n1 * n2)

    @staticmethod
    def divide(n1, n2): return n1 /n2

#End class