import requests
import json

def dict_Merge(dict1,dict2,result):
    ''' Merge two dictionaries with same keys and same data type 
    Eg:..
    dict1 = {
        'items': ['ram','shyam'],
        'total': 935,
         'totalPage': 'not known',
         'count': 10,
         'links': 
            {
            'self': '/api/search?page=1',
            'first': '/api/search?page=2',
            }
        }
    dict2 = {
        'items': ['sunil','Decon'],
        'total': 845,
        'totalPage': 'more than 100',
        'count': 10,
        'links': 
            {
            'self': '/api/search?page=1&title=%E0',
            'first': '/api/search?page=1&title=%E0',
            }
        }
        >>> data = dict_Merge(dict1,dict2,{})
    Output: 
    {
    'items': ['ram', 'shyam', 'sunil', 'Decon'], 
    'total': [935, 845], 
    'totalPage': ['not known', 'more than 100'], 
    'links': 
        {
            'self': ['/api/search?page=1', '/api/search?page=1&title=%E0'], 
            'first': ['/api/search?page=2', '/api/search?page=1&title=%E0'], 
        }
    }
    '''
    # dict2 sorted on the order of dict1 keys
    dict2_sorted = {i:dict2[i] for i in dict1.keys()} 
    for x,y,key in zip(dict1.values(),dict2_sorted.values(),dict1.keys()):
        tp_x = type(x)
        tp_y = type(y)
        try:
            if (tp_x is list) & (tp_y is list):
                result[key] = x+y
            elif ((tp_x is str) or (tp_x is int)) & ((tp_x is str) or (tp_x is int)):
                result[key] = [x,y]
            elif(tp_x is float) & (tp_y is float):
                result[key] = [x,y]
            elif (tp_x is dict) & (tp_y is dict):
                result[key] = {}
                result[key] = dict_Merge(x,y,result[key])
            else:
                raise Exception(f'{tp_x} can"t be merger with {tp_y} found on the key {key}')

        except Exception as e:
            print(e)
    return result

hello = {
    '1':{
        'items': ['ram','shyam'],
        'total': 935,
         'totalPage': 'not known',
         'count': 10,
         'links': {'self': '/api/search?page=1&title=%E0%A4%9A%E0%A5%81%E0%A4%A8%E0%A4%BE%E0%A4%B5',
          'first': '/api/search?page=1&title=%E0%A4%9A%E0%A5%81%E0%A4%A8%E0%A4%BE%E0%A4%B5',
          'last': '/api/search?page=94&title=%E0%A4%9A%E0%A5%81%E0%A4%A8%E0%A4%BE%E0%A4%B5',
          'next': '/api/search?page=2&title=%E0%A4%9A%E0%A5%81%E0%A4%A8%E0%A4%BE%E0%A4%B5'}
    },
    '2':{
        'items': ['sunil','Decon'],
        'total': 845,
         'totalPage': 'more than 100',
         'count': 10,
         'links': {'self': '/api/search?page=1&title=%E0',
          'first': '/api/search?page=1&title=%E0',
          'last': '/api/search?page=94&title=%E0',
          'next': '/api/search?page=2&title=%E0'}
    }
    
}
a = hello['1']
b = hello['2']
rus = {}
result = dict_Merge(a,b,rus)
print(result)