#####
import json
import os.path
from pathlib import Path



def isPodmanLoggedIn():


    auth_file = Path ("/home/mike/auth.json")


    try:

     my_abs_path = auth_file.resolve(strict=True)

    except (FileNotFoundError,NameError) as e:
        print( "isPodmanLoggedIn:File Not Found ....... ")
        return False

    else:

        print ("isPodmanLoggedIn:auth.json: File Found")

        with open(my_abs_path) as f:
            data = json.load(f)

        try:


            if (data["auths"]["docker-dms-mms-mmcm2-usvms-local.repo.ukdn.thalesuk"]["auth"]):
                print ("isPodmanLoggedIn:Success: Logged In ....")
##                print (data["auths"]["docker-dms-mms-mmcm2-usvms-local.repo.ukdn.thalesuk"]["auth"])
                return True


        except KeyError:
            print ("isPodmanLoggedIn:KeyError ..................")
            return False


def main():
    
    print ("The main procedure .....")

    if not isPodmanLoggedIn():

       print("main:  You must login to Podman ....")

       quit()

    else:

        print ("main: You are already logged In ....")




if __name__ == "__main__":

    main()
