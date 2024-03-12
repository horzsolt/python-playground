import pandas as pd
import os

def article_views(views: pd.DataFrame) -> pd.DataFrame:

    """
        1148. Article Views I

        Write a solution to find all the authors that viewed at least one of their own articles.
        Return the result table sorted by id in ascending order.

        Input: 
            Views table:
            +------------+-----------+-----------+------------+
            | article_id | author_id | viewer_id | view_date  |
            +------------+-----------+-----------+------------+
            | 1          | 3         | 5         | 2019-08-01 |
            | 1          | 3         | 6         | 2019-08-02 |
            | 2          | 7         | 7         | 2019-08-01 |
            | 2          | 7         | 6         | 2019-08-02 |
            | 4          | 7         | 1         | 2019-07-22 |
            | 3          | 4         | 4         | 2019-07-21 |
            | 3          | 4         | 4         | 2019-07-21 |
            +------------+-----------+-----------+------------+
        Output: 
            +------+
            | id   |
            +------+
            | 4    |
            | 7    |
            +------+

    """

    merged = views.merge(views, left_on='author_id', right_on='viewer_id', suffixes=['_1','_2'])
    print(merged[['author_id_1', 'viewer_id_2']])

    authour_viewer_same = views[views.author_id == views.viewer_id][['author_id']].rename(columns={'author_id': 'id'})
    return authour_viewer_same.sort_values(by='id').drop_duplicates()

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | id          | int     |
    | name        | varchar |
    +-------------+---------+

    +-------------+------+
    | Column Name | Type |
    +-------------+------+
    | id          | int  |
    | customerId  | int  |
    +-------------+------+

    find all customers who never order anything
    """
    merged = customers.merge(orders, how='left', left_on='id', right_on='customerId', suffixes=['_1','_2'])
    justnull = merged[merged['id_2'].isnull()][['name']]
    justnull.columns = justnull.columns.str.replace('name', 'Customers')
    return justnull
    


def big_countries(world: pd.DataFrame) -> pd.DataFrame:

    """
    | name        | continent | area    | population | gdp         |
    | ----------- | --------- | ------- | ---------- | ----------- |
    | Afghanistan | Asia      | 3000000 | 25500100   | 20343000000 |
    | Albania     | Europe    | 28748   | 25000000   | 12960000000 |
    """

    area_filter = world["area"] > 3000000
    population_filter = world["population"] > 25000000

    return world[area_filter | population_filter][['name', 'population', 'area']]

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:

    """
    | name     | species | age | weight |
    | -------- | ------- | --- | ------ |
    | Tatiana  | Snake   | 98  | 464    |
    | Khaled   | Giraffe | 50  | 41     |
    | Alex     | Leopard | 6   | 328    |
    | Jonathan | Monkey  | 45  | 463    |
    | Stefan   | Bear    | 100 | 50     |
    | Tommy    | Panda   | 26  | 349    |
    """
    
    return animals[animals["weight"] > 100].sort_values(by='weight', ascending=False)[['name']]

"""
animals_json = {"name":{"0":"Tatiana","1":"Khaled","2":"Alex","3":"Jonathan","4":"Stefan","5":"Tommy"},"species":{"0":"Snake","1":"Giraffe","2":"Leopard","3":"Monkey","4":"Bear","5":"Panda"},"age":{"0":98,"1":50,"2":6,"3":45,"4":100,"5":26},"weight":{"0":464,"1":41,"2":328,"3":463,"4":50,"5":349}}
df = pd.DataFrame(animals_json)
print(findHeavyAnimals(df))

world_json = {"name":{"0":"Afghanistan","1":"Albania","2":"Algeria","3":"Andorra","4":"Angola"},"continent":{"0":"Asia","1":"Europe","2":"Africa","3":"Europe","4":"Africa"},"area":{"0":652230,"1":28748,"2":2381741,"3":468,"4":1246700},"population":{"0":25500100,"1":2831741,"2":37100000,"3":78115,"4":20609294},"gdp":{"0":20343000000,"1":12960000000,"2":188681000000,"3":3712000000,"4":100990000000}}
df = pd.DataFrame(world_json)
print(big_countries(df))

"""
#print(os.listdir())
views = pd.read_csv("./pandas/data.csv")
print(article_views(views))