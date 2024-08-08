class Kitap:
    def __init__(self, baslik, yazar, yil, isbn):
        self.baslik = baslik
        self.yazar = yazar
        self.yil = yil
        self.isbn = isbn

    def kitap_bilgisi(self):
        return f"'{self.baslik}' by {self.yazar} ({self.yil}) - ISBN: {self.isbn}"