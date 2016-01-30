import unicodecsv
from data_wrangling1 import csv2list,find_uniqueset
from data_wrangling1 import engagements,enrollments,submissions  #Cleaned and data-typed data from data_wrangling1 available here.
new_engagements_filepath = "../Dataset/engagements_wrangled.csv"
new_enrollments_filepath = "../Dataset/enrollments_wrangled.csv"
new_submissions_filepath = "../Dataset/submissions_wrangled.csv"

# engagements = csv2list(new_engagements_filepath) 
# enrollments = csv2list(new_enrollments_filepath)
# submissions = csv2list(new_submissions_filepath)

engagements_set = find_uniqueset(engagements)
enrollments_set = find_uniqueset(enrollments)


for enrollment in enrollments:
	key = enrollment['account_key']
	if key not in engagements_set:
		# print enrollment
		break;


# This code shows that there are students in enrollment table not in engagements due to fact that join and cancel date is same.
num =0
for enrollment in enrollments:
	key = enrollment['account_key']
	if key not in engagements_set and enrollment['days_to_cancel'] !=0:
		num += 1

# print num

''' This shows there are 3 students in enrollment not in engagement even though join date != cancel date.On further investigation we see 
 we see all of them have is_udacity as true showing they are test accounts.'''

# Following code reomoves all test_accounts.

test_bots = set()
for enrollment in enrollments:
	if enrollment['is_udacity']:
		test_bots.add(enrollment['account_key'])


def removebots(data):
	clean_data = []
	for dic in data:
		if dic['account_key'] not in test_bots:
			clean_data.append(dic)

	return clean_data

non_bot_enrollments = removebots(enrollments)
non_bot_engagements = removebots(engagements)
non_bot_submissions  = removebots(submissions)

# print len(non_bot_engagements)
# print len(non_bot_enrollments)
# print len(non_bot_submissions)

'''############### This tentatively ends the first part of Data Wrangling. It was spread over two files:
					1. data_wrangling1.py
					2.data_investigation.py
		A good plan to take a course in Data Wrangling(using MongoDB) is in pipe.

	Coded by Deep Vyas(PHANTM_V) for Intro to Data analysis. '''




