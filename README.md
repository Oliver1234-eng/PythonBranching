# In this project, the following tasks have been successfully solved:
# 1. Write a function that calculates the earnings of workers. Workers who work more than 40 hours per week are paid 1.5 times more than they would be paid if they worked up to 40 hours per week. The number of working hours per day for a completed workweek is read from a file. The function takes the path to the file with working hours and the hourly wage as parameters and prints the names and earnings of the workers. Example program execution for the file workers.txt: </br> >>> calculateEarnings("workers.txt", 1000) </br> Name: pera </br> Earnings: 61500.0 </br> Name: jova </br> Earnings: 38000 </br> Name: steva </br> Earnings: 40000
# 2. Write a function that takes the number of points on a test and returns the grade for the test. A student can score from 0 to 100 points on the test. The grading is as follows: from 0 to 55 - 5, from 56 to 65 - 6, from 66 to 75 - 7, from 76 to 85 - 8, from 86 to 95 - 9, from 96 to 100 - 10. Example program execution: </br> >>> grade(77) </br> 8 </br> >>> grade(95) </br> 9 </br> >>> grade(96) </br> 10
# 3. Body Mass Index (BMI) is calculated using the formula BMI = m / h^2, where m is weight in kilograms and h is height in meters. The recommended classification of BMI is as follows: < 18.5 Underweight, 18.5 - 25 Normal weight, 25 - 30 Overweight, > 30 Obesity. Write a function that takes weight in kilograms and height and returns the BMI classification category. Example program execution: </br> >>> print(BMIClassification(55, 1.8)) </br> 'Underweight' </br> >>> print(BMIClassification(75, 1.8)) </br> 'Normal weight' </br> >>> print(BMIClassification(81, 1.8)) </br> 'Overweight' </br> >>> print(BMIClassification(120, 1.8)) <br> 'Obesity'
# 4. The penalty for speeding is calculated as 5000 dinars + 500 dinars for each kilometer over the speed limit + 10000 dinars for driving over 120 km/h. Write a function that takes the measured vehicle speed and the speed limit. If the speed is greater than the limit, the function returns a message with the fine amount, and if it is lower, it returns a message that everything is fine. Example program execution: </br> >>> print(speedingFine(80, 60)) </br> Your fine is 15000 dinars </br> >>> print(speedingFine(50, 60)) </br> You did not exceed the speed limit </br> >>> print(speedingFine(130, 60)) </br> Your fine is 50000 dinars
# 5. A babysitter charges 150 dinars per hour for babysitting until 9:00 PM, and 100 dinars per hour for babysitting after 9:00 PM. Write a function that takes the time when the babysitter starts babysitting and when it finishes, and returns a message about the earnings that should be paid. Time is given in the format hh:mm, and it is assumed that babysitting takes place within a 24-hour period. Example program execution: </br> >>> print(babysitter('18:35', '22:50')) </br> The babysitter's earnings are 546 dinars
# 6. The date of Easter in the Gregorian calendar for the years 1982-2048 is calculated by the following formula: a = year % 19; b = year % 4; c = year % 7; d = (19a + 24) % 30; e = (2b + 4c + 6d + 5) % 7. The date of Easter is 22 + d + e March (if the value is greater than 31, then it is April). Write a function that calculates the date of Easter. The function takes the year as a parameter and returns a message with the information about when Easter is if the year is within the specified range, or a message indicating an error if the year is not within the specified range. Example program execution: </br> >>> print(easter(1994)) </br> Easter is on March 29, 1994 </br> >>> print(easter(2011)) </br> Easter is on April 19, 2011 </br> >>> print(easter(1962)) </br> The year is not within the specified range
# 7. The formula for calculating the date of Easter in the Gregorian calendar, as given in the previous task, is valid for all years from 1900 to 2099, except for 1954, 1981, 2049, and 2076. For these years, this formula gives a result that is one week later than it should be. Modify task 6 to make it valid for all years from 1900 to 2099. A year is a leap year if it is divisible by 4, except if it is the last year of a century, in which case it is a leap year if it is divisible by 400 (for example, 1800 and 1900 are not leap years, but 1600 and 2000 are). Write a function that checks if a year is a leap year. Example program execution: </br> >>> print(isLeapYear(1983)) </br> Not a leap year </br> >>> print(isLeapYear(1984)) </br> Leap year </br> >>> print(isLeapYear(1900)) </br> Not a leap year </br> >>> print(isLeapYear(2000)) </br> Leap year
# 8. Write a function that takes a date in the format dd/mm/yyyy and checks if it is a valid date. For example, 24/5/1962 is a valid date, but 31/9/2000 is not valid because September does not have 31 days. Also, take into account whether the year is a leap year.
# 9. Write a program that takes a date in the format dd/mm/yyyy and calculates the ordinal number of the day in the year. The ordinal number of the day in the year is calculated as follows: </br> 1. dayInYear = 31(mm - 1) + dd </br> 2. if mm is after February, subtract (4mm+23)/10 from dayInYear </br> 3. if it's a leap year and mm is after February, add 1 to dayInYear