import inspect

class DPifier:
    def __init__(self, f, lambda_mode=False):
        self.dp = {}

        def Y(f):
            def g(*args):
                if args in self.dp.keys():
                    return self.dp[args]

                else:
                    self.dp[args] = f(Y(f))(*args)
                    return self.dp[args]
            return g
        
        self.Y = Y

        if lambda_mode:
            self.f = f

        else:
            self.f = self.__parseFunction(f)

    def __call__(self, *args):
        return self.Y(self.f)(*args)

    def __parseFunction(self, f):
        functionName = f.__name__
        s = inspect.getsource(f)
        s = s.replace(functionName, 'h', 1)
        s = s.replace(functionName + '(', 'abc' + '(')

        def g(abc):
            exec(s, {'abc' : abc}, globals())
            return h

        return g
