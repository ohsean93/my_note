def make_url(base_url,key,**kwargs):
    url = f'{base_url}?key={key}'
    for key,value in kwargs.items():
        url = f'{url}&{key}={value}'
    return url