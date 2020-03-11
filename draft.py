import pandas as pd
import matplotlib.pyplot as plt


df_cal = pd.read_csv('./boston/calendar.csv')
df_cal["price"] = df_cal["price"].apply(lambda x: str(x).replace("$", ""))
df_cal["price"] = pd.to_numeric(df_cal["price"] , errors="coerce")


plt.plot(df_cal['date'], df_cal['price'])
plt.show()
df_cal = df_cal[df_cal.columns['price']].replace('[\$,]', '', regex=True).astype(float)
df_listings = pd.read_csv('./boston/listings.csv')
df_reviews = pd.read_csv('./boston/reviews.csv')
print(df_listings.columns)
print(df_listings[['id', 'last_scraped', 'price']])
print(df_cal)
