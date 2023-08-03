def dict_return(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[value] = key
    return result

print(dict_return(a=11,b='sdf',c=109,d='combo',name='Alexander'))