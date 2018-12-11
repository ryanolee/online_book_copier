from ghost import Ghost, Session
import time

wrapping_div = ''
next_button = ''
initial_url = ''
series_name = ''


chunks = 10

core_session = Ghost()
session = Session(core_session, display=False)

lower_bound = 0
upper_bound = chunks+lower_bound

def save_story(series_name, lower_bound, upper_bound, content):
    file_name = './chap/{0}_{1}-{2}.txt'.format(series_name, lower_bound, upper_bound)
    content = ''.join([i if ord(i) < 128 else ' ' for i in content])
    print(file_name)
    with open(file_name, 'wt', encoding='utf-8') as file:
        file.write(content)


searching = True
story_buffer = ''

next_url = initial_url

while searching:    
    try:
        session.open(next_url, timeout=300)
        lower_bound += 1
        session.wait_for_selector(next_button, 60)
    except:
        break

    story_data = session.evaluate('document.querySelector("{0}").innerText;'.format(wrapping_div))
    text = story_data[0]
    story_buffer += str(text)
    
    
    if lower_bound > upper_bound:
        save_story(series_name, lower_bound-chunks, upper_bound, story_buffer)
        story_buffer = ''
        lower_bound = upper_bound
        upper_bound += chunks


    
    link_data = session.evaluate('document.querySelector("{0}").href'.format(next_button))
    print(link_data[0])
    next_url = link_data[0]
    
    

save_story(series_name, lower_bound, upper_bound, story_buffer)