from yahoo_finance import Share

class Finance:

	#companyCodeVal must be a string
	def __init__(self, companyCodeVal):
		self.companyCode = companyCodeVal #YHOO
		self.jsonObj = [{}]

	def displayFinance(self, yearStart, yearEnd):
		yahoo = Share(self.companyCode)

		#declare
		textReturn = ""

		textReturn += "Opening price: " + str(yahoo.get_open()) + '\n'
		self.jsonObj[0]["openPrice"] = str(yahoo.get_open())

		textReturn += "Current price: " + str(yahoo.get_price()) + '\n'
		self.jsonObj[0]["currPrice"] = str(yahoo.get_price())

		textReturn += "Dividend Share: " + str(yahoo.get_dividend_share()) + '\n'
		self.jsonObj[0]["dividendPrice"] = str(yahoo.get_dividend_share())
		
		textReturn += "Year High: " + str(yahoo.get_year_high()) + '\n'
		self.jsonObj[0]["yearHigh"] = str(yahoo.get_year_high())
		
		textReturn += "Year Low: " + str(yahoo.get_year_low()) + '\n'
		self.jsonObj[0]["yearLow"] = str(yahoo.get_year_low())

		#historical data returns a jSON object
		jsonHistorical = yahoo.get_historical(str(yearStart) + '-04-25', str(yearEnd) + '-04-29')

		textReturn += "Historical Data: " + '\n'

		#To limit the number of historical datapoints sent
		numHist = 0
		maxHist = 10

		for dict in jsonHistorical:
			numHist += 1

			if numHist < maxHist:
				textReturn += "For year " + dict['Date'] + " High was: " + dict['High'] + " Low was: " + dict['Low'] + '\n'
				self.jsonObj[0][dict['Date'] + "High"] = dict['High']
				self.jsonObj[0][dict['Date'] + "Low"] = dict['Low']

		if textReturn = "":
			self.jsonObj[0]["success"] = "false"
		else:
			self.jsonObj[0]["success"] = "true"

		return textReturn

	def convertToJson(self):

		return self.jsonObj
