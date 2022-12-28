# coding: utf-8

_dict = {
    "data": [
        {
            "data":[
                "test1",
                "test2",
                "test3"
            ]
        }
    ]
}


for i in _dict["data"]:
    for l in i["data"]:
        del i["data"][i["data"].index(l)]


print(_dict)