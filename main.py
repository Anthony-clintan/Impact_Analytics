import unittest

class SchoolCombination:
    def dfs(self, n, path, counts):
        if len(path) == n:
            counts[0] += 1
            if path[-1] == '0':
                counts[1] += 1
            return
        
        self.dfs(n, path + '1', counts)
        if path[-3:] != '000':
            self.dfs(n, path + '0', counts)

    def count_combinations(self, n):
        #counts[0] for all possibilities, counts[1] probality of missing the Nth day. 
        counts = [0, 0]
        self.dfs(n, '1', counts)
        self.dfs(n, '0', counts)

        ans = str(counts[1])+'/'+str(counts[0])
        return ans

class TestSchoolCombination(unittest.TestCase):
    def setUp(self):
        self.combination_counter = SchoolCombination()

    def test_count_combinations(self):
        # Test case 1: n = 5
        ans = self.combination_counter.count_combinations(5)
        self.assertEqual(ans, '14/29')

        # Test case 2: n = 10
        ans = self.combination_counter.count_combinations(10)
        self.assertEqual(ans, '372/773')  

        # Test case 3: n = 3
        ans = self.combination_counter.count_combinations(3)
        self.assertEqual(ans, '4/8')  


if __name__ == '__main__':
    unittest.main()
