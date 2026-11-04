
import re
import random
from datetime import datetime

def respond(user_input):
    text = user_input.lower().strip()

    if re.search(r'\bmy name is (\w+)', text):
        name = re.search(r'\bmy name is (\w+)', text).group(1)
        return random.choice([
            f'Nice to meet you, {name.capitalize()}!',
            f'Hello {name.capitalize()}, how can I help you?'
        ])

    elif re.search(r'\bhow are you\b', text):
        return 'I am doing great, thank you! How about you?'

    elif re.search(r'\b(hi|hello|hey)\b', text):
        return 'Hello! How can I help you today?'

    elif re.search(r'\b(course|courses|subject|subjects)\b', text):
        return 'We offer Computer, IT, Mechanical and Civil engineering courses.'

    elif re.search(r'\b(fee|fees)\b', text):
        return 'Fee details are available at the college office or on the website.'

    elif re.search(r'\b(timing|timings|hours)\b', text):
        return 'The college is open from 9:00 AM to 5:00 PM, Monday to Saturday.'

    elif re.search(r'\btime\b', text):
        return 'The current time is ' + datetime.now().strftime('%I:%M %p')

    elif re.search(r'\b(thanks|thank you)\b', text):
        return 'You are welcome!'

    elif re.search(r'\b(bye|goodbye|exit|quit)\b', text):
        return 'Goodbye! Have a nice day.'

    else:
        return random.choice([
            'Sorry, I did not understand that. Could you rephrase?',
            'I am still learning. Try asking about courses, fees or timings.'
        ])


def chat():
    print('Bot: Hi! I am CollegeBot. Type bye to exit.')

    while True:
        user = input('You: ')
        reply = respond(user)
        print('Bot:', reply)

        if re.search(r'\b(bye|goodbye|exit|quit)\b', user.lower()):
            break

if __name__ == '__main__':
    chat()
