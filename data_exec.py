df = pd.DataFrame(columns = ['max_s', 'min_s', 'avg_s', 'median_s', 'max_d', 'min_d', 
                             'avg_d', 'median_d', 'total_d_tr', 'max_t', 'min_t', 'avg_t', 'median_t', 'total_t_tr'])

def dist(file):
  distance = []
  for i in range(1, len(file)):
    distance.append(((file.x[i]-file.x[i-1])**2 + (file.y[i]-file.y[i-1])**2)**0.5)
  return [sum(distance)/1000, sum(distance)*18/(len(file)*5), len(file)/3600]

def data(file):
  for i in range(len(file)):
    d = [dist(i)[0] for i in drive(file[i])]
    sp = [dist(i)[1] for i in drive(file[i])]
    t = [dist(i)[2] for i in drive(file[i])]
    details = [str(i), max(sp), min(sp), mean(sp), median(sp), max(d), min(d), mean(d), median(d), sum(d), max(t), min(t), mean(t), median(t), sum(t)]
    df.loc[len(df)] = details
  return df

def data_per_driver(file):
  distance = []
  for i in range(1, len(file)):
    distance.append(((file.x[i]-file.x[i-1])**2 + (file.y[i]-file.y[i-1])**2)**0.5)
  return [sum(distance)/1000, sum(distance)*18/(len(file)*5), len(file)/3600]
