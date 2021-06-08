from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
	return render_template('Form.html')


@app.route('/result', methods=['POST','GET'])
def login():
	
	day = int(request.form['Day'])
	month = int(request.form['Month'])
	year = int(request.form['Year'])

	MONTH30 = [4, 6, 9, 11]
	DAY2 = 28
	if year%400 == 0:
		DAY2 = 29
	elif year%100 == 0:
		pass
	elif year%4 == 0:
		DAY2 = 29
	

	if day < 1 or day > 31 or month < 1 or month > 12 or year < 0 or (month in MONTH30 and day == 31) or (month == 2 and day > DAY2):
		return f"<center><h1><br><br><br>Invalid Date</h1></center>"

	wd=""   #week-day
	d=6
	y=year
	d+= (y*365)+(y//4)-(y//100)+(y//400)
	if month == 12:
		d+= 30
	if month >= 11:
        	d+= 31
	if month >= 10:
		d+= 30
	if month >= 9:
		d+= 31
	if month >= 8:
		d+= 31
	if month >= 7:
		d+= 30
	if month >= 6:
		d+= 31
	if month >= 5:
		d+= 30
	if month >= 4:
		d+= 31
	if month >= 3:
		if(year%400==0):
			d+= 29
		elif(year%100==0):
 			d+= 28
		elif(year%4==0):
			d+= 29
		else:
			d+= 28
	if month >= 2:
		d+= 31
	if month >= 1:
		if(year%400==0):
			d-= 1
		elif(year%100==0):
			d = d
		elif(year%4==0):
			d-= 1

	d+= day
	d%= 7
	if d == 0:
		wd="SUNDAY"
	if d == 1:
		wd="MONDAY"
	if d == 2:
		wd="TUESDAY"
	if d == 3:
		wd="WEDNESDAY"
	if d == 4:
		wd="THURSDAY"
	if d == 5:
		wd="FRIDAY"
	if d == 6:
		wd="SATURDAY"
	print('The Week Day is:', wd)

	return f"<center><h1><br><br><br>Week Day: {wd}</h1></center>"

if __name__ == '__main__':
	app.run(debug=True)
