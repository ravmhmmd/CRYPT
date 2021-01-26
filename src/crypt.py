# Muhammad Rayhan Ravianda
# 13519201
# K-04

# Tugas Kecil 1 IF2211 Strategi Algoritma
# Penyelesaian Cryptarithmetic dengan Algoritma Brute Force

# File : crypt.py


# ---------- FUNGSI TAMBAHAN ---------- #

# Module yang digunakan
import re
import time

# Fungsi 'maks' untuk mencari jumlah digit dari operand yang akan dijadikan batas maksimal untuk digit hasil
def maks(A) :
    maksA = len(A[0])
    for i in range (1, len(A)) :
        if maksA <= len(A[i]) :
            maksA = len(A[i])
    return maksA

# Fungsi 'printSoal' untuk mencetak Persoalan yang ingin dicari solusinya
def printSoal(A) :
    empty = " "
    diff = 0
    for i in range(len(A)) :
        diff = len(hasilList) - len(A[i])
        space = (empty * diff) + A[i]
        print(space)
    div = (len(hasilList) * "-") + "+"
    print(div)
    print(hasilList)

# Fungsi 'printSolusi' untuk mencetak Solusi yang sudah ditemukan
def printSolusi(A) :
    empty = " "
    diff = 0
    for i in range(len(A)-1) :
        diff = len(hasilList) - len(A[i])
        space = (empty * diff) + A[i]
        print(space)
    div = (len(hasilList) * "-") + "+"
    print(div)
    print(A[len(A)-1])

# Fungsi 'solveCrypt' untuk menyelesaikan permasalahan cryptarithmetic
def solveCrypt(letter, number, isVisit, word) :
    
    # Mengambil variabel boolean 'isSolved'
    global isSolved

    # Basis
    if len(hurufList) == len(number) :
        map = {}
        for n, m in zip(letter,number) :
            map[n] = m
        for i in range(len(word)) :
            if map[word[i][0]] == 0 :
                return
        solveCrypt.counter = solveCrypt.counter + 1

        wordList = [0 for i in range(len(word))]
        for i in range(len(word)) :
            wordList[i] = ''
        for i in range(len(word)) :
            for j in word[i] :
                wordList[i] += str(map[j])
        sum = 0
        for i in range(len(wordList)-1) :
            sum = sum + int(wordList[i])
        if sum == int(wordList[len(wordList)-1]) :
            print("Solusi : ")
            printSolusi(wordList)
            print("Jumlah tes yang dilakukan untuk mendapat solusi ini sebanyak : ",solveCrypt.counter,"\n \n")
            isSolved = True
        return
    
    # Rekurens
    for i in range(10) :
        if not isVisit[i] :
            isVisit[i] = True
            number.append(i)
            solveCrypt(letter,number,isVisit,word)
            number.pop()
            isVisit[i] = False

# ---------- END of FUNGSI TAMBAHAN ---------- #


# ---------- PROGRAM UTAMA ---------- #

# Input file
fileTest = input("Nama file : ")
folderTest = "../test/"
sourceTest = folderTest + fileTest
operandList = []

with open(sourceTest,'r') as files :
    for line in files :
        operandList += filter(None, re.split(r'\W|\d', line))

# Variabel boolean untuk mengetahui apakah percobaan sudah selesai
isSolved = False

# Memasukkan operand dan hasil kedalam list
hasilList = operandList[len(operandList)-1]
operandList.pop()
opList = operandList

# Mengambil waktu saat memulai percobaan
start_time = time.perf_counter()

# Memasukan list per line kedalam list berisi setiap huruf
if len(hasilList) > (maks(opList)+1) :
    print("\n")
    print("Solusi tidak dapat ditemukan")
else :
    hurufList = []
    for i in range(len(opList)) :
        for j in opList[i] :
            if j not in hurufList :
                hurufList.append(j)
    for n in hasilList :
        if n not in hurufList :
            hurufList.append(n)
    if len(hasilList) > 10 :
        print("\n")
        print("Jumlah maksimal huruf dalam operand adalah 10 buah !")
        exit()

# Memunculkan soal kelayar dengan fungsi 'printSoal'
print("\n")
print("Soal : ")
printSoal(opList)
print("\n")

# Memanggil fungsi 'solveCrypt' untuk menemukan solusi
opList.append(hasilList)
solveCrypt.counter = 0
solveCrypt(hurufList,[],[False for _ in range(10)],opList)

# Jika soal tidak dapat ditemukan solusinya
if not isSolved :
    print("\n")
    print("Solusi tidak dapat ditemukan")

# Memunculkan total waktu yang digunakan untuk menyelesaikan percobaan
print("Total waktu yang dibutuhkan untuk menemukan solusi : ","%.2f"%(time.perf_counter() - start_time), "detik")

# ---------- END of PROGRAM UTAMA ---------- #
