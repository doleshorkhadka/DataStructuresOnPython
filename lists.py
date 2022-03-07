
'''
    1. football_res -- working with value of dictionaries in list
        [
        {'Austria': 0, 'Hungary': 2}
        ]
    2. sort -- sorting dictionary by value and sorting list
    3. rgb_finder -- working with 2D list && use of List_comprehension([expression for item in list])
         [
        ['red', 'F00'],
        ]
    4. bill_splitting -- working with list of lists (different data types in lists)
        [
        ['Tom', 'Calamari', 6.00]
        ]
'''

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

def bill_splitting(keyname):
    bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramasu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramasu', 4.90],
    ]
    keyname = keyname.capitalize()
    result = {}
    for item in bill_items:
        if item[0] not in result :
            result[item[0]] = item[-1]
        else:
            result[item[0]] +=item[-1]
    if keyname not in result:
        print('{} did not have dinner.'.format(keyname))
        print('The name of peoples having dinner are : \n',[*result])
        return None   

    print(' {} should pay {} '.format(keyname,result[keyname]))

if __name__ == '__main__':
    football_res()
    rgb_finder('yellow')
    bill_splitting('tim')