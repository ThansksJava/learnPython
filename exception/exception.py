import logging
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ValueError as e:
    logging.exception('ValueError:', e)
except ZeroDivisionError as e:
    logging.exception('除0错误')
    raise e
else:
    print('no error!')
finally:
    print('finally...')
print('END')
