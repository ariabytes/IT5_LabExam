# Tower of Hanoi WOW!

def hanoi(n, a, b, c):
    if n == 1:
        print(f"Disk {n} moved from stack {a} to {c}")
        return
    hanoi (n-1, a, c, b)
    print(f"Disk {n} moved from stack {a} to {c}")
    hanoi (n-1, b, a, c)
    print(f"Disk {n} moved from stack {b} to {c}")


# Main
while True:
    try:
        disk = int(input("\nHow many disks does your tower have? "))
        if disk <= 0:
            print("A tower cannot have 0 disks! Try again!")
            continue
        hanoi(disk, "A", "B", "C")
        print(f"\nTotal moves: {disk**2}")
    except ValueError:
        print("Positive only!")




