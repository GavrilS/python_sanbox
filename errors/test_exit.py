def run_exit_test():
    print('Testing with exit()...')
    exit()

def run_error_code():
    res = 10 / 0
    print('Res: ', res)

if __name__=='__main__':
    try:
        run_exit_test()
        print('After exit test!')
        run_error_code()
        print('After error code!')
    except Exception as e:
        print('Exception: ', str(e))
