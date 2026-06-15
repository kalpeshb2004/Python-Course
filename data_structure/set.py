# P1 — common friends
# do log hai — unke friends ke 2 sets banao
# common friends print karo
# only in A, only in B bhi print karo

# frnd1 = {"kalpesh","jayesh","ram","sham"}
# frnd2 = {"jayesh","sham","rahul","priyansh","bapi"}

# comman = frnd1.intersection(frnd2)
# print(comman)

# diffrence1 = frnd1.difference(frnd2)
# print(diffrence1)

# diffrence2 = frnd2.difference(frnd1)
# print(diffrence2)

# P2 — unique words
# sentence lo → "hi bye hi hello bye hi"
# set use karke unique words nikalo
# total unique words count bhi print karo

# s = "hi bye hi hello bye hi"
# split1 = s.split()
# print(split1)
# unique = list(set(split1)) # sirf unique words deta he 
# print(unique)
# print(len(unique))

# P3 — voting system
# voters ki list lo — kuch ne 2 baar vote kiya!
# voters = ["ram","sam","ram","tom","sam","ram"]
# valid voters nikalo (unique)
#sbse jada voting kisne kiya
# kitne ne 2+ baar vote kiya wo bhi nikalo

# voters = ["ram","sam","ram","tom","sam","ram"]
# unique_voters = list(set(voters))
# print(unique_voters)

# jada_voting = max(set(voters) , key=voters.count)
# print(jada_voting)

# checked = []
# for i in range(len(voters)):
#     if voters.count(voters[i]) > 2 and voters[i] not in checked:
#         checked.append(voters[i])
# print(checked)



