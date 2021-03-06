# ---------
# This testing file is part of the Dependency Extractor python package.
# Copyright (c) 2021, Alexandros Raikos tou Konstantinou.
#
# Licensed under the MIT License.
# ---------

import unittest
import os
from pprint import pprint

from dextractor import analyse

if os.getcwd().endswith("dependency-extractor") == False:
    raise Exception(
        """
            -------------------- ERROR --------------------
            Please launch the script from the root directory 
            of the dextractor package.
            -----------------------------------------------
        """
    )


class LanguageTest(unittest.TestCase):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    def test_data_analysis(self):
        """
        Test using the data directory.
        """
        results = analyse(os.getcwd() + "/tests/data",5000000,True,True)
        if not results:
            print("\nNo results were returned.")
        else:
            pprint(results, compact=True)


if __name__ == "__main__":
    unittest.main()