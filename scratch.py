

# def route(func):
#     def wrapper():
#         print('An HTTP request was made')
#         request = {'data': {'username': 'brians', 'password': 'abc123'}}
#         res = func(request)
#         print('This is the response:', res)
#     return wrapper


# @route
# def signup(new_user_data):
#     print('This is our function!')
#     new_user = {
#         'id': 1,
#         'username': new_user_data['data']['username'],
#         'password': new_user_data['data']['password']
#     }
#     return new_user


# signup()


# from example import my_example_func