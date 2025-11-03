# Node 클래스
class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    def append(self, new):
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node


# LinkedList 클래스
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def append(self, book):
        # 중복된 책 번호 확인
        if self.find_by_id(book.book_id):
            print(f"[오류] 책 번호 {book.book_id}는 이미 존재합니다.")
            return False

        new_node = Node(book)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.link is not None:
                current = current.link
            current.link = new_node
        return True

    def find_by_id(self, book_id):
        current = self.head
        while current is not None:
            if current.data.book_id == book_id:
                return current.data
            current = current.link
        return None

    def find_by_title(self, title):
        current = self.head
        while current is not None:
            if current.data.title == title:
                return current.data
            current = current.link
        return None

    def find_pos_by_title(self, title):
        current = self.head
        pos = 0
        while current is not None:
            if current.data.title == title:
                return pos
            current = current.link
            pos += 1
        return -1

    def delete_by_title(self, title):
        if self.isEmpty():
            return False

        # 첫 번째 노드가 삭제 대상인 경우
        if self.head.data.title == title:
            self.head = self.head.link
            return True

        prev = self.head
        current = self.head.link
        while current is not None:
            if current.data.title == title:
                prev.link = current.link
                return True
            prev = current
            current = current.link
        return False

    def display(self):
        if self.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return

        current = self.head
        print("\n[전체 도서 목록]")
        print("-" * 50)
        while current is not None:
            print(current.data)
            current = current.link
        print("-" * 50)


# Book 클래스
class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"책번호: {self.book_id}, 제목: {self.title}, 저자: {self.author}, 출판연도: {self.year}"


# BookManagement 클래스
class BookManagement:
    def __init__(self):
        self.books = LinkedList()

    def add_book(self):
        try:
            book_id = int(input("책 번호: "))
            title = input("책 제목: ")
            author = input("저자: ")
            year = input("출판 연도: ")

            new_book = Book(book_id, title, author, year)
            if self.books.append(new_book):
                print(f"'{title}' 도서가 추가되었습니다.")
        except ValueError:
            print("[입력 오류] 책 번호는 숫자로 입력해주세요.")

    def remove_book(self):
        title = input("삭제할 책 제목: ")
        if self.books.delete_by_title(title):
            print(f"'{title}' 도서가 삭제되었습니다.")
        else:
            print(f"[오류] '{title}' 도서를 찾을 수 없습니다.")

    def search_book(self):
        title = input("조회할 책 제목: ")
        book = self.books.find_by_title(title)
        if book:
            print("\n[도서 조회 결과]")
            print(book)
        else:
            print(f"[오류] '{title}' 도서를 찾을 수 없습니다.")

    def display_books(self):
        self.books.display()

    def run(self):
        while True:
            print("\n=== 도서 관리 프로그램 ===")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 프로그램 종료")

            choice = input("메뉴 선택: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.remove_book()
            elif choice == '3':
                self.search_book()
            elif choice == '4':
                self.display_books()
            elif choice == '5':
                print("프로그램을 종료합니다.")
                break
            else:
                print("[오류] 올바른 메뉴 번호를 입력해주세요.")


# 실행부
if __name__ == "__main__":
    manager = BookManagement()
    manager.run()
