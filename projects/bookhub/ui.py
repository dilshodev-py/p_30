from typing import Optional

from projects.bookhub.backend import User, Book


class UI:
    session_user : Optional['User'] = None
    session_book : Optional['Book'] = None
    def main(self):
        menu = """
            1) Ro'yhatdan o'tish
            2) Hisobga kirish
            3) To'xtatish
        """
        key = input(menu)

        match key:
            case "1":
                self.register()
            case "2":
                self.login()
            case "3":
                return

    def register(self):
        pass

    def login(self):
        pass

    def account(self):
        menu = """
            1) Kitoblar koleksiyasi
            2) Mening kitoblarim 
            3) savat
            4) chiqish
            >>>"""
        key = input(menu)

    def discover_book(self):
        menu = """
            1) Qidirish 🔎
            2) Janr bo'yicha qidirish
            3) Hamma kitoblar
            4) back
            >>>"""

    def search(self):
        pass

    def books_by_category(self):
        pass

    def all_books(self):
        pass


    def book_detail(self):
        menu = """
            1) Kitob haqida
            2) online o'qish
            3) savatga qo'shish
            
            0) back
            >>>"""






