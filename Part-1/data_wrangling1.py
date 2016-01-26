import unicodecsv
from datetime import datetime

enrollments_filepath = './Dataset/enrollments.csv'
submissions_filepath = './Dataset/project_submissions.csv'
engagement_filepath = './Dataset/daily_engagement.csv'

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


enrollments = csv2list(enrollments_filepath)
engagements = csv2list(submissions_filepath)
submissions = csv2list(engagement_filepath)

# Format Enrollment data
for enrollment in enrollments:
	enrollment['is_udacity'] = parse_boolean(enrollment['is_udacity'])
	enrollment['is_canceled'] = parse_boolean(enrollment['is_canceled'])
	enrollment['join_date'] = parse_date(enrollment['join_date'])
	enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
	enrollment['days_to_cancel'] = parse_int(enrollment['days_to_cancel'])

# Format Submission Data
for submission in submissions:
	submission['lessons_completed'] = parse_int(parse_double(submission['lessons_completed']))
	submission['num_courses_visited'] = parse_int(parse_double(submission['num_courses_visited']))
	submission['projects_completed'] = parse_int(parse_double(submission['projects_completed']))
	submission['utc_date'] = parse_date(submission['utc_date'])
# Format engagements Data
for engagement in engagements:
	engagement['completion_date'] = parse_date(engagement['completion_date'])
	engagement['creation_date'] = parse_date(engagement['creation_date'])

# print enrollments[0]
# print engagements[0]
# print submissions[0]



