import typing

class TagsDict:
    def __init__(self, name, aliases, result, _id, default = None):
        self.aliases = aliases
        self.result = result
        self.default = default
        self.name = name
        self.id = _id

    def __repr__(self):
        return f"<TagsDict name={self.name} aliases={self.aliases} default={self.default} result={self.result} id={self.id}>"

    def __str__(self): return self.name

class Tags:
    def __init__(self, *args, **kwargs):
        """
        Tags class.
        """
        self.args = args
        self.kwargs = kwargs
        self._tags = {}
        self._tags_id = {}
        self._aliases = {}
        self._default = {}
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<Tags args={self.args} kwargs={self.kwargs}>"

    def __len__(self): return len(self._tags)

    def add_tag(self, name, result, *aliases) -> None:
        self._tags[name] = result
        self._tags_id[str(id(name))] = name

        for alias in aliases:
            self._tags[alias] = result
            self._tags_id[str(id(alias))] = name
            if name not in self._aliases:
                self.aliases[name] = []

            self._aliases[name] += alias

    def set_default(self, name, key, *aliases) -> None:
        if name not in self._tags:
            self._tags[name] = key
        
        #if name not in self._default:
            #self._default[name] = ""

        if name not in self._default:
            self._default[name] = key
            self._tags_id[str(id(name))] = name

        for alias in aliases:
            if alias not in self._tags:
                self._tags[alias] = key
                self._tags_id[str(id(alias))] = name
            if name not in self._aliases:
                self._aliases[name] = []

            self._aliases[name] += alias

    def convert(self, string) -> str:
        string = str(string)

        s = ''
        for k, v in self._tags:
            s = string.replace(k, v)

        return s

    def get_id(self, name) -> typing.Union[int, None]:
        for k, v in self._tags_id:
            if v == str(name):
                return int(k)

        return None

    def get_tag(self, option) -> TagsDict:
        name = option
        try:
            name = self._tags_id[str(name)]
        except:
            pass

        if name not in self._tags:
            raise KeyError(name)

        return TagsDict(name, self._aliases.get(name, []), self._tags[name], self.get_id(name), self._default.get(name, None))