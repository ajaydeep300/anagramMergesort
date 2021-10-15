from itertools import islice
class Anagram(object):
    def __init__(self, filename):
        self.load_dictionary(filename)

    """
    Helper method to load the dictionary file.
    You may read it in some other way if you want to but do not change the function signature.
    """
    def load_dictionary(self, filename):
        with open(filename) as handle:
            self.dictionary = set(w.strip() for w in handle)
    
    """   
   * Implement the algorithm here. Do not change the function signature.
   *
   * @returns - List of lists, where each element of the outer list is a list containing all the words in that anagram class.
   * example: [['pots', 'stop', 'tops'], ['brake', 'break']]
    """

    def getAnagrams(self):

        set1 = self.dictionary
        dic1 = dict.fromkeys(set1, 0)
        x = iter(dic1.items())
        res1 = dict(islice(x, len(dic1) // 2))
        res2 = dict(x)

        #STEP - DIVIDE- O(n)
        # iterating over the dictionary to divide it into 2 sub dictionaries with equal length
        # takes O(n) time since one loop with n elements
        score1 = {}
        score2 = {}
        for i in res1.keys():
            x = self.mergesorter(i)
            if x in score1.keys():
                y = score1.get(x)
                y.append(i)
                score1.update({x: y})
            else:
                score1.update({x: [i]})
        for i in res2.keys():
            x = self.mergesorter(i)
            if x in score2.keys():
                y = score2.get(x)
                y.append(i)
                score2.update({x: y})
            else:
                score2.update({x: [i]})
        #STEP- CONQUER- O(n/2)
        #looping through each sub dictionary to and apply sorting on both
        # takes 2* O(n/2) time since we are looping through half the number of elements and applying sorting algorithm.

        lis = self.merge(score1, score2)
        listoflist = list(lis.values())

        #STEP- MERGE -O(n)
        # merging both the sorted results from above
        #takes O(n) time since since worst case can be with no anagrams in the dictionary and each word has a different key.

        return listoflist
    def merge(self,r1,r2):
        outpu = dict(r1)
        for k in r2.keys():
            if k in r1.keys():
                outpu[k] = outpu[k] + r2[k]
            else:
                outpu.update({k: [r2[k]]})
        return outpu

    #merging helper method which loops through one dictionary and updates all the values with soimilar keys in both the dictionaries
    def split(self, word):
        res = []
        res[:] = word
        return res
    # splits a word into characters
    # takes O(k) time with k being equal to number of characters in the word.
    def mergesorter(self, word):
        dis = {"a": 2, "b": 3, "c": 5, "d": 7, "e": 11, "f": 13, "g": 17, "h": 19, "i": 23, "j": 29, "k": 31, "l": 37,
               "m": 41, "n": 43, "o": 47, "p": 53, "q": 59, "r": 61, "s": 67, "t": 71, "u": 73, "v": 79, "w": 83,
               "x": 89, "y": 97, "z": 101}
        score = 1
        for i in self.split(word):
            score = score * dis[i]
        return score
    # sorts each word in the dictionary and assigns it a score based on the value assigned to each character,i.e a prime number.
    # takes O(k) time where k is equal to number of characters in the word.
"""
You can use this for debugging if you wish.
"""
if __name__ == "__main__":
    pf = Anagram("dict2.txt")
    print(pf.getAnagrams())

