#Question 1
Qnum = "1.A hypotenuse of right triangle with sides length %s and %s is %.3f"
M = 4
N = 5
anz = (M**2+N**2)**0.5
print Qnum %(M, N, anz)
#Q1B
Qnum = "1.B Area of rectangle %sx%s is %.3f and perimeter is %.3f"
M=4
N=5
anz=M*N
anz2=M*2+N*2
print Qnum %(M,N, anz, anz2)
#Question 1C
Qnum = "1.C Area of circle with radius %s is %.3f and perimeter is %.3f"
N = 5
anz1 = 3.14*N**2
anz2 = 2*3.14*5
print Qnum %(N,anz1, anz2)
#Question 2
#Q2A
Qnum = "2.A The result of slicing string %s is %s"
S = "Everythingisawesomeeverythingiscoolwhenyourepartofateam"
a = 0
b = 19
c = 35
d = 55
slice = S[a:b+1] + " " + S[c:d+1]
print Qnum %(S, slice)

#Q2B
Qnum = "2.B the reverse of string %s is %s"
s = "Everythingisawesomeeverythingiscoolwhenyourepartofateam"
reverseds=''.join(reversed(s))

print Qnum %(s, reverseds)


#Question 3
a = "CGCAGTTGTATTGCTTCCCACATTTATTAGACCACCTATTAAAAATGGATTTCTTCCCA"
b = "TTTCAAGCTGCCCACAAATCTCGCTCCTGATACGTTCTTCACTTCAAGCCGTAGCATCCC"
c = "AATATCAGAAGCGGCGCCGGACTTGTTTTCAAAATATCCACGTATCCCTTCTTTCTCTTTC"
d = "AATAGAAAACACCCATTGGTTCCGAAATAACGCATCTTATACTGTGGCTTATTGGCGTTAC"
e = "CC"
DNA = a + b + c + d + e

Qnum = "3.A The first location of the TAG codon is %s and the last location is %s"

first = DNA.find("TAG")
last = DNA.rfind("TAG")
print Qnum %(first, last)

Qnum = "3.B The result of fragmenting the DNA sequence by the stop codon TAG is fragments %s with legnth %s and fragment %s with length %s"
f1 = (DNA[27:181])
f2 = (DNA[182:])

print Qnum %(f1, len(f1), f2, len(f2))

Qnum = "3.C The length of the given sequence is %s bp"
print Qnum %(len(DNA))

Qnum = "3.D The percent of G in the DNA sequence is %.3f"

G = DNA.count("G")
l = len(DNA)
p = float(G)/l*100
print Qnum %(p)


Qnum = "3.E The number of A, C, T, and G is %s, %s, %s, %s"
A = DNA.count("A")
C = DNA.count("C")
T = DNA.count("T")
G = DNA.count("G")
print Qnum %(A, C, T, G)
