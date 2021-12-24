import math
from scipy.spatial import distance
def get_angle(p1, p2, p3):
  dot_product = (p1[0] - p2[0]) * (p3[0] - p2[0]) + (p1[1] - p2[1]) * (p3[1] - p2[1])
  denominator = max(distance.euclidean(p1, p2) * distance.euclidean(p2, p3), 0.1)
  ratio = dot_product / denominator
  if ratio > 1:
    ratio = 1
  if ratio < -1:
    ratio = -1
  angle = math.acos(ratio)
  return angle * 180 / math.pi

def getTurn(x):
  x=np.array(x[10:-10])
  return len(x[x>15])
