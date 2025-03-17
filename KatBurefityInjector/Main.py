import os
import pathlib as sdd
from time import sleep
from Inject import Inject as inj
def Main():
    if(sdd.Path("KatBurefity.dll").is_file()):
        print("File is Founded!!! Injecting...")
        sleep(2)
        inj("Holoearth", "KatBurefity.dll")
        sleep(2)
        print("Injecting Done!!!")
        os._exit(120)
    else:
        sleep(2)
        print("Not Founded KatBurefity.dll(This DLL Cheeto is WIP!!!)")
        sleep(2)
        os._exit(321)
    
if __name__ == "__main__":
    Main()