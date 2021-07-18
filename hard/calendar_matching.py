# Calendar Matching

# Imagine that you want to schedule a meeting of a certain duration with a
# co-worker. You have access to your calendar and your co-worker's calendar
# (both of which contain your respective meetings for the day, in the form of
# [startTime, endTime]), as well as both of your daily bounds (i.e., the
# earliest and latest times at which you're available for meetings every day, in
# the form of [earliestTime, latestTime]).

# Write a function that takes in your calendar, your daily bounds, your
# co-worker's calendar, your co-worker's daily bounds, and the duration of the
# meeting that you want to schedule, and that returns a list of all the time
# blocks (in the form of [startTime, endTime]) during which you could schedule
# the meeting, ordered from earliest time block to latest.

# Note that times will be given and should be returned in military time. For
# example: 8:30, 9:01, and 23:56.

# Also note that the given calendar times will be sorted by start time in
# ascending order, as you would expect them to appear in a calendar application like Google Calendar.

# Sample Input
# calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
# dailyBounds1 = ['9:00', '20:00']
# calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
# dailyBounds2 = ['10:00', '18:30']
# meetingDuration = 30
# Sample Output
# [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]

# Solution

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
	startTime = get_bound_time(dailyBounds1[0], dailyBounds2[0])
	endTime = get_bound_time(dailyBounds1[1], dailyBounds2[1], False)
	if len(calendar1) == 0 and len(calendar2) == 0:
		return [[startTime.toStr(), endTime.toStr()]]
	formattedCalendar1 = [TimeBlock(date[0], date[1]) for date in calendar1]
	formattedCalendar2 = [TimeBlock(date[0], date[1]) for date in calendar2]
	alreadyBooked = getAlreadyBooked(formattedCalendar1, formattedCalendar2)
	flattenedBooked = flattenCalendar(alreadyBooked)
	return getAvailableSlots(startTime, endTime, flattenedBooked, meetingDuration)
	
def getAvailableSlots(startTime, endTime, flattenedBooked, meetingDuration):
	results = []
	if startTime.totalMinutes() + meetingDuration <= flattenedBooked[0].start.totalMinutes():
		results.append(TimeBlock(startTime.toStr(), flattenedBooked[0].start.toStr()))
	for i in range(len(flattenedBooked) - 1):
		if startTime.totalMinutes() > flattenedBooked[i].end.totalMinutes():
			start_block = startTime.totalMinutes()
		else:
			start_block = flattenedBooked[i].end.totalMinutes()
		if endTime.totalMinutes() < flattenedBooked[i].start.totalMinutes():
			end_block = endTime.totalMinutes()
		else:
			end_block = flattenedBooked[i + 1].start.totalMinutes()
		if start_block + meetingDuration <= end_block:
			results.append(TimeBlock(flattenedBooked[i].end.toStr(), flattenedBooked[i + 1].start.toStr()))
	if endTime.totalMinutes() - meetingDuration >= flattenedBooked[-1].end.totalMinutes():
		results.append(TimeBlock(flattenedBooked[-1].end.toStr(), endTime.toStr()))
	return [[result.start.toStr(), result.end.toStr()] for result in results]
	
def getAlreadyBooked(calendar1, calendar2):
	booked = []
	i = 0
	j = 0
	while i < len(calendar1) and j < len(calendar2):
		calendar1StartTime = calendar1[i].start
		calendar2StartTime = calendar2[j].start
		if calendar1StartTime.totalMinutes() < calendar2StartTime.totalMinutes():
			booked.append(calendar1[i])
			i += 1
		else:
			booked.append(calendar2[j])
			j += 1
	while i < len(calendar1):
		booked.append(calendar1[i])
		i += 1
	while j < len(calendar2):
		booked.append(calendar2[j])
		j += 1
	return booked

def flattenCalendar(calendar):
	flattened = [calendar[0]]
	for i in range(1, len(calendar)):
		last_end = flattened[-1].end.totalMinutes()
		this_start = calendar[i].start.totalMinutes()
		this_end = calendar[i].end.totalMinutes()
		if last_end >= this_start:
			if last_end > this_end:
				new_end = flattened[-1].end
			else: 
				new_end = calendar[i].end
			flattened[-1].end = new_end
		else:
			flattened.append(calendar[i])
	return flattened
	
def get_bound_time(date1, date2, start = True):
	time1 = Time(date1)
	time2 = Time(date2)
	if start:
		return time1 if time1.totalMinutes() > time2.totalMinutes() else time2
	else:
		return time1 if time1.totalMinutes() < time2.totalMinutes() else time2


class Time:

	def __init__(self, timeString):
		hours, minutes = timeString.split(':')
		self.hours = int(hours)
		self.minutes = int(minutes)

	def totalMinutes(self):
		return self.hours * 60 + self.minutes
	
	def toStr(self):
		hours = str(self.hours)
		minutes = f'0{str(self.minutes)}' if self.minutes < 10 else str(self.minutes)
		return f'{hours}:{minutes}'


class TimeBlock:
	def __init__(self, start, end):
		self.start = Time(start)
		self.end = Time(end)