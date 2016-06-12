import forecastio

class Weather:


	def __init__(self, latVal, lngVal):

		self.lat = latVal #31.967819
		self.lng = lngVal #115.87718
		self.jsonObj = [{}]

		#time = "2016-06-13T12:00:00"

	def displayWeather(self, timeFrameUserVal):
		textReturn = ""

		api_key = "ece623732956ab6653653c4cec4247fa"
		#load the forcast for the latitute and longitude
		forecast = forecastio.load_forecast(api_key, self.lat, self.lng)

		timeFrameUser = timeFrameUserVal #"today"

		#Based on what time frame the user chose, display weather
		if timeFrameUser == "hourly":
			timeFrame = forecast.hourly()

			textReturn += timeFrame.summary
			self.jsonObj[0]["summary"] = str(timeFrame.summary)

			textReturn += '\n'
			textReturn += timeFrame.icon
			self.jsonObj[0]["icon"] = str(timeFrame.icon)

			textReturn += '\n\n'

			listOfTemps = []
			numHour = 0

			textReturn += "Hourly temperature for today"
			for onePieceData in timeFrame.data:

				if numHour < 24:
					numHour += 1
					textReturn += "Time: " + str(numHour) + '\n'
					
					textReturn += str(onePieceData.temperature) + '\n'

					self.jsonObj[0][str(numHour) + "Hr"] = str(onePieceData.temperature)

		elif timeFrameUser == "today":
			listOfTemps = []
			numHour = 0
			timeFrame = forecast.currently()

			textReturn += timeFrame.summary + '\n'
			self.jsonObj[0]["summary"] = str(timeFrame.summary)

			textReturn += timeFrame.icon + '\n'
			self.jsonObj[0]["icon"] = str(timeFrame.icon)

			textReturn += "average temperature for the day: " + str(timeFrame.temperature)
			self.jsonObj[0]["avg"] =  str(timeFrame.temperature)

			timeFrame = forecast.hourly()
			for onePieceData in timeFrame.data:

				if numHour < 24:
					numHour += 1
					listOfTemps.append(str(onePieceData.temperature))

			textReturn += '\n' + "min value for today : " + str(min(listOfTemps)) + '\n'
			self.jsonObj[0]["min"] =  str(min(listOfTemps))

			textReturn += "max value for today : " + str(max(listOfTemps))
			self.jsonObj[0]["max"] =  str(max(listOfTemps))

		elif timeFrameUser == "weekly":
			timeFrame = forecast.daily()

			textReturn += timeFrame.summary + '\n'
			self.jsonObj[0]["summary"] = str(timeFrame.summary)

			textReturn += timeFrame.icon
			self.jsonObj[0]["icon"] = str(timeFrame.icon)

		else:
			textReturn += "Format of your text should be 'WEATHER: hourly' or 'WEATHER: today' or 'WEATHER: weekly'"
		
		if textReturn = "":
			self.jsonObj[0]["success"] = "false"
		else:
			self.jsonObj[0]["success"] = "true"
			
		return textReturn

	def convertToJson(self):

		return self.jsonObj
