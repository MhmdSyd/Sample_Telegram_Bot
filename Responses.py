from datetime import datetime

def sample_responses(text_input):
    
    user_massege = str(text_input).lower()
    
    if user_massege in ('hello', 'hey', 'hello!', 'hey!'):
        return "Hey! How's it going?"
    
    if user_massege in ('who are you', 'who are you!'):
        return "I am a Sample Bot :)"
    
    if user_massege in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime('%d/%m/%Y, %H:%M:%S')
        return str(date_time)
    
    return "I don't understand you."