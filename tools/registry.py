class ToolRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, name, obj):
        if name in self._registry:
            raise ValueError(f"Object with name '{name}' is already registered.")
        if not callable(obj):
            raise TypeError(f"Object '{name}' must be callable.")
        self._registry[name] = obj

    def get(self, name):
        if name not in self._registry:
            raise KeyError(f"No object registered under the name '{name}'.")
        return self._registry[name]

    def unregister(self, name):
        if name in self._registry:
            del self._registry[name]
        else:
            raise KeyError(f"No object registered under the name '{name}'.")

    def list_registered(self):
        return list(self._registry.keys())