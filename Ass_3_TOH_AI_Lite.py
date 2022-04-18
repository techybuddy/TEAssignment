class Rod:                                                          # Class to represent rods
    def __init__(self, name, rings = []) -> None:
        self.name = name                                            # Name of tower
        self.rings = rings                                          # List of rings
    
    def __repr__(self):
        return f"'{self.name}' Rod -> Rings : {self.rings}"



def transfer(source, dest) -> None:

    if not len(source.rings):                                       # In case source rod is empty
        source.rings.append(dest.rings.pop())
        print(f"Disk {source.rings[-1]} is moved from '{dest.name}' to '{source.name}'.")

    elif not len(dest.rings):                                       # In case dest rod is empty
        dest.rings.append(source.rings.pop())
        print(f"Disk {dest.rings[-1]} is moved from '{source.name}' to '{dest.name}'.")
    
    else:
        if source.rings[-1] < dest.rings[-1]:                       # In case the top ring of the 'source' rod is smaller than that of 'dest' rod
            dest.rings.append(source.rings.pop())                   # Then remove ring from source rod and insert it into 'dest' rod
            print(f"Disk {dest.rings[-1]} is moved from '{source.name}' to '{dest.name}'.")

        else:                                                       # In case the top ring of the 'dest' rod is smaller than that of 'source' rod
            source.rings.append(dest.rings.pop())                   # Then remove ring from 'dest' rod and insert it into 'source' rod
            print(f"Disk {source.rings[-1]} is moved from '{dest.name}' to '{source.name}'.")




#### Main Method
if __name__== "__main__":
    n = int(input("Enter number of rings: "))                       # Number of Rings
    print(f"\t\t Number of Rods = {n} \t\t Number of Iterations = {2**n-1}\n{'.'*100}\n")
    source, auxiliary, dest = Rod('Source', list(range(n, 0, -1))), Rod('Auxiliary', []), Rod('Destination', [])   # Creating Towers(Rods)
    
    args = {
        0: {
            0: (auxiliary, dest,),
            1: (source, auxiliary,),
            2: (source, dest,),
        },
        1: {
            0: (dest, auxiliary,),
            1: (source, dest,),
            2: (source, auxiliary,),
        }
    }

    for i in range(1, 2**n):                                        # Iterate for total 2^n operations
        print(f"{i:5}. ", end='')
        transfer(*args[n%2][i%3])