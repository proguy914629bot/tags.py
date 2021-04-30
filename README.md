## How to install using pip:

Stable:
```sh
pip install tags.py
```

Developement:
```sh
pip install git+https://github.com/proguy914629bot/tags.py
```

## Simple guide on how to use:

```py
from tags import Tag

tag = Tag()

#Without aliases:
tag.add_tag(r"{user}", "user123")

#With aliases called "{users}" and "{usr}":
tag.add_tag(r"{user}", "user123", r"{users}", r"{usr}")

#Converting the string:
string = r"{user} is the same as {users} and {usr}!"
tag.convert(string) # "user123 is the same as user123 and user123!"

#Getting a tag by name:
tag.get_tag("Insert-Name-Here")

#Getting a tag by id:
tag.get_tag("Insert-ID-Here")

#Get a tag ID by name:

#Way 1:
tag.get_tag("Insert-Name-Here").id

#Way 2:
tag.get_id("Insert-Name-Here")

#All these ways are the same. get_tag.id returns tag.get_id.
```

## Contribution:
You can contribute by forking this repository, or cloning this repository. This is fully open-sourced in [Github](https://github.com/proguy914629bot/tags.py).

## License:
MIT