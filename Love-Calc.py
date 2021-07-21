
print("created by hussainatphysics@gmail.com(hussainsha syed)")
print("welcome to LOVE calculator,,, press enter it it stays")

"""
we are creating LOVE calculator....

"""




print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



name1=name1.lower()
name2=name2.lower()

T1,T2= name1.count('t'),name2.count('t')
R1,R2= name1.count('r'), name2.count('r')
U1,U2=name1.count('u'), name2.count('u')
E1,E2=name1.count('e'), name2.count('e')

a = str(T1+R1+U1+E1+T2+R2+U2+E2)

L1,L2= name1.count('l'),name2.count('l')
O1,O2= name1.count('o'), name2.count('o')
V1,V2=name1.count('v'), name2.count('v')
E11,E22=name1.count('e'), name2.count('e')

b = str(L1+O1+V1+E11+L2+O2+V2+E22)

Love_score= int(a+b)

if Love_score < 10 or Love_score >90:
  print("your score is {Love_score}, you go together for honey moon")

elif Love_score >=40 and Love_score <=50:
  print(f"your score is {Love_score}, you are alright together")
else:
  print(f"your score is {Love_score}")

# Just for console based exe
print()

print(input("press enter for bye dear"))