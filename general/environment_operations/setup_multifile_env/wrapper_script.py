import os
from subprocess import Popen, PIPE

ENVIRONMENT_STATUS_UPDATE = 'The environment status was changed!'

def main():
    # os.environ['CMD_STATUS'] = 'true'
    commands = [
        "python3 test.py"
    ]

    procs = [ Popen(i, stdout=PIPE, stderr=PIPE, shell=True) for i in commands ]
    for p in procs:
        result, error = p.communicate()
        print('p.stdout: ', result)
        print('p.stderr: ', error)
        str_result = result.decode('utf-8')
        if ENVIRONMENT_STATUS_UPDATE in str_result:
            print('Status was update, found: ', ENVIRONMENT_STATUS_UPDATE)
        else:
            print('Status was NOT updated!')
        print('*'*40)
        results = str_result.split('\n')
        print('results: ', results)
        print('*'*40)


    command_status = os.getenv('CMD_STATUS', 'false')
    print('command_status from environment in wrapper: ', command_status)

    if command_status == 'true':
        print('The status is true, we can see environments set from other scripts!!!')
    else:
        print('The status is not true, we cannot see the environment set from the other script!!!')



if __name__=='__main__':
    main()
