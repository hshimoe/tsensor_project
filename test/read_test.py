from raw_to_ndarray import SensorData

data = SensorData()
#data.make_dummy(109)
print(data.data.shape[1])
print(data.split(2,1).shape[1])