
'''
    1. radio_df -- working with dictionary 
    2. rgb_finder -- working with 2D list && use of List_comprehension([expression for item in list])
    3. result_sch -- working with value of lists in dictionary 
    4. football_res -- working with value of dictionaries in list
    5. sort -- sorting dictionary by value and sorting list
'''



def radio_ds(name) :
    result = []
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
            print('You are currently listening to {} at {}'.format(value,key))
            return None
    print('I know about {} FM radio stations \n {}'.format(len(fm_frequencies),result))
    
def rgb_finder(key):
    colours = [
    ['red', 'F00'],
    ['yellow', 'FF0'],
    ['green', '0F0'],
    ['cyan', '0FF'],
    ['blue', '00F'],
    ['magenta', 'F0F'],
    ]
    result = [x for x in colours if x[0] is key]   
    print('The rgb code for {} is {}'.format(key,result[0][1]))

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
            
def football_res():
    results = [
        {'Austria': 0, 'Hungary': 2},
        {'Portugal': 1, 'Iceland': 1},
        {'Iceland': 1, 'Hungary': 1},
        {'Portugal': 1, 'Austria': 0},
        {'Iceland': 2, 'Austria': 1},
        {'Hungary': 3, 'Portugal': 3},
    ]
    df = {}
    h_teams = {}
    l_teams = {}
    lowest_goal = 0
    highest_goal = 0
    most_total_goals = {}
    for result in results:
        goal = 0
        for key in result:
            if key in h_teams.keys():
                if result[key] >= h_teams[key]:
                    h_teams[key] = result[key]
                if result[key] < l_teams[key] or result[key] == 0:
                    l_teams[key] = result[key]
            else:
                l_teams[key] = result[key]
                h_teams[key] = result[key]

            if key not in most_total_goals.keys():
                most_total_goals[key] = result[key]
            else:
                most_total_goals[key] += result[key]
            
            goal +=result[key]
            if goal >= highest_goal:
                highest_goal = goal       

        df[str([*result])] = goal

    
    df = sort(df)
    df = list(df.items())
    print('The match with the most goals was {}'.format(df[-1] ))
    print('The match with the fewest goals was {}'.format(df[0]))

    most_total_goals =  sort(most_total_goals)
    most_total_goals = list(most_total_goals.items())
    print('The team with the most total goals was',most_total_goals[-1])
    print('The team with the fewest total goals was', most_total_goals[0])

    l_teams = sort(l_teams)
    h_teams = sort(h_teams)
    l_teams = list(l_teams.items())
    h_teams = list(h_teams.items())
    print('The team with the most points was', h_teams[-1])
    print('The team with the fewest points was',l_teams[0])

def sort(args):
    # res = sorted(dictionary.items(),key=lambda x: x[1])
    if type(args) is dict: 
        keys = list(args.keys())
        values = list(args.values())
        result = {}
        for j in range(len(values)):
            for i in range(len(values)-1):            
                if values[i] > values[i+1]:
                    temp = values[i+1]
                    templ =  keys[i+1]
                    values[i+1] = values[i]
                    keys[i+1] = keys[i]
                    values[i] = temp 
                    keys[i] = templ       

        for key , value in zip(keys , values):
            result[key] = value
        return result
    elif type(args) is list:
        for j in range(len(args)):
            for i in range(len(args)-1):            
                if args[i] > args[i+1]:
                    temp = args[i+1]
                    args[i+1] = args[i]
                    args[i] = temp 
        return args
    else:
        print('Function takes list or dictionary only.')
                    



if __name__ == '__main__':
    # radio_ds('radio 4')
    # rgb_finder('red')
    # result_sch()
    football_res()


