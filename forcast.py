import forecastio

class Weather:


	def __init__(self, latVal, lngVal):
		
		self.lat = latVal #31.967819
		self.lng = lngVal #115.87718
		#time = "2016-06-13T12:00:00"

	def displayWeather(self, timeFrameUserVal):
		

		api_key = "ece623732956ab6653653c4cec4247fa"
		#load the forcast for the latitute and longitude
		forecast = forecastio.load_forecast(api_key, self.lat, self.lng)

		timeFrameUser = timeFrameUserVal #"today"

		#Based on what time frame the user chose, display weather
		if timeFrameUser == "hourly":
			timeFrame = forecast.hourly()

			print(timeFrame.summary)
			print(timeFrame.icon)
			
			listOfTemps = []
			numHour = 0

			print("Hourly temperature for today")
			for onePieceData in timeFrame.data:
				
				if numHour < 24:
					numHour += 1
					print("Time: ", numHour)
					print(onePieceData.temperature)

					listOfTemps.append(onePieceData.temperature)

		elif timeFrameUser == "today":
			listOfTemps = []
			numHour = 0
			timeFrame = forecast.currently()

			print(timeFrame.summary)
			print(timeFrame.icon)
			print("average temperature for the day: ", timeFrame.temperature)

			timeFrame = forecast.hourly()
			for onePieceData in timeFrame.data:
				
				if numHour < 24:
					numHour += 1
					listOfTemps.append(onePieceData.temperature)

			print("min value for today : ", min(listOfTemps))
			print("max value for today : ", max(listOfTemps))

		elif timeFrameUser == "weekly":
			timeFrame = forecast.daily()

			print(timeFrame.summary)
			print(timeFrame.icon)