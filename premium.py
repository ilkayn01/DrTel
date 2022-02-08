def standard_insurance(file):
  file = file.copy()
  file['insurance'] = 1880
  for i in range(len(file)):
    if file.medianSpeed[i] <= 3:
      file.insurance[i] = file.insurance[i]*1.05
    elif (file.medianSpeed[i] <= 10 and file.medianSpeed[i] > 3):
      file.insurance[i] = file.insurance[i]*1.10
    elif (file.medianSpeed[i] <= 25 and file.medianSpeed[i] > 10):
      file.insurance[i] = file.insurance[i]*1.15
    elif (file.medianSpeed[i] <= 40 and file.medianSpeed[i] > 25):
      file.insurance[i] = file.insurance[i]*1.20
    elif file.medianSpeed[i] > 40:
      file.insurance[i] = file.insurance[i]*1.25
  return speeding(file)

def speeding(file):
  file = file.copy()
  for i in range(len(file)):
    if file.medianSpeed[i] > 24:
      file.insurance[i] = file.insurance[i]*1.25
  return urban(file)

def urban(file):
  file = file.copy()
  for i in range(len(file)):
    if file.speedingUrban[i] > mean(file.speedingUrban):
      file.insurance[i] = file.insurance[i]*1.45
  return jerks(file)

def jerks(file):
  file = file.copy()
  for i in range(len(file)):
    if file.jerkCount[i] > mean(file.jerkCount):
      file.insurance[i] = file.insurance[i]*1.20
    else:
      file.insurance[i] = file.insurance[i]*1.05
  return accelerating(file)

def accelerating(file):
  file = file.copy()
  for i in range(len(file)):
    if file.maxAcc[i] > mean(file.maxAcc):
      file.insurance[i] = file.insurance[i]*1.35
    else:
      file.insurance[i] = file.insurance[i]*1.15
  return file

res = standard_insurance(res)
