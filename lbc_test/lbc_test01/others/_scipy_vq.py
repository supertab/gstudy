import numpy as np
import scipy.cluster.vq as vq

centorid = np.array([[1.3,2],[3,4]])
point = np.array([[0.5, 1]]) # point shape should be(n, 2)
label, dist = vq.vq(point, centorid)
