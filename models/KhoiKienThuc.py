from MonHoc import MonHoc

class KhoiKienThuc:
    def __init__(self, name):
        self.__name = name
        self.__dsMonHoc: list[MonHoc] = []

    def addMonHoc(self, monHoc):
        self.__dsMonHoc.append(monHoc)
    
    def addMonHocs(self, monHocs):
        for monHoc in monHocs:
            self.__dsMonHoc.append(monHoc)

    def getDsMonHoc(self):
        return self.__dsMonHoc