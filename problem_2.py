def towerofhanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    towerofhanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    towerofhanoi(n - 1, auxiliary, destination, source)

n = int(input("Enter number of disks: "))
towerofhanoi(n, 'A', 'C', 'B')