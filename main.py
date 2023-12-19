from os import path as ospath
from os import system
from time import sleep
import hashlib


# general vars
hashToUse = ""
hashValue = ""
pathToWordlist = ""

print("Welcome to the hashcrackertron 3000")

def identifyHash(hash: str) -> str:

  match len(hash):
    case 32:
      return "md5"
    case 128:
      return "sha3-512"
    case 64:
      return "sha256"

hashIdentified = False
while not hashIdentified:
  hash = input("Input hash: ")
  print(len(hash))
  match identifyHash(hash):
    case "md5":
      hashToUse = "md5"
      hashIdentified = True
      hashValue = hash
    case "sha256":
      hashToUse = "sha256"
      hashIdentified = True
      hashValue = hash
    case "sha3-512":
      hashToUse = "sha3-512"
      hashIdentified = True
      hashValue = hash
  
  if not hashIdentified:
    print(f"The hash: {hash} is not supported or is invalid.\n Supported types: MD5, SHA3-512, SHA256")
    sleep(5)
    system("cls")

print(f"Hash identified as: {hashToUse}")
sleep(5)
system("cls")

pathIdentified = False
while not pathIdentified:
  sleep(5)
  system("cls")
  path = input("Input path to a wordlist in a .txt format: ")

  if not ospath.exists(path):
    print(f"The path \"{path}\" does not exist")
    continue

  if not ospath.isfile(path):
    print(f"The path \"{path}\" does not lead to a file.")
    continue

  if not path.lower().endswith(".txt"):
    print(f"The file at: \"{path}\"\n is not a text file. Please provide a .txt file")
    continue
  
  pathIdentified = True
  pathToWordlist = path

print(f"Identified hash type: {hashToUse}")
print(f"Identified wordlist path as: {pathToWordlist}")

def hash(string, hashtype):
  match hashtype:
    case "md5":
      h = hashlib.md5()
      h.update(string.encode("utf-8"))
      return h.hexdigest()
    case "sha256":
      h = hashlib.sha256()
      h.update(string.encode("utf-8"))
      return h.hexdigest()      
    case "sha3-512":
      h = hashlib.sha3_512()
      h.update(string.encode("utf-8"))
      return h.hexdigest()      

crackedHash = None
with open(pathToWordlist) as file:
  fileLines = [ line.replace("\n", "") for line in file.readlines()]
  print(fileLines)
  
  for line in fileLines:
    print(f"Textfile Line: {line}")
    print(f"Hashed Line: {hash(line, hashToUse)}")
    if hashValue == hash(line, hashToUse):
      crackedHash = line
  file.close()

if crackedHash == None:
  print("No matches found in wordlist.")
else:
  print(f"Found decoded hash: {crackedHash}")