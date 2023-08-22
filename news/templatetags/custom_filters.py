from django import template
 
censor_words = ["водила", "тачке", "кент"]

register = template.Library() 

@register.filter(name='censor') 

def censor(censor_text): 

    for word in censor_words:
        censor_text = censor_text.lower().replace(word.lower(), '*censor*') 
    return censor_text 
