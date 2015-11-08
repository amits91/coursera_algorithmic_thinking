"""
Provide code and solution for Application 4
"""

DESKTOP = True

import math
import random
import urllib2

if DESKTOP:
    import matplotlib.pyplot as plt
    import dp_project as student
else:
    import simpleplot
    import userXX_XXXXXXX as student


# URLs for data files
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"



###############################################
# provided code

def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    scoring_file = urllib2.urlopen(filename)
    ykeys = scoring_file.readline()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict

def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
    protein_file = urllib2.urlopen(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.rstrip()
    return protein_seq

def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    word_file = urllib2.urlopen(filename)

    # read in files as string
    words = word_file.read()

    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print "Loaded a dictionary with", len(word_list), "words"
    return word_list

hseq = read_protein(HUMAN_EYELESS_URL)
fseq = read_protein(FRUITFLY_EYELESS_URL)
pm50 = read_scoring_matrix(PAM50_URL)

am50 = student.compute_alignment_matrix(hseq, fseq, pm50, False)
res = student.compute_local_alignment(hseq, fseq, pm50, am50 )

def print_res(res, label):
    print "Score:", res[0]
    print label[0], res[1]
    print label[1], res[2]

print_res(res,["Human   :", "Fruitfly:"])

cpax = read_protein(CONSENSUS_PAX_URL)
# print 'cpax:', cpax
hdseq = res[1].replace('-', '')
# print 'h no d:', hdseq
amhc = student.compute_alignment_matrix(hdseq, cpax, pm50, True)
gah = student.compute_global_alignment(hdseq, cpax, pm50, amhc)
# gah = student.compute_global_alignment(cpax, hdseq, pm50, am50)
print_res(gah,["Human:", "CPAX :"])
dashh = gah[1].count('-')
dashc = gah[2].count('-')
print "dash h:", dashh, 'dashc:', dashc, 'lenh:', len(gah[1]), 'lenc:', len(gah[2])

print 'Percentage Agree Human:', 100 * (((len(gah[1]) - (dashh + dashc)) * 1.0)/len(gah[1])),"%"
fdseq = res[2].replace('-', '')
amfc = student.compute_alignment_matrix(fdseq, cpax, pm50, True)
gaf = student.compute_global_alignment(fdseq, cpax, pm50, amfc)
print_res(gaf,["Fruitfly:", "CPAX    :"])
dashh = gaf[1].count('-')
dashc = gaf[2].count('-')
print "dash h:", dashh, 'dashc:', dashc, 'lenh:', len(gah[1]), 'lenc:', len(gah[2])

print 'Percentage Agree Fruitfly:', 100 * (((len(gah[1]) - (dashh + dashc)) * 1.0)/len(gah[1])),"%"

def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    sdist = { }
    # l = list(seq_y)
    for i in range(num_trials):
        l = list(seq_y)
        random.shuffle(l)
        rand_y = ''.join(l)
        am = student.compute_alignment_matrix(seq_x, rand_y, scoring_matrix, False)
        las = student.compute_local_alignment(seq_x, rand_y, scoring_matrix, am)
        score = las[0]
        if sdist.has_key(score):
            sdist[score] = sdist[score] + 1
        else:
            sdist[score] = 1
    return sdist

num_trials = 1000
dist = generate_null_distribution(hseq, fseq, pm50, num_trials)
disthf = {}
for i in dist.keys():
    disthf[i] = (dist[i] * 1.0) / num_trials
print 'Unnormalized Dist:', dist
print 'Normalized Dist:', disthf

sum = 0
for i in dist.keys():
    sum = dist[i] + sum
mean = (sum * 1.0) / len(dist)
sd = 0.0
for i in dist.keys():
    sd = math.pow(dist[i] - mean, 2) + sd

sdv = math.sqrt((sd  * 1.0)/len(dist))
print "s:", res[0]
print "Mean:", mean
print "Standard Deviation:", sdv
print "z-score:", (res[0] - mean)/sdv


plt.bar(disthf.keys(), disthf.values(), label='statistical hypothesis')
plt.xlabel('Scores')
plt.ylabel('Fraction of trails')
plt.title('Normalized distribution of generate_null_distribution')
plt.grid(True)
# plt.legend(loc='upper right')
plt.show()
