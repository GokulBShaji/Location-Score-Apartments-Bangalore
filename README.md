# Location-Score-Apartments-Bangalore
The Project covers web-scraping, Geocoding and development of location score based on distance from nearest Hospital and nearest Railway Station

## Objective
- Web Scrap Names of Railway Stations.
- Geocode these railway station to get Latitude and Longitude of the same.
- With help of railway stations database made and Hospitals database available from government sourse compute location score.

## Procedure
- Install the following libraries - Selenium,Pandas,Openpyxl
- Install chromedriver [link](https://chromedriver.chromium.org/downloads) and place the chromdriver.exe file in the program folder(LocationScore) here.
- Web-scraping of railway station names are done from [link](https://www.totaltraininfo.com/a.php)
- First Run railwaystations.py file such that, the commented lines are run in pairs i.e line 16 and line 87 make a pair, the comment(16,87) and run(17,88) and so on.
- Then Run the cleaning.py file for removing 'NA's from the last scraped file of a particular letter.This also needs to be run in pairs i.e (line 3, line38) followed by (line 4, line39) and so on
- Then Run the Geocoding.py file. Each of the files obtained in scraping is passed to the code for geocoding i.e z1.xlsx(line 24) is passed to obtain the result z_1.xslx(line 35).
- There are chances of of obtaing error of too many requests while running the Geocoding.py file, but patiently run the code multiple times until output file is obtained for each and every scraped file.
- Then run combine.py file.
- Hospitals.xlsx(Available in dataset.zip of this repository)file is obtained after sufficient preprocessing of the file [link](https://data.gov.in/catalog/all-india-health-centres-directory)
- Location_of_apartments.xlsx(Available in dataset.zip of this repository)file is obtained after sufficient preprocessing of the file [link](https://www.kaggle.com/datasets/galijithendranath/locations-of-apartments-in-bangalore)
- Then run nearest.py file.This file has to be run twice, first commenting lines(28,30,34,39,41) and then for the second time by uncommenting the above mentioned lines and commenting the following 
  lines(29,31,35,40,42).
- Then run Location_Score.py file and the final output with location score is obtained the excel file Location_of_apartments.xlsx.

## Location Score formula
- location score and distance from nearest railway station or Hospital are inversely proportional i.e A location near to Hospital and Raailway station have higher value compared to a location far away.
- Higher priority is given to Nearest Hospital than Nearest Railway station
- Hence Location Score is given a random equation aligning towards the above assumptions i.e Location Score = 1000 * ((1/(distance to nearest railway station)) + (2/(distance to nearest hospital)))
