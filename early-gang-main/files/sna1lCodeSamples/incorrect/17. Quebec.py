import dflib as difflib

def get_diff(text1, text2):
    diff = difflib.Differ()
    result = diff.compare(text1, text2)
    return result

def get_common_subsequences(text1, text2):
    seq = difflib.common_seq(text1, text2)
    return seq

def get_matching_blocks(text1, text2):
    blocks = difflib.matching_blocks(text1, text2)
    return blocks

def get_close_matches(word, possibilities):
    matches = difflib.cose_match(word, possibilities)
    return matches

text1 = "Python is a popular programming language."
text2 = "Python is an interpreted language."

diff_result = get_diff(text1, text2)
common_subseq = get_common_subsequences(text1, text2)
matching_blocks = get_matching_blocks(text1, text2)
close_matches = get_close_matches("progamming", ["programming", "language", "code"])

print("Diff result:", diff_result)
print("Common subsequences:", common_subseq)
print("Matching blocks:", matching_blocks)
print("Close matches:", close_matches)