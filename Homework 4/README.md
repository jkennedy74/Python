
# Heroes of Pymoli Analysis


```python
import json
import pandas as pd
import numpy as np

```


```python
df = pd.read_json('../Resources/purchase_data.json') 


df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>



## Player Count


```python
player_count = df["SN"].nunique()
print("Player Count:  " + str(player_count))

```

    Player Count:  573
    

## Purchasing Analysis (Total)


```python
# Number of Unique Items
items = df["Item ID"].nunique()

# Average Purchase Price
avg_pp = "{:.2f}".format(df["Price"].mean())

# Total Number of Purchases
total_purchases = df["SN"].count()

# Total Revenue
total_revenue = df["Price"].sum()

```


```python

print("Unique Items:  " + str(items))
print("Average Purchase Price:  " + str(avg_pp))
print("Total Purchases:  " + str(total_purchases))
print("Total Revenue:  " + str(total_revenue))

```

    Unique Items:  183
    Average Purchase Price:  2.93
    Total Purchases:  780
    Total Revenue:  2286.33
    

## Gender Demographics


```python
gender_count = df.groupby('Gender', as_index = True)['SN'].nunique()

# Percentage and Count of Male Players
m = gender_count.loc["Male"]
pm ="{:.2%}".format(m/player_count)

# Percentage and Count of Female Players
f = gender_count.loc["Female"]
fm ="{:.2%}".format(f/player_count)

# Percentage and Count of Other / Non-Disclosed
o = gender_count.loc['Other / Non-Disclosed']
om ="{:.2%}".format(o/player_count)


```


```python
print(str(m) + " male players made up " + str(pm) + " of all players")
print(str(f) + " female players made up " + str(fm) + " of all players")
print(str(o) + " other/non-disclosed players made up " + str(om) + " of all players")
```

    465 male players made up 81.15% of all players
    100 female players made up 17.45% of all players
    8 other/non-disclosed players made up 1.40% of all players
    

## Purchasing Analysis (Gender)



```python
# Purchase Count

pc = df.groupby('Gender', as_index = True)['Item ID'].nunique()
pc = pc.to_frame()

# Average Purchase Price
avp = df.groupby('Gender', as_index = True)['Price'].mean()
avp = avp.to_frame()

# Total Purchase Value
tvp = df.groupby('Gender', as_index = True)['Price'].sum()
tvp = tvp.to_frame()


gender_df = pc.merge(avp, left_index =True,right_index=True)
gender_df = gender_df.merge(tvp, left_index =True,right_index=True)
gender_df = gender_df.rename(index=str, columns={"Item ID": "Total Purchased", "Price_x": "Average Price", "Price_y": "Total Price"})
gender_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchased</th>
      <th>Average Price</th>
      <th>Total Price</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>96</td>
      <td>2.815515</td>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>180</td>
      <td>2.950521</td>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>3.249091</td>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>



## Age Demographics


The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.) 


Purchase Count
Average Purchase Price
Total Purchase Value
Normalized Totals


```python
bins = [0, 9, 14, 19, 24, 29, 34, 39, 44]

group_names = ['<10', '10-14', '15-19', '20-24','25-29' , '30-34', '35-39','>40' ] 


df["Age Range"]=pd.cut(df["Age"], bins, labels=group_names)

```


```python
age_pc = df.groupby('Age Range', as_index = True)['Item ID'].nunique()
age_app = df.groupby('Age Range', as_index = True)['Price'].mean()
age_tpv = df.groupby('Age Range', as_index = True)['Price'].sum()

age_pc = age_pc.to_frame()
age_app = age_app.to_frame()
age_tpv = age_tpv.to_frame()


```


```python
age_df = age_pc.merge(age_app, left_index =True,right_index=True)
age_df = age_df.merge(age_tpv, left_index =True,right_index=True)
age_df = age_df.rename(index=str, columns={"Item ID": "Total Purchased", "Price_x": "Average Price", "Price_y": "Total Price"})
age_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchased</th>
      <th>Average Price</th>
      <th>Total Price</th>
    </tr>
    <tr>
      <th>Age Range</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>24</td>
      <td>2.980714</td>
      <td>83.46</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>32</td>
      <td>2.770000</td>
      <td>96.95</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>91</td>
      <td>2.905414</td>
      <td>386.42</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>158</td>
      <td>2.913006</td>
      <td>978.77</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>89</td>
      <td>2.962640</td>
      <td>370.33</td>
    </tr>
  </tbody>
</table>
</div>



## Top Spenders


```python
spender_df = df.groupby('SN')['Price'].sum()
spender_df = spender_df.to_frame()
spender_df["Purchase Count"] = df.groupby('SN')["Item ID"].count()
spender_df["Average Price"] = df.groupby('SN')["Price"].mean()
spender_df["Total Price"] = df.groupby('SN')["Price"].sum()

```

### Top Spenders


```python
spender_df.nlargest(5, "Price")

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
      <th>Purchase Count</th>
      <th>Average Price</th>
      <th>Total Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>17.06</td>
      <td>5</td>
      <td>3.412000</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>13.56</td>
      <td>4</td>
      <td>3.390000</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>12.74</td>
      <td>4</td>
      <td>3.185000</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>12.73</td>
      <td>3</td>
      <td>4.243333</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>11.58</td>
      <td>3</td>
      <td>3.860000</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>



## Most Popular Items

### Most Popular by Purchase Count


```python
popular_df = df.groupby('Item ID')['Price'].max()
popular_df = popular_df.to_frame()
popular_df["Item Name"] = df["Item Name"]
popular_df["Purchase Count"] = df.groupby('Item ID')["Item ID"].count()
popular_df["Total Price"] = df.groupby('Item ID')["Price"].sum()

popular_df.nlargest(5, "Purchase Count")

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Total Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>2.35</td>
      <td>Stormfury Mace</td>
      <td>11</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <td>2.23</td>
      <td>Thorn, Satchel of Dark Souls</td>
      <td>11</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.49</td>
      <td>Piety, Guardian of Riddles</td>
      <td>9</td>
      <td>13.41</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2.07</td>
      <td>Shadow Strike, Glory of Ending Hope</td>
      <td>9</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>34</th>
      <td>4.14</td>
      <td>Alpha, Reach of Ending Hope</td>
      <td>9</td>
      <td>37.26</td>
    </tr>
  </tbody>
</table>
</div>



### Most Popular by Total Price


```python
popular_df.nlargest(5, "Total Price")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Total Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>4.14</td>
      <td>Alpha, Reach of Ending Hope</td>
      <td>9</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>4.25</td>
      <td>Thorn, Conqueror of the Corrupted</td>
      <td>7</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>4.95</td>
      <td>Rage, Legacy of the Lone Victor</td>
      <td>6</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>4.87</td>
      <td>Mercy, Katana of Dismay</td>
      <td>6</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>3.61</td>
      <td>Spectral Diamond Doomblade</td>
      <td>8</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>



## Incites from Analysis

1 - More men buy items in Pymoli than women.
2 - However this could be skewed by the fact that there are more male players.  
3 - The largest slice in the age demographic by total purchases and price are people between 20-24
