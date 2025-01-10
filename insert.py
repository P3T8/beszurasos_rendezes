import random

def main():
    # Kérjük be a tömb méretét
    N = int(input("Add meg a tömb méretét (N): "))

    # Készítsünk egy tömböt és töltsük fel véletlen számokkal
    T = [random.randint(1, 100) for _ in range(N)]

    print("Eredeti tömb:", T)

    # Rendezzük sorba a tömböt
    T.sort()

    # Írjuk ki a rendezett tömböt
    print("Rendezett tömb:", T)

if __name__ == "__main__":
    main()
