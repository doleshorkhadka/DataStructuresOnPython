
'''
    1. radio_df -- working with dictionary 
        {
        '89.1 MHz': 'BBC Radio 2',
        }
    2. result_sch -- working with value of lists in dictionary 
        {
        'A': [70, 100]
        }
    3.
'''

def radio_ds(name) :
    result = []
    radio_l = []
    fm_frequencies = {
        '89.1 MHz': 'BBC Radio 2',
        '91.3 MHz': 'BBC Radio 3',
        '93.5 MHz': 'BBC Radio 4',
        '94.9 MHz': 'BBC London',
        '95.8 MHz': 'Capital FM',
        '97.3 MHz': 'LBC',
        '98.8 MHz': 'BBC Radio 1',
        '100.0 MHz': 'Kiss FM',
        '100.9 MHz': 'Classic FM',
        '105.4 MHz': 'Magic',
        '105.8 MHz': 'Virgin',
        '106.2 MHz': 'Heart 106.2',
    }

    for key,value in fm_frequencies.items():
        result.append(fm_frequencies[key])
        if name in  value.lower().strip(' '):
            radio_l.append(value)
            keys = key
            # print('You are currently listening to {} at {}'.format(value,key))

    if len(radio_l) == 0:
        print('I know about {} FM radio stations \n {}'.format(len(fm_frequencies),result))
    elif len(radio_l) == 1:
        print('You are currently listening to {} at {}'.format(radio_l,keys))
    else:
        print('You keyword is in {} \n Give full name of channel ! '.format(radio_l))

def result_sch():
    subjects = ['Maths', 'Philosophy', 'Geography', 'Music']
    grade_boundaries = {
        'A': [70, 100],
        'B': [60, 69],
        'C': [50, 59],
        'D': [40, 49],
        'E': [30, 39],
        'F': [0, 29],
    }
    marks = []
    result = {}
    print('Enter your marks in the following subjects:')
    for index , subject in enumerate(subjects):
        marks.append(int(input('What marks did you get in {} ?\n ->'.format(subject))))
        if marks[index] > 100 or marks[index] < 0:
            marks[index] = int(input('Not valid enter again! What marks did you get in {} ?\n ->'.format(subject)))
        for key,value in grade_boundaries.items():
            if marks[index] > value[0] and marks[index] < value[1]:
                result[subject] = key
            
    print('Your grades are :\n {}'.format(result))


if __name__ == '__main__':
    radio_ds('44')
    result_sch()