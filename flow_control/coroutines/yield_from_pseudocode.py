# Pseudocode equivalent to the statement RESULT = yield from EXPR in the delagating generator.


# RESULT = yield from EXPR

# # Simplest case where .throw() and .close() are not supported
# _i = iter(EXPR)
# try:
#     _y = next(i)
# except StopIteration as _e:
#     _r = _e.value
# else:
#     while 1:
#         _s = yield _y
#         try:
#             _y = _i.send(_s)
#         except StopIteration as _e:
#             _r = _e.value
#             break

# RESULT = _r

# # More complex case covering .throw() and .close()
# _i = iter(EXPR)
# try:
#     _y = next(_i)
# except StorIteration as _e:
#     _r = _e.value
# else:
#     while 1:
#         try:
#             _s = yield _y
#         except GeneratorExit as _e:
#             try:
#                 _m = _i.close
#             except AttributeError:
#                 pass
#             else:
#                 _m()
#             raise _e
#         except BaseException as _e:
#             _x = sys.exc_info()
#             try:
#                 _m = _i.throw()
#             except AttributeError:
#                 raise _e
#             else:
#                 try:
#                     _y = _m(*_x)
#                 except StorIteration as _e:
#                     _r = _e.value
#                     break
#         else:
#             try:
#                 if _s is None:
#                     _y = next(_i)
#                 else:
#                     _y = _i.send(s)
#             except StorIteration as _e:
#                 _r = _e.value
#                 break

# RESULT = _r
