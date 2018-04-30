#Author: Clitus Dmonte
#Date: 04/06/2018
#Course Number: ITMD-513

import json
import urllib.request
import turtle
import time

#ClassA() Tracks Internation space center
class ClassA():

    def run(self,t):
        try:
            if str(t) == "":
                t = "Space Center, Houston"
            #setting up turtle screen
            screenISS = turtle.Screen()
            screenISS.setup(720, 360)
            screenISS.setworldcoordinates(-180, -90, 180, 90)
            #registering Internation space center image which will be used for tracking
            screenISS.register_shape('images/iss.gif')

            #setting background map image
            screenISS.bgpic('images/map.gif')
            iss = turtle.Turtle()
            iss.shape('images/iss.gif')
            iss.setheading(90)
            iss.penup()

            lat = 88
            lon = -100

            locationTurtle = turtle.Turtle()
            locationTurtle.penup()
            locationTurtle.color('yellow')
            locationTurtle.goto(lon, lat)
            locationTurtle.dot(10)
            locationTurtle.hideturtle()
            tracking = 'International Space Center is been Tracked from: ' + str(t)
            locationTurtle.write(tracking)


            while True:
                #API used to get current location of Internation space center
                url = 'http://api.open-notify.org/astros.json'
                responseAPI = urllib.request.urlopen(url)
                #Getting Internation space center location data from API
                resultAPI = json.loads(responseAPI.read())

                lat =  15
                lon = -175

                location = turtle.Turtle()
                location.penup()
                location.color('yellow')
                location.goto(lon,lat)
                location.dot(10)
                location.hideturtle()
                #Getting people in Internation space center information from API
                print('People in Space: ', resultAPI['number'])
                noOfPeople = 'People in Space: ' + str(resultAPI['number'])
                location.write(noOfPeople)

                namesCraft = ""
                people = resultAPI['people']
                for p in people:
                  name = str(p['name'])
                  craft = str(p['craft'])
                  namesCraft +='\n' + name + ' in ' + craft
                  print(p['name'], ' in ', p['craft'])

                lat = -35
                lon = -175
                #Plotting data on to the map
                location = turtle.Turtle()
                location.penup()
                location.color('red')
                location.goto(lon, lat)
                location.dot(10)
                location.hideturtle()
                location.write(namesCraft)

                #API to get information on when the Internation space center will pass over user selected location
                url = 'http://api.open-notify.org/iss-now.json'
                response = urllib.request.urlopen(url)
                #Getting data from API
                resultAPI = json.loads(response.read())

                location = resultAPI['iss_position']
                lat = location['latitude']
                lon = location['longitude']
                print('Latitude: ', lat)
                print('Longitude: ', lon)

                iss.goto(float(lon), float(lat))
                #Setting up conditions for user seleted specific Locations LAT and LON
                if str(t) == "Space Center, Houston":
                    # Space Center, Houston
                    lat = 29.5502
                    lon = -95.097
                elif str(t) == "london":
                    # london
                    lat = 51.5072
                    lon = 0.1275
                elif str(t) == "Tokyo":
                    # Tokyo
                    lat = 35.689487
                    lon = 139.691706
                elif str(t) == "India":
                    # India
                    lat = 20.5937
                    lon = 78.9629
                elif str(t) == "Russia":
                    # Russia
                    lat = 61.5240
                    lon = 105.3188
                elif str(t) == "England":
                    # England
                    lat = 52.3555
                    lon = 1.1743
                elif str(t) == "Germany":
                    # Germany
                    lat = 51.1657
                    lon = 10.4515
                elif str(t) == "China":
                    # Germany
                    lat = 39.9042
                    lon = 116.4074

                #Plotting data on to the map
                location = turtle.Turtle()
                location.penup()
                location.color('white')
                location.goto(lon,lat)
                location.dot(10)
                location.hideturtle()

                url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
                response = urllib.request.urlopen(url)
                resultAPI = json.loads(response.read())
                print("###############33",resultAPI)
                #
                #print resultAPI
                over = resultAPI['response'][1]['risetime']
                location.write(time.ctime(over))
        except Exception as e:
            print("Program Exited")
            exit(1)

