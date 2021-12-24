def drive(loc_files):
  frame = []
  for i in loc_files:
    d = pd.read_csv(i)
    frame.append(d)
  return frame

def plot(file):
  frame = drive(file)
  fig = plt.figure(figsize = (12, 7))
  for i in frame:
    plt.plot(i['x'], i['y'])
  plt.show()

#determines sharp turns based on parameters
def binary(x, limit, ref):
  for i in ref:
    if (i >= limit):
      x.append(1)
    else:
      x.append(0)
  return x

def angle_to(x2, y2, x1, y1, rotation=0, clockwise=False):
    angle = degrees(atan2(y2-y1, x2-x1)) - rotation
    if not clockwise:
        angle = -angle
    return angle % 360

  def dd(df):
  total = pd.DataFrame(columns = ['x', 'y', 'd', 's', 't', 'angle', 'sharp_turn', 'sharp_turn_count', 'hway'])
  df = drive(df)
  for i in range(200):
    tr = dist(df[i])
    total = pd.concat([total, tr])
  total['t'] = total.index
  return total

def combine(file, x):
  df = dd(file[x])
  return compress(df)
