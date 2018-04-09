# Backtracking to find Levenshtein Sequence

"The Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other." - Wikipedia

Levenshtein Distance has a lot of use case in NLP. In simplest algorithm of word prediction, Levenshtein Distance is used to find the most similar word. Even in spell correction/detection methodology, Levenshtein Distance can be used to predict the correct spelling of word from a given dictionaty. Typically, Program computes the Levenshtein distance of target word against each word of the dictionary. Word with minimum of distance is prioritize and predicted.

## How to find Levenshtein distance??
Levenshtein distance is very popular application of Dynamic Programming (DP). Since Levenshtein Distance between two strings has the [Optimal Substructure](https://en.wikipedia.org/wiki/Optimal_substructure) property and requires recomputation of sub-problems, Dynamic Programming can be used to memonize the intermediate solution for substructures


## Does two string have unique solution??
Not Always, In most of the cases, There are multiple Levenshtein sequence between two string with equal distance. All solutions are correct though

## Scope of this implementation
This python script is focused to find all Levenshtein Sequence possible. And it requires backtracking the path for finding all the solutions


## Usage

```sh
    $ sequence.py "paris" "alice"
```

## Output

Program will list down all the sequence of minimum edit operation requires to convert "paris" to "alice":

- paris delete p(0) -> aris replace r with l(1) -> alis replace s with c(3) -> alic insert e(3)  ->  alice
- paris delete p(0) -> aris replace r with l(1) -> alis insert c(2) -> alics replace s with e(4)  ->  alice
