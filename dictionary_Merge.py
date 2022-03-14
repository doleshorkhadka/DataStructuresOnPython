import string
import requests
import json

class Annapurna_Scraper:
    def __init__(self,page_no,search_keyword = 'चुनाव',save_to_file=True):
        self.search_keyword = search_keyword
        self.page_no = page_no
        self.save_to_file = save_to_file
        self.responses = []
        self.data = {}
        
    def fetch_data(self,search_key,page):
        url = f"https://bg.annapurnapost.com/api/search?title={search_key}&page={page}"
        header = {
            'authority': 'bg.annapurnapost.com',
            'content-type': 'application/json',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'cache-control': 'no-cache',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',

        }
        return requests.get(url,headers=header)
    
    def Scrape(self):
        try:
            for page in range(self.page_no):
                # self.responses.append(self.fetch_data(self.search_keyword,page+1))
                response = self.fetch_data(self.search_keyword,page+1)
                if response.status_code != 200 :
                    raise Exception('Connection error !!!')
                else:
                    data = response.json()['data']
                    self.data[page+1] = data 

            if self.save_to_file == True:
                with open('scrape.json','a') as f:
                    json.dump(data,f)
            else:    
                return self.data
        except Exception as e:
            print(e)

result = {}
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