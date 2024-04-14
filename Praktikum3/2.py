class LimitedInstances:
    _instances = []
    limit = 5

    def __new__(cls, *args, **kwargs):
        if len(cls._instances) >= cls.limit:
            raise RuntimeError("Превышен лимит экземпляров")
        instance = super().__new__(cls)
        cls._instances.append(instance)
        return instance

    def __del__(self):
        self._instances.remove(self)

for _ in range(5):
    instance = LimitedInstances()
del instance

try:
    instance = LimitedInstances()
except RuntimeError as e:
    print(e)

