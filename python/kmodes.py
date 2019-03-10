



#################
# print cluster points in K-modes

# link : https://github.com/nicodv/kmodes/blob/master/examples/soybean.py
# we have clusters=10 , hence classtable of 10 * 10
print('Results tables:')
for result in (kproto):
    classtable = np.zeros((10, 10), dtype=int)
    for ii, _ in enumerate(y):
        classtable[int(y[ii][-1]) - 1, result.labels_[ii]] += 1
    print("\n")
    print("    | Cl. 1 | Cl. 2 | Cl. 3 | Cl. 4 | Cl. 5 | Cl. 6 | Cl. 7 | Cl. 8 | Cl. 9 | Cl. 10 |")
    print("----|-------|-------|-------|-------|")
    for ii in range(4):
        prargs = tuple([ii + 1] + list(classtable[ii, :]))
        print(" D{0} |    {1:>2} |    {2:>2} |    {3:>2} |    {4:>2} |  {5:>2} |    {6:>2} |    {7:>2} |    {8:>2} | {9:>2} |    {10:>2} |".format(*prargs))



