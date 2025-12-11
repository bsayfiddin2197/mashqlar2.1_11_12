# 1
kvadratlar = {n*n for n in range(1, 21)}
print(kvadratlar)

# 2
sozlar = ["Hello", "WORLD", "Python", "CoDe"]

kichik_set = {s.lower() for s in sozlar}
print(kichik_set)

# 3
raqam_yig_10 = {
    n for n in range(1, 101)
    if sum(int(x) for x in str(n)) == 10
}
print(raqam_yig_10)

# 4
matn = "Assalomu Alaykum, Python!"

unlilar = "aeiouAEIOU"

unli_set = {ch for ch in matn if ch in unlilar}
print(unli_set)

# 5
lst = [-10, 5, 12, 20, -25, 30, 7, 15]

musbat_5_karrali = {x for x in lst if x > 0 and x % 5 == 0}
print(musbat_5_karrali)
