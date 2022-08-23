num_of_sets = input()
nums = int(input())
n_set = set()
m_set = set()

for sets in num_of_sets:
    n, m = num_of_sets.split()

    for k in n:
        n_set.add(k)

    for j in m:
        m_set.add(j)

# print(n_set.intersection(m_set))
# print(m_set)
print(n_set)
