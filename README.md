# Spell-Checker
This is an individual project based on a Naive Bayesian Spell Checker.

The default Dataset used is the War and Peace book by Leo Tolstoy from Project Gutenburg Website (https://www.gutenberg.org/cache/epub/2600/pg2600.txt).
However, an option is provided of using own dataset.

How the Spell Checker works:
1. A frequency table (in form of a dictionary) is prepared from the dataset. This serves two purposes:
  i. Every unique word from the dataset is treated as valid word.
  ii. Each word has a frequency associated with it. This is used in calculating the Probability of its occurence (Higher the frequency, higher its probability of being referred).
2. The input to the class is your word file (in txt format). The spell checker traverses through each word (assumes that it is misspelled), and performs a search for the most likely valid word (which can be the same word)
3. Essentially it is a Bayesian Classification. It classifies the word into different valid words which can be obtained from it (via permuting/deletion/insertion/replacement), finds the probability of that classification, and chooses the one which maximum probability.
4. What makes it Naive is the fact that we assume that the occurence of each word is independent of other words. Although this is a imperfect assumption, it provides a decent prediction.
5. The conditional probability function requires a few base variables, which have a default value set. However, you can provide your own values for them.

The Alternate valid words (or classifications) are obtained as following:
1. Cyclic Permutation: O(n)
2. Swapping one character : O(n^2)
3. Deleting one character : O(n)
4. Inserting one character : O(n^2)
5. Replacing one character : O(n^2)
Further changes in terms of more characters can be made to increase the accuracy, but keeping in mind the speed of the checker, it is not recommended.

Accuracy : 90%
