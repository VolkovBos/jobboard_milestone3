# Imports needed
import os
from app import app
import unittest


# Import my env.py that's ignored by git
if os.path.exists("env.py"):
    import env


# To run the test app
if __name__ == "__main__":
    unittest.main()
