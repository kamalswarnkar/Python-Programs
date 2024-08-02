def Tower_Of_Hanoi(n, s, a, d):
    if(n <= 0):
        return
    if(n == 1):
        move_disk(s, d)
        return 
    Tower_Of_Hanoi(n - 1, s, d, a)
    move_disk(s, d)
    Tower_Of_Hanoi(n - 1, a, s, d)

def move_disk(source, destination):
    disk = source.pop()
    destination.append(disk)  
    print(f"Move disk {disk} from {source} to {destination}")
        
no_of_disks = int(input("No. of Disks: "))
source_rod = list(range(no_of_disks, 0, -1))
auxiliary_rod = []
destination_rod = []

Tower_Of_Hanoi(no_of_disks, source_rod, auxiliary_rod, destination_rod)
total_steps = (2 ** (no_of_disks)) - 1
print(total_steps)