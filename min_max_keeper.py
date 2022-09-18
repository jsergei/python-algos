from sortedcontainers import SortedList

class MinMaxKeeper:
    def __init__(self):
        self._key_to_value = {}
        self._sorted_values = SortedList()
        self._value_to_key = {}

    def inc_key(self, key):
        new_value = 1
        if key in self._key_to_value:
            new_value = self._key_to_value[key] + 1
            self._unregisted_old_value(key)
        self._register_new_value(key, new_value)

    def dec_key(self, key):
        # assume key always exists and its value is greater than 1
        new_value = self._key_to_value[key] - 1
        self._unregisted_old_value(key)
        self._register_new_value(key, new_value)

    def has_key(self, key):
        return key in self._key_to_value

    def get_value(self, key):
        return self._key_to_value[key]

    def calc_max_variance(self):
        return self._sorted_values[-1] - self._sorted_values[0]

    def _unregisted_old_value(self, key):
        value = self._key_to_value[key]
        self._value_to_key[value].remove(key)
        if not self._value_to_key[value]:
            del self._value_to_key[value]
            self._sorted_values.remove(value)

    def _register_new_value(self, key, new_value):
        self._key_to_value[key] = new_value
        if new_value not in self._value_to_key:
            self._value_to_key[new_value] = set()
        self._value_to_key[new_value].add(key)
        if new_value not in self._sorted_values:
            self._sorted_values.add(new_value)
