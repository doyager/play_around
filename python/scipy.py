
########################################################




1.   CSR - Compressed Sparse Row matrix


scipy.sparse.csr_matrix
class scipy.sparse.csr_matrix(arg1, shape=None, dtype=None, copy=False)[source]
Compressed Sparse Row matrix

This can be instantiated in several ways:
csr_matrix(D)
with a dense matrix or rank-2 ndarray D
csr_matrix(S)
with another sparse matrix S (equivalent to S.tocsr())
csr_matrix((M, N), [dtype])
to construct an empty matrix with shape (M, N) dtype is optional, defaulting to dtype=’d’.
csr_matrix((data, (row_ind, col_ind)), [shape=(M, N)])
where data, row_ind and col_ind satisfy the relationship a[row_ind[k], col_ind[k]] = data[k].
csr_matrix((data, indices, indptr), [shape=(M, N)])
is the standard CSR representation where the column indices for row i are stored in indices[indptr[i]:indptr[i+1]] and their corresponding values are stored in data[indptr[i]:indptr[i+1]]. If the shape parameter is not supplied, the matrix dimensions are inferred from the index arrays.
Notes

Sparse matrices can be used in arithmetic operations: they support addition, subtraction, multiplication, division, and matrix power.

Advantages of the CSR format
efficient arithmetic operations CSR + CSR, CSR * CSR, etc.
efficient row slicing
fast matrix vector products
Disadvantages of the CSR format
slow column slicing operations (consider CSC)
changes to the sparsity structure are expensive (consider LIL or DOK)
Examples

>>>
>>> import numpy as np
>>> from scipy.sparse import csr_matrix
>>> csr_matrix((3, 4), dtype=np.int8).toarray()
array([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]], dtype=int8)
>>>
>>> row = np.array([0, 0, 1, 2, 2, 2])
>>> col = np.array([0, 2, 2, 0, 1, 2])
>>> data = np.array([1, 2, 3, 4, 5, 6])
>>> csr_matrix((data, (row, col)), shape=(3, 3)).toarray()
array([[1, 0, 2],
       [0, 0, 3],
       [4, 5, 6]])
>>>
>>> indptr = np.array([0, 2, 3, 6])
>>> indices = np.array([0, 2, 2, 0, 1, 2])
>>> data = np.array([1, 2, 3, 4, 5, 6])
>>> csr_matrix((data, indices, indptr), shape=(3, 3)).toarray()
array([[1, 0, 2],
       [0, 0, 3],
       [4, 5, 6]])
As an example of how to construct a CSR matrix incrementally, the following snippet builds a term-document matrix from texts:

>>>
>>> docs = [["hello", "world", "hello"], ["goodbye", "cruel", "world"]]
>>> indptr = [0]
>>> indices = []
>>> data = []
>>> vocabulary = {}
>>> for d in docs:
...     for term in d:
...         index = vocabulary.setdefault(term, len(vocabulary))
...         indices.append(index)
...         data.append(1)
...     indptr.append(len(indices))
...
>>> csr_matrix((data, indices, indptr), dtype=int).toarray()
array([[2, 1, 0, 0],
       [0, 1, 1, 1]])
Attributes:	
dtype : dtype
Data type of the matrix

shape : 2-tuple
Get shape of a matrix.

ndim : int
Number of dimensions (this is always 2)

nnz
Number of stored values, including explicit zeros.

data
CSR format data array of the matrix

indices
CSR format index array of the matrix

indptr
CSR format index pointer array of the matrix

has_sorted_indices
Determine whether the matrix has sorted indices

#####

# quick_run_code

import numpy as np
import pandas as pd
from scipy import sparse

n_rows = 3
n_cols = 3
rows = np.array([0, 0, 1, 2, 2, 2])
cols = np.array([0, 2, 2, 0, 1, 2])
data = np.array([1, 2, 3, 4, 5, 6])

X = sparse.csr_matrix((data, (rows, cols)), shape=(n_rows, n_cols))


#save 
sparse.save_npz( '/Users/mac/workspace/X.npz', X)

#load 
test_X = sparse.load_npz('/Users/mac/workspace/X.npz')
#######################
