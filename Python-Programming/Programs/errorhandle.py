# Exceptions and lists

def getStats(classList):
	newStats = []
	for person in classList:
		newStats.append([person[0], person[1], avg(person[1])])
	return newStats 

# avg function: version with an exception
def avg(grades):
	try:
		return sum(grades)/len(grades)
	except ZeroDivisionError:
		print('warning: no grades data')
		return 'nan'
        
'''
# avg function: version with assert
def avg(grades):
	assert len(grades) != 0, 'warning: no grades data'
	return sum(grades)/len(grades)
'''

testGrades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], 
              [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
              [['captain', 'america'], [80.0, 70.0, 96.0]],
              [['deadpool'], []]]

print(getStats(testGrades))
