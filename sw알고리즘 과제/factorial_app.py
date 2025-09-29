
"""
factorial_app.py (minimal)
- 반복(iterative) / 재귀(recursive) 팩토리얼
- 실행 시간 비교
- 메뉴 기반 인터랙션
- 예외 처리/입력 검증/출력 요약 같은 보조 기능 모두 제거
"""
import time
from typing import Callable, Tuple, List


def factorial_iter(n: int) -> int:
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

def factorial_rec(n: int) -> int:
    if n in (0, 1):
        return 1
    return n * factorial_rec(n - 1)

def run_with_time(func: 'Callable[[int], int]', n: int) -> 'Tuple[int, float]':
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    return result, end - start

def ask_n() -> int:
    print("\n정수 n을 입력하세요: ", end="")
    return int(input()) 

def do_iterative():
    n = ask_n()
    val, t = run_with_time(factorial_iter, n)
    print(f"\n[반복] {n}! = {val}")
    print(f"[반복] 경과 시간: {t:.6f} 초")

def do_recursive():
    n = ask_n()
    val, t = run_with_time(factorial_rec, n)
    print(f"\n[재귀] {n}! = {val}")
    print(f"[재귀] 경과 시간: {t:.6f} 초")

def do_compare():
    n = ask_n()
    v1, t1 = run_with_time(factorial_iter, n)
    v2, t2 = run_with_time(factorial_rec, n)
    print(f"\n[비교] n={n}")
    print(f"반복 결과: {v1}\n  시간: {t1:.6f} 초")
    print(f"재귀 결과: {v2}\n  시간: {t2:.6f} 초")
    print(f"동일 여부: {v1 == v2}")

def do_batch_tests():
    test_cases: List[int] = [0, 1, 5, 10, 20, 50, 100, 200]
    print("\n[일괄 테스트] 케이스:", test_cases)
    for n in test_cases:
        print("-" * 60)
        print(f"n = {n}")
        vi, ti = run_with_time(factorial_iter, n)
        print(f"  반복 (time={ti:.6f}s, digits={len(str(vi))})")
        vr, tr = run_with_time(factorial_rec, n)
        print(f"  재귀 (time={tr:.6f}s, digits={len(str(vr))})")
        print(f"  동일 여부: {vi == vr}")
    print("-" * 60)
    print("참고: 큰 n에서는 재귀 깊이 초과(RecursionError)가 발생할 수 있습니다.")

def print_menu():
    print("""
================= n! 계산기 (반복 vs 재귀) =================
1) 반복으로 계산 (factorial_iter)
2) 재귀로 계산 (factorial_rec)
3) 둘 다 실행하고 결과/시간 비교
4) 사전 정의 테스트 케이스 일괄 실행
5) 종료
==========================================================
번호를 선택하세요: """, end="")

def main():
    while True:
        print_menu()
        choice = input().strip()
        if choice == '1':
            do_iterative()
        elif choice == '2':
            do_recursive()
        elif choice == '3':
            do_compare()
        elif choice == '4':
            do_batch_tests()
        elif choice == '5':
            print("종료합니다.")
            break
        else:
            print("[오류] 1~5 중에서 선택하세요.")

if __name__ == "__main__":
    main()
