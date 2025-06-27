def singleton(cls):
    instances = {}

    class SingletonWrapper(cls):
        def __new__(subcls, *args, **kwargs):
            if subcls not in instances:
                instances[subcls] = super(SingletonWrapper, subcls).__new__(subcls, *args, **kwargs)
            return instances[subcls]
    
    return SingletonWrapper

# def singleton(cls):
#     _instances = {}

#     def instance(*args, **kwargs):
#         if cls not in _instances:
#             _instances[cls] = cls(*args, **kwargs)
#         return _instances[cls]
    
#     return instance