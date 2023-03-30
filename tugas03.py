# Mendefinisikan objek-objek
obj1 = "mahasiswa fasilkom universitas jember adalah mahasiswa hebat"
obj2 = "universitas jember memiliki 30.000 mahasiswa"
obj3 = "saat ini fasilkom universitas jember memiliki tiga prodi"
obj4 = "prodi pertama fasilkom universitas jember saat ini adalah prodi sistem informasi"


# Membuat  dictionary kosong yang akan digunakan untuk menyimpan hasil inverted index.
inverted_index = {}

# Memecah setiap objek menjadi kata-kata individu Baris-baris ini melakukan loop pada setiap objek dan memecah setiap objek menjadi kata-kata individu menggunakan metode .split()
# Loop ini menggunakan enumerate() untuk mengambil setiap objek dari list [obj1, obj2, obj3, obj4] 
# dan memberikan ID dokumen yang sesuai untuk setiap objek. 
for i, obj in enumerate([obj1, obj2, obj3, obj4], start=1):
    words = obj.split() # memecah objek menjadi kata-kata
    
    # Menampilkan representasi dari setiap objek
    print(f"obj {i} -> D {i} = {words}")
    
    # Memperbarui inverted index
    for word in words:
        # Jika kata sudah ada di dalam inverted index, tambahkan ID dokumen
        if word in inverted_index:
            if i not in inverted_index[word]:
                inverted_index[word].append(i)
        # Jika kata belum ada di dalam inverted index, buat entri baru
        else:
            inverted_index[word] = [i]



# Menampilkan dictionary dan inverted index
print("\nDictionary\t| Inverted Index")
print("="*80)
# Menampilkan inverted index secara urut berdasarkan urutan kata secara ascending
for word in sorted(inverted_index.keys()):
    # Menampilkan kata dan ID dokumen di mana kata tersebut muncul
    print("{:<15} | {}".format(word, inverted_index[word]))

query = input("\nMembangun Query\n---------------\nKetik yang anda cari: ").split()
relevant_docs = []
for word in query:
    if word in inverted_index:
        relevant_docs.append(inverted_index[word])
    
# Print 
print("\nDokumen yang sesuai dengan query")
print("-----------------------------------")
print(relevant_docs)
print(f"{' '.join(query)} (S 1 ): {relevant_docs}")

# logika AND
retrieved_docs = set.intersection(*[set(doc) for doc in relevant_docs])
print("\nRetrieved object (R) dengan logika 'AND'")
for doc in retrieved_docs:
    print(f"Obj {doc} : {globals()['obj'+str(doc)]}")

# logika OR
retrieved_docs = set.union(*[set(doc) for doc in relevant_docs])
print("\nRetrieved object (R) dengan logika 'OR'")
for doc in retrieved_docs:
    print(f"Obj {doc} : {globals()['obj'+str(doc)]}")

# logika NOT (logika AND dengan kata-kata yang tidak ada dalam query)
not_query = [word for word in inverted_index.keys() if word not in query]
not_relevant_docs = []
for word in not_query:
    if word in inverted_index:
        not_relevant_docs.append(inverted_index[word])

not_retrieved_docs = set.intersection(*[set(doc) for doc in not_relevant_docs])
print("\nRetrieved object (R) dengan logika 'NOT'")
for doc in not_retrieved_docs:
    print(f"Obj {doc} : {globals()['obj'+str(doc)]}")


#TUGAS 03 METODE TIGA PERANGKINGAN

# soal 1. Metode Jaccard
print("\nRetrieved object (R) dengan metode Jaccard")
for i in range(1, len(relevant_docs)+1):
    for j in range(i+1, len(relevant_docs)+1):
        doc1 = set(relevant_docs[i-1])
        doc2 = set(relevant_docs[j-1])

        #Rumus Jaccard
        jaccard = len(doc1.intersection(doc2)) / len(doc1.union(doc2))
        print(f"score antara Obj {i} dan Obj {j} : {jaccard:.2f}")


# soal 2 Metode Dice's Coefficient (DSC)
print("\nRetrieved object (R) dengan metode Dice's Coefficient (DSC)")
for i in range(1, len(relevant_docs)+1):
    for j in range(i+1, len(relevant_docs)+1):
        doc1 = set(relevant_docs[i-1])
        doc2 = set(relevant_docs[j-1])

        # Rumus DSC
        dsc = 2 * len(doc1.intersection(doc2)) / (len(doc1) + len(doc2))
        print(f"score antara Obj {i} dan Obj {j} : {dsc:.2f}")


# Metode Overlap Similarity
print("\nRetrieved object (R) dengan metode Overlap Similarity")
for i in range(1, len(relevant_docs)+1):
    for j in range(i+1, len(relevant_docs)+1):
        doc1 = set(relevant_docs[i-1])
        doc2 = set(relevant_docs[j-1])

        #Rumus Overlap similarity
        overlap = len(doc1.intersection(doc2))
        os = overlap / len(doc1)
        print(f"Score antara Obj {i} dan Obj {j} : {os:.2f}")
