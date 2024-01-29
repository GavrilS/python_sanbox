import os

ENVIRONMENT_STATUS_UPDATE = 'The environment status was changed!'

def test():
    CMD_STATUS = os.getenv('CMD_STATUS', 'false')
    print('CMD_STATUS: ', CMD_STATUS)

    if CMD_STATUS != 'true':
        os.environ['CMD_STATUS'] = 'true'
        print(ENVIRONMENT_STATUS_UPDATE)
    else:
        os.environ['CMD_STATUS'] = 'not true'

    updated_status = os.getenv('CMD_STATUS', 'false')
    print('updated_status: ', updated_status)
    cmd_response = f"The status of the CMD is {updated_status}"


if __name__=='__main__':
    test()
