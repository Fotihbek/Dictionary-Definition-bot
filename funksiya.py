import requests
#from pprint import pprint

def get_definitions(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    natija = requests.get(url)
    res = natija.json()
    
   

    if 'title' in res:
        return False
    print(res[0])
    data = {}
    definitions = ''

    for n in range(len(res[0]['meanings'][0]['definitions'])):
        definitions += f"📌{n+1}. {res[0]['meanings'][0]['definitions'][n]['definition'].capitalize()} \n"

    data['definitions'] = definitions
    #data['definitions'] = '\n'.join(definitions)
    data['audio'] = f'http://audio.linguarobot.io/en/{word.lower()}-us.mp3'
    return data

""" if res[0]["phonetics"][0].get("audio"): 
        data['audio'] = res[0]["phonetics"][0]["audio"]"""

def tutuq(text):
    if '`' in text:
        word = text.replace('`', "’")
    elif "'" in text:
        word = text.replace("'", "’")
    elif "ʻ" in text:
        word = text.replace('ʻ', "’")

    return word


if __name__ == '__main__':
    print(get_definitions('word'))