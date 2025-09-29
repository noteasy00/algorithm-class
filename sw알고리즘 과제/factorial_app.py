
import time
from typing import Callable, Tuple, List

# ========== 핵심 계산 ==========
def factorial_iter(n: int) -> int:
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

def factorial_rec(n: int) -> int:
    if n in (0, 1):
        return 1
    return n * factorial_rec(n - 1)

def run_with_time(func: "Callable[[int], int]", n: int) -> "Tuple[int, float]":
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    return result, end - start

# ========== 입력 유틸 ==========
def parse_nonneg_int_or_none(s: str):
    """정수(0 이상)면 int, 아니면 None"""
    s = s.strip()
    if not s or (s[0] in "+-" and not s[1:].isdigit()) or (s[0].isdigit() is False and s[0] not in "+-"):
        return None
    try:
        val = int(s)
    except Exception:
        return None
    if val < 0:
        return None
    return val

def ask_n_or_back() -> int | None:
    print("\nn 값(정수, 0 이상)을 입력하세요: ", end="")
    s = input()
    n = parse_nonneg_int_or_none(s)
    if n is None:
        print("정수(0 이상)의 숫자만 입력하세요.")
        return None
    return n

# ========== 출력 포맷 ==========
TITLE = "==================  Factorial Tester  =================="
LINE  = "----------------------------------------------------------"

def print_menu():
    print(TITLE)
    print("1) 반복법으로 n! 계산")
    print("2) 재귀로 n! 계산")
    print("3) 두 방식 모두 계산 후 결과/시간 비교")
    print("4) 준비된 테스트 데이터 일괄 실행")
    print("q) 종료")
    print(LINE)
    print("선택: ", end="")

# ========== 동작 ==========
def do_iterative():
    n = ask_n_or_back()
    if n is None:
        return
    val, t = run_with_time(factorial_iter, n)
    print(f"[반복] {n}! = {val}")
    print(f"[반복] 시간: {t:.6f} s")

def do_recursive():
    n = ask_n_or_back()
    if n is None:
        return
    val, t = run_with_time(factorial_rec, n)
    print(f"[재귀] {n}! = {val}")
    print(f"[재귀] 시간: {t:.6f} s")

def do_compare():
    n = ask_n_or_back()
    if n is None:
        return
    v1, t1 = run_with_time(factorial_iter, n)
    v2, t2 = run_with_time(factorial_rec, n)
    print(f"[반복] {n}! = {v1}")
    print(f"[재귀] {n}! = {v2}")
    print(f"결과 일치 여부: {'일치' if v1 == v2 else '불일치'}")
    print(f"[반복] 시간: {t1:.6f} s    [재귀] 시간: {t2:.6f} s")

def do_batch():
    tests: List[int] = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100, 200, 500]
    print("\n[테스트 데이터 실행]")
    for n in tests:
        vi, ti = run_with_time(factorial_iter, n)
        vr, tr = run_with_time(factorial_rec, n)
        same = (vi == vr)
        print(f"{n:>3} ) same={same} | iter={ti:.6f}s,  rec={tr:.6f}s")
        print(vi)
    print("(안내) 큰 n에서는 재귀 깊이 한계로 에러가 발생할 수 있습니다.")

def main():
    print("팩토리얼 계산기 (반복/재귀) - 정수 n>=0 를 입력하세요.")
    while True:
        print_menu()
        choice = input().strip().lower()
        if choice == '1':
            do_iterative()
        elif choice == '2':
            do_recursive()
        elif choice == '3':
            do_compare()
        elif choice == '4':
            do_batch()
        elif choice == 'q':
            print("종료합니다.")
            break
        else:
            print("메뉴에서 선택하세요.")

if __name__ == "__main__":
    main()