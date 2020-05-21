#testTechniqueから新規作成
#unit test用のpythonコード

import unittest
from gitPyst import technique_test

class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = CalTest.Cal()
        self.assertEquals(
            cal.add_num_and_double(1,1),4)


if __name__ == '__main__':
    unittest.main()
