
Summary:

While there is still a global food need, the World Food Program (WFP) has been struggling to keep up, partially due to rising food prices. My goal is to prove that price of the commodities used by the WFP has increased rapidly within a short amount of time across two different countries over the past couple of years.To show this, I am using food prices data from Uganda that goes back more than 10 years and and data from Sri Lanka that goes back more than 15 years. The original data is extremely long and detailed which makes it hard for us to analyze.To simplify analyzing the data, I filtered it to only show and graph the rapidly changed prices of random goods. This code can be used to test out the changed prices for other commodities in Uganda and Sri Lanka other than the ones we are showing. Additionally, with the right alteration, the same code could also be used for other countries where the World Food Program is present.

Input Data:

The data used from Uganda goes as far back as 2006 and the Sri Lankan data goes back to 2004 and each contains everything distributed by WFP including beans, oil, rice, sugar, flour, maize etc. It contains a lot of additional information that is not relevant to this project and may not mean much to someone who isn't familiar with food distribution. It is important to note that the prices are in the local currency of the both countries. For Uganda, the currency is Ugandan Shilling and for Sri Lanka, the rupee. With the current code, the graph gives us the information we need to determine the difference in price with the same commodity over a certain period of time. The Uganda data can be dowloaded from:https://data.humdata.org/dataset/wfp-food-prices-for-uganda and Sri Lanka: https://data.humdata.org/dataset/wfp-food-prices-for-sri-lanka. This website has very recent food price data from countries where the World Food Program is present.

Deliverables:

There are five deliverables: three python script that is called 'Beans-Uganda.py, Maize-Uganda.py and Sugar-sri Lanka.py',one README.md file that discusses the project, one relult.md file that briefly explains the results. Also, the country data used have also been included for convenience.

Instruction:

1. Import pandas and matplotlib.pyplot (for plotting).

2. Set file_data to the result of calling pd.read_csv() to read 'wfp_food_prices_uganda.csv and wfp_food_prices_sri-lanka.csv'.

3. print (file_data.head())

4. Remove the first row since it contains values irrelevant to this project.

5. The datas include a lot of information so filter out the commodities and markets that you would like displayed on the graph.

6. Display the top 5 rows of the filtered commodity data.

7. Print out the length of the filtered data we have.

8. Start plotting the graph.
