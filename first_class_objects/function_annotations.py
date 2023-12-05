def clip(text:str, max_len:'int > 0'=80) -> str:
    """Returns text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ',0,max_len)
        print('space_before: ', space_before)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ',max_len)
            print('space_after: ', space_after)
            if space_after >= 0:
                end = space_after
    
    if end is None:
        end = len(text)
    
    return text[:end].rstrip()


if __name__=='__main__':
    test = 'blaclavladlazlamlatla'
    res1 = clip(test)
    print('res1: ', res1)
    print('*'*40)
    test = 'blaclavla dlazlamlatla'
    res2 = clip(test, 4)
    print('res2: ', res2)
    print('*'*40)

    res3 = clip(test, -1)
    print('res3: ', res3)
    print('*'*40)
