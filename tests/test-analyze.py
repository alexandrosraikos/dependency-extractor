# ---------
# This testing file is part of the Dependency Extractor python package.
# Copyright (c) 2021, Alexandros Raikos tou Konstantinou.
#
# Licensed under the MIT License.
# ---------

import unittest
import os
from pprint import pprint

from dextractor import analyze

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
        pprint(analyze(os.getcwd() + "/tests/data"))


if __name__ == "__main__":
    unittest.main()