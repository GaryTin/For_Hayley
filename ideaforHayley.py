class Web():
    def __init__(self,name,infoCollected):
        self.name = name
        self.infoCollected = infoCollected


class Webdata():
    def __init__(self):
        self.web = {}

    def addWeb(self,name,infoCollected):
        self.web[name] = Web(name,infoCollected)

    def getWebInfoCollected(self,name):
        return self.web[name].infoCollected

    def toBool(self,name,checkList):
        list = []
        for item in checkList:
            list.append( item in self.getWebInfoCollected(name))
        return list



def main():
    webdata = Webdata()
    webdata.addWeb("HKTVMall",["Name", "ID", "Email"])
    webdata.addWeb("TaoBao", ["Name", "ID", "Email", "Location"])
    print(webdata.getWebInfoCollected("TaoBao"))
    print(webdata.toBool("HKTVMall",["Name", "ID", "Email", "Location"]))


if __name__ == "__main__":
    main()