# P1 — Easy
# notes.txt file banao. User se 3 lines lo input se aur file me likho. Phir file padhke print karo.

with open("notes.txt","w") as f:
     for i in range(3):
          enter = input(f"enter {i+1}: ")
          f.write(enter + "\n")

with open("notes.txt","r") as f:
     content = f.read()

print(content)
