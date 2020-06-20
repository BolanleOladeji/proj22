#Covid-19 Information Platform
#Bolanle Oladeji and Ruisha Prasai
#CS-10001
#Summary
#The number of COVID-19 cases in the world is rising with every passing moment.
#We wanted users to be able to have easy access to up-to-date information on the number of COVID-19 cases in their location.
#We used the knowledge of the parsing of HTML files and the input function to generate the output needed.
#The statistics were gotten from the website “Our World In Data” which lists all the countries and the corresponding statistics.
 


import pandas as pd
#use panda to store and manipulate data using dataframe
data = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
# get data through panda
df = pd.DataFrame(data, columns=["iso_code", "location", "date", "total_cases", "new_cases","total_deaths", "new_deaths", "total_cases_per_million",  "new_cases_per_million", "total_deaths_per_million" ,"new_deaths_per_million", "total_tests new_tests", "total_tests_per_thousand", "new_tests_per_thousand",  "tests_units" ])
# takes csv and converts in dataframe
covid2nd= df[["location", "date", "total_cases", "total_deaths"]]
# be able to ascess 1,2,3,4 columns in dataframe we created


# create list of countries
countries3=['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua & Deps','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin', 'Bhutan',\
'Bolivia',\
'Bosnia Herzegovina',\
'Botswana',\
'Brazil',\
'Brunei',\
'Bulgaria',\
'Burkina',\
'Burundi',\
'Cambodia',\
'Cameroon',\
'Canada',\
'Cape Verde',\
'Central African Rep',\
'Chad',\
'Chile',\
'China',\
'Colombia',\
'Comoros',\
'Congo',\
'Congo {Democratic Rep}',\
'Costa Rica',\
'Croatia',\
'Cuba',\
'Cyprus',\
'Czech Republic',\
'Denmark','Djibouti','Dominica','Dominican Republic','East Timor','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia',\
'Ethiopia','Fiji','Finland','France','Gabon','Gambia','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea',\
'Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland {Republic}','Israel','Italy','Ivory Coast','Jamaica','Japan','Jordan','Kazakhstan',\
'Kenya','Kiribati','North Korea','South Korea','Kosovo','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya',\
'Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco',\
'Mongolia','Montenegro','Morocco','Mozambique','Myanmar, {Burma}','Namibia','Nauru','Nepal','Netherlands','New Zealand',\
'Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russian Federation','Rwanda','St Kitts & Nevis','St Lucia',\
'Saint Vincent & the Grenadines','Samoa','San Marino',\
'Sao Tome & Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia',\
'Slovenia','Solomon Islands','Somalia','South Africa','South Sudan','Spain','Sri Lanka','Sudan','Suriname',\
'Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand',\
'Togo','Tonga','Trinidad & Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom',\
'United States', "USA", 'Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe']

country = input('Insert a country: ')
# use input function to insert the country user want to know infromation about
if country not in countries3:
    print('Error. Country not found. Please run code again and try alternative spelling or form.')
    
else:
    print('Country found.  {}'.format(country))
    print("Please wait a moment as results are being gathered...")
    Cases = covid2nd.loc[covid2nd["location"] == country]
    #.loc locates location from the columns in data frame
    print(pd.concat([Cases.tail(1)]))
#     to get latest data from latest date, we use .tail function
    print("                           ")
    print("Stay safe in this period. You can get more information on the WHO and CDC websites.")
    print("With love from Ruisha and Bolanle.")
# Thank you!

#Source for pandas dataframe:
#https://stackoverflow.com/questions/16283799/how-to-read-a-csv-file-from-a-url-with-python
