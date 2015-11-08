'''
Dynamic Programming for Computing Alignment
'''


def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    '''
    build_scoring_matrix
    :param alphabet:
    :param diag_score:
    :param off_diag_score:
    :param dash_score:
    :return: dictionary of dictionary: scoring_matrix[row_char][col_char], E U {'-'}
    '''
    scoring_matrix = { }
    scoring_matrix['-'] = {'-': dash_score}
    for cols in alphabet:
        scoring_matrix[cols] = {'-': dash_score}
    for cols in alphabet:
        scoring_matrix['-'][cols] = dash_score
    for rows in alphabet:
        for cols in alphabet:
            if rows == cols:
                scoring_matrix[rows][cols] = diag_score
            else:
                scoring_matrix[rows][cols] = off_diag_score
    return scoring_matrix

def print_sm(mat):
    '''
    :param mat:
    :return:
    '''
    # print mat
    print '  :',
    for data in sorted(mat.keys()):
        print '  ', data,
    print
    vals = sorted(mat.items())
    for val in vals:
        print val[0], ':',
        for item in sorted(val[1].items()):
            data = item[1]
            if -10 < data < 0:
                print ' ', data,
            elif data < -10:
                print '', data,
            elif -1 < data < 10:
                print '  ', data,
            else:
                print ' ', data,
        print

# print_sm({'1': {'2':4}})
# print_sm(build_scoring_matrix('abc', 10, 4, -4))
# print_sm(build_scoring_matrix('ACTG', 10, 4, -4))

def check_val(global_flag, val):
    '''
    :param global_flag:
    :param val:
    :return:
    '''
    if val < 0 and global_flag == False:
        return 0
    else:
        return val

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    '''
    :param seq_x:
    :param seq_y:
    :param scoring_matrix:
    :param global_flag:
    :return:
    '''
    mval = len(seq_x) + 1
    nval = len(seq_y) + 1
    align_mat = [[-1 for dummy_col in range(nval)] for dummy_row in range(mval)]
    align_mat[0][0] = 0
    for idx in range(1, mval):
        align_mat[idx][0] = check_val(global_flag, align_mat[idx - 1][0] + scoring_matrix[seq_x[idx - 1]]['-'])
    for idx in range(1, nval):
        align_mat[0][idx] = check_val(global_flag, align_mat[0][idx - 1] + scoring_matrix['-'][seq_y[idx - 1]])
    for idx in range(1, mval):
        for jdx in range(1, nval):
            val = max(align_mat[idx - 1][jdx] + scoring_matrix[seq_x[idx - 1]]['-'], align_mat[idx][jdx - 1] + scoring_matrix['-'][seq_y[jdx - 1]])
            align_mat[idx][jdx] =  check_val(global_flag, max(align_mat[idx - 1][jdx - 1] + scoring_matrix[seq_x[idx - 1]][seq_y[jdx - 1]], val))

    return align_mat

print  [[0, -4, -8, -12], [-4, 6, 2, -2], [-8, 2, 8, 4], [-12, -2, 4, 14]]
print compute_alignment_matrix('ATG', 'ACG', {'A': {'A': 6, 'C': 2, '-': -4, 'T': 2, 'G': 2}, 'C': {'A': 2, 'C': 6, '-': -4, 'T': 2, 'G': 2}, '-': {'A': -4, 'C': -4, '-': -4, 'T': -4, 'G': -4}, 'T': {'A': 2, 'C': 2, '-': -4, 'T': 6, 'G': 2}, 'G': {'A': 2, 'C': 2, '-': -4, 'T': 2, 'G': 6}}, True)
# print compute_alignment_matrix('ACT', 'ACCG', build_scoring_matrix('ACGT', 10, 4, -4), False)

