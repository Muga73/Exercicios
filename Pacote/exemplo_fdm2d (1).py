import numpy as np;
import numpy.linalg as la;
A = np.array([[-4, 1, 1, 0, 1, 0],
			  [ 1,-4, 0, 1, 0, 1],
              [ 1, 0,-4, 1, 0, 0],
			  [ 0, 1, 1,-4, 0, 0],
			  [ 1, 0, 0, 0,-1, 0],
			  [ 0, 1, 0, 0, 0,-1]]);

b = np.array([-15, -10, -70, -50, 0, 0]);

phi = la.solve(A,b)

print(phi)
