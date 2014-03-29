import numpy, sklearn
from sklearn import linear_model

def normalize_sample(sample):
	# Normalize Class 1
	total = sample[0] + sample[1] + sample[2]
	factor = 1 / total

	# Set negative to 0, for some reason numpy.clip does not work
	for c in range(0, sample.shape[0]):
		if sample[c] < 0:
			sample[c] = 0

	sample[0] *= factor
	sample[1] *= factor
	sample[2] *= factor

	# Normalize Class 2
	total = (sample[3] + sample[4]) / sample[1]
	factor = 1 / total

	sample[3] *= factor
	sample[4] *= factor

	# Normalize Class 3
	total = (sample[5] + sample[6]) / sample[4]
	factor = 1 / total

	sample[5] *= factor
	sample[6] *= factor

	# Normalize Class 4
	total = (sample[7] + sample[8]) / sample[4]
	factor = 1 / total

	sample[7] *= factor
	sample[8] *= factor

	# Normalize Class 5
	total = (sample[9] + sample[10] + sample[11] + sample[12]) / sample[4]
	factor = 1 / total

	sample[9] *= factor
	sample[10] *= factor
	sample[11] *= factor
	sample[12] *= factor

	# Normalize Class 6
	total = sample[13] + sample[14]
	factor = 1 / total

	sample[13] *= factor
	sample[14] *= factor

	# Normalize Class 7
	total = (sample[15] + sample[16] + sample[17]) / sample[0]
	factor = 1 / total

	sample[15] *= factor
	sample[16] *= factor
	sample[17] *= factor

	# Normalize Class 8
	total = (sample[18] + sample[19] + sample[20] + sample[21] + sample[22] + sample[23] + sample[24]) / sample[13]
	factor = 1 / total

	sample[18] *= factor
	sample[19] *= factor
	sample[20] *= factor
	sample[21] *= factor
	sample[22] *= factor
	sample[23] *= factor
	sample[24] *= factor

	# Normalize Class 9
	total = (sample[25] + sample[26] + sample[27]) / sample[3]
	factor = 1 / total

	sample[25] *= factor
	sample[26] *= factor
	sample[27] *= factor

	# Normalize Class 10
	total = (sample[28] + sample[29] + sample[30]) / sample[7]
	factor = 1 / total

	sample[28] *= factor
	sample[29] *= factor
	sample[30] *= factor

	# Normalize Class 11
	total = (sample[31] + sample[32] + sample[33] + sample[34] + sample[35] + sample[36]) / sample[7]
	factor = 1 / total

	sample[31] *= factor
	sample[32] *= factor
	sample[33] *= factor
	sample[34] *= factor
	sample[35] *= factor
	sample[36] *= factor

	return sample

def SGDTest():
	rf = []

	for i in range(0, 37):
		print "Loading model %i" %(i)
		rf.append(sklearn.linear_model.SGDRegressor(eta0=0.001, n_iter=100))
		rf[i].coef_ = numpy.loadtxt("C:\\Zoo\\features\\sgd_classifier\\model_coef_" + str(i) + ".txt", delimiter=",")
		rf[i].intercept_ = numpy.loadtxt("C:\\Zoo\\features\\sgd_classifier\\model_intercept_" + str(i) + ".txt", delimiter=",")

	result = numpy.zeros((79975, 37));
	j = 0

	with open('C:\\Zoo\\features\\test_set.csv', 'rb') as f:
		for line in f:
			for i in range(0, 37):
				result[j, i] = rf[i].predict(numpy.asarray(map(float, line.split(','))))
			j += 1

			if j % 100 == 0:
				print "Predicting, %.2f%% done" %(1.*j/79975*100)

	print "Scaling..."
	for i in range(0, result.shape[0]):
		sample = result[i, :]
		sample = normalize_sample(sample)

	numpy.savetxt("result.csv", result, delimiter=',', fmt='%.8f')

if __name__ == '__main__':
	SGDTest()