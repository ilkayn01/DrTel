path = os.getcwd()
csv_files = []
for i in csv_folders:
  csv_files.append(glob.glob(os.path.join(f'{i}', "*.csv")))

#speed (max, min, avg, median), distance travelled (max, min, avg, median), time travelled per trip (max, min, avg, median)
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
  
#df = data(csv_files)

#new_csv = csv_files
portion1 = new_csv[0:50]
new_csv = new_csv[50:]
print(len(new_csv), len(csv_files))

res = pd.DataFrame(columns = ['turno', 'tripDuration', 'tripDistance', 'activeDriving', 'stopDuration', 'stopNo', 'speed', 'jerkCount', 'maxAngVel', 'maxAcc',
                                 'maxJerk', 'medianSpeed', 'medianAcc', 'avgAngleChange', 'meanSpeed', 'meanAcc', 'urban', 'highway', 'speedingUrban', 
                                 'speedingHighway'])
res = pd.read_csv('final.csv')
del res['Unnamed: 0']

p1 = join(portion4, 50)
p2 = join(portion5, 36)
#p3 = join(portion3, 50)

res = pd.concat([res, p1, p2], axis=0)
