from KhoiKienThuc import KhoiKienThuc
from MonHoc import MonHoc

class ChuongTrinhDaoTao:
    def __init__(self):
        self.__dsKhoiKienThuc: list[KhoiKienThuc] = []

    def init(self):
        # Init KhoiKienThuc
        lyLuanChinhTri = KhoiKienThuc("Lý luận chính trị")
        khoaHocTuNhien = KhoiKienThuc("Toán - Tin - Khoa học tự nhiên")

        # Init MonHoc of LyLuanChinhTri
        ss003 = MonHoc("SS003", "Tư tưởng Hồ Chí Minh")
        ss007 = MonHoc("SS007", "Triết học Mác - Lênin")
        ss008 = MonHoc("SS008", "Kinh tế chính trị Mác - Lênin")
        ss009 = MonHoc("SS009", "Chủ nghĩa xã hội khoa học")
        ss010 = MonHoc("SS010", "Lịch sử Đảng Cộng sản Việt Nam")

        lyLuanChinhTri.addMonHocs([ss003, ss007, ss008, ss009, ss010])

        # Init MonHoc of KhoaHocTuNhien
        ma006 = MonHoc("MA006", "Giải tích")
        ma003 = MonHoc("MA003", "Đại số tuyến tính")
        ma004 = MonHoc("MA004", "Cấu trúc rời rạc")
        ma005 = MonHoc("MA005", "Xác suất thống kê")
        it001 = MonHoc("IT001", "Nhập môn Lập trình")

        khoaHocTuNhien.addMonHocs([ma006, ma003, ma004, ma005, it001])

        self.__dsKhoiKienThuc.extend([lyLuanChinhTri, khoaHocTuNhien])