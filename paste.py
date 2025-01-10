def main():
    # Bekéri az elemek számát
    N = int(input("Adja meg az elemek számát: "))

    # Létrehozza a listát és feltölti értékekkel
    T = []
    for i in range(N):
        elem = int(input(f"Adja meg a(z) {i + 1}. elemet: "))
        T.append(elem)

    # Sorba rendezi a listát
    T.sort()

    # Kiírja a rendezett listát
    print("A rendezett tömb:", ", ".join(map(str, T)))

if __name__ == "__main__":
    main()

