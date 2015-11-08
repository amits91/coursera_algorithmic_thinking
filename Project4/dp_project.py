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
print_sm(build_scoring_matrix('abc', 10, 4, -4))
print_sm(build_scoring_matrix('ACTG', 10, 4, -4))
