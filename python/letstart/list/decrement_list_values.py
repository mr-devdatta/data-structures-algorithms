
lst = [54, 43, 2, 1, 5]
print(lst)


for index, val in enumerate(lst):
    lst[index] -= 1

print(lst)


newLst = [ (i-1) for i in lst ]
print(newLst)


def requried_login(fun):
    def wrapper(user, *args, **kwargs):
        if not user.is_authenticated:
            raise PermissionError("Login required")
        return fun(user, *args, **kwargs)
    return wrapper


@requried_login
def view_profile(user):
    return "user"