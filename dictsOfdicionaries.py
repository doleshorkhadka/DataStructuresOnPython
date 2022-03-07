'''
Working with dictionary of dictionaries
{
    'A1': {'ram' : 'Itahari'},
    'A2' : {'hari' : 'Dharan' }
}
'''

def conference_schedule(place_arg ,time_arg):
    schedule = {
        'Main Hall': {
            '10:00': 'Django REST framework',
            '11:00': 'Lessons learned from PHP',
            '12:00': "Tech interviews that don't suck",
            '14:00': 'Taking control of your Bluetooth devices',
            '15:00': "Fast Python? Don't Bother!",
            '16:00': 'Test-Driven Data Analysis',
            },
        'Seminar Room': {
            '10:00': 'Python in my Science Classroom',
            '11:00': 'My journey from wxPython tp PyQt',
            '12:00': 'Easy solutions to hard problems',
            '14:00': 'Taking control of your Bluetooth devices',
            '15:00': "Euler's Key to Cryptography",
            '16:00': 'Build your Microservices with ZeroMQ',
            },
        'Assembly Hall': {
            '10:00': 'Distributed systems from scratch',
            '11:00': 'Python in Medicine: ventilator data',
            '12:00': 'Neurodiversity in Technology',
            '14:00': 'Chat bots: What is AI?',
            '15:00': 'Pygame Zero',
            '16:00': 'The state of PyPy',
            },
        }
    time_arg = float(time_arg.replace(':','.'))
    for key,value in schedule.items():
        time_ls = [*value]
        time_ls = [float(tm.replace(':','.')) for tm in time_ls ]
        detail_ls = list(value.values())
        for i in range(len(time_ls)-1):
            if time_arg >= time_ls[i] and key == place_arg and time_arg < time_ls[i+1]:
                print('Your meeting at {} is on {} about {}'.format(
                    str(time_arg).replace('.',':'),
                    key,
                    detail_ls[i]
                    ))
                return None
            elif time_arg == time_ls[i+1] and key == place_arg:
                print('Your meeting at {} is on {} about {}'.format(
                    str(time_arg).replace('.',':'),
                    key,
                    detail_ls[i+1]
                    ))
                return None
            else:
                continue
    print('No schedule found !!!')

if __name__ =='__main__':
    conference_schedule('Seminar Room','10:60')
    conference_schedule('Assembly Hall','15:00')
    conference_schedule('Main Hall','14:20')
    conference_schedule('Main Hall','16:20')