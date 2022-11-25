class TreeStore:
    global res
    res = []

    def __init__(self, items):
        self.items = items

    def getAll(self):
        return items

    def getItem(self, id: int):
        for i in items:
            if i["id"] == id:
                return i

    def getChildren(self, id: int):
        result = []
        for i in items:
            if i["parent"] == id:
                result.append(i)
        return result

    def getAllParents(self, id: int):
        for i in items:
            if i["id"] == items[id - 1]["parent"]:
                res.append(i)
                ts.getAllParents(i["id"])
        return res


ts = TreeStore(items)
print(ts.getAllParents(7))
