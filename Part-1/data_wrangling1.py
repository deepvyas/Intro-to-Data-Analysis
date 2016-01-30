import unicodecsv,csv
from datetime import datetime

enrollments_filepath = '../Dataset/enrollments.csv'
submissions_filepath = '../Dataset/project_submissions.csv'
engagement_filepath = '../Dataset/daily_engagement.csv'

def csv2list(filename):
	with open(filename,'rb') as f:
		iterator = unicodecsv.DictReader(f)
		return list(iterator)

def parse_date(date_s):
	if date_s == '':
		return None
	else:
		return datetime.strptime(date_s , '%Y-%m-%d')
def parse_int(i):
	if i == '':
		return None
	else:
		return int(i)

def parse_double(double):
	if double == '':
		return None
	else:
		return float(double)

def parse_boolean(strg):
	if strg == 'True':
		return True
	else:
		return False

def find_uniqueset(data):
	result  = set()
	for dic in data:
		result.add(dic['account_key'])
	return result

enrollments = csv2list(enrollments_filepath)
engagements = csv2list(engagement_filepath)
submissions = csv2list(submissions_filepath)

# Changing column name

for dic in engagements: 
	dic['account_key'] = dic['acct']
	del dic['acct']

# Format Enrollment data
for enrollment in enrollments:
	enrollment['is_udacity'] = parse_boolean(enrollment['is_udacity'])
	enrollment['is_canceled'] = parse_boolean(enrollment['is_canceled'])
	enrollment['join_date'] = parse_date(enrollment['join_date'])
	enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
	enrollment['days_to_cancel'] = parse_int(enrollment['days_to_cancel'])

# Format Submission Data
for engagement in engagements:
	engagement['lessons_completed'] = parse_int(parse_double(engagement['lessons_completed']))
	engagement['num_courses_visited'] = parse_int(parse_double(engagement['num_courses_visited']))
	engagement['projects_completed'] = parse_int(parse_double(engagement['projects_completed']))
	engagement['utc_date'] = parse_date(engagement['utc_date'])
# Format engagements Data
for submission in submissions:
	submission['completion_date'] = parse_date(submission['completion_date'])
	submission['creation_date'] = parse_date(submission['creation_date'])

new_enrollments_filepath = "../Dataset/enrollments_wrangled.csv"
new_submissions_filepath = "../Dataset/submissions_wrangled.csv"
new_engagements_filepath = "../Dataset/engagements_wrangled.csv"

def write2csv(filename,dataset):
	keys = dataset[0].keys()
	with open(filename,'wb') as f:
		writer = csv.DictWriter(f,keys)
		writer.writeheader()
		writer.writerows(dataset)


write2csv(new_engagements_filepath,engagements)
write2csv(new_enrollments_filepath,enrollments)
write2csv(new_submissions_filepath,submissions)




enrollment_num_rows = len(enrollments)
engagement_num_rows = len(engagements)
submission_num_rows = len(submissions)
enrollment_num_rows_unique = len(find_uniqueset(enrollments))
submissions_num_rows_unique = len(find_uniqueset(submissions))
engagement_num_rows_unique = len(find_uniqueset(engagements))


# print engagement_num_rows
# print enrollment_num_rows
# print submission_num_rows
# print enrollment_num_rows_unique
# print submissions_num_rows_unique
# print engagement_num_rows_unique


