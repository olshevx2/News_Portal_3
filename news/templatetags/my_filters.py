from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise ValueError("Фильтр censor применяется только к строкам!")
    
    bad_words = ['редиска', 'дурак', 'балбес']
    words = value.split()
    censored_words = []
    
    for word in words:
        clean_word = word.strip('.,!?;:"()[]{}').lower()
        if clean_word in bad_words:
            new_word = word[0] + '*' * (len(word) - 1)
            censored_words.append(new_word)
        else:
            censored_words.append(word)
            
    return ' '.join(censored_words)