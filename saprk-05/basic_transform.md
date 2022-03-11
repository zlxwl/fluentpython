df = spark.read.format('json').load('data/flight-data/json/2015-summary.json')
df.printSchema()

from pyspark.sql.types import StructField, StructType, StringType, LongType
myManualSchema = StructType([StructField('DEST_COUNTRY_NAME', StringType(), True), StructField('ORIGIN_COUNTRY_NAME', StringType(), True), StructField('count', LongType(), False, metadata={'hello': 'world'})])
df = spark.read.format('json').schema(myManualSchema).load('data/flight-data/json/2015-summary.json')

# column
from pyspark.sql.functions import col, column
expr('(((someCol + 5 ) * 200 ) - 6 ) < otherCol')
spark.read.format('json').schema(myManualSchema).load('data/flight-data/json/2015-summary.json').columns


# Row
- 1.create
from pyspark.sql import Row
>>>my_row = Row('Hello', None, 1, False)

# DataFrame
df = spark.read.format('json').load('data/flight-data/json/2015-summary.json')
df.createOrReplaceTempView('dfTable')

from pyspark.sql import Row
from pyspark.sql.types import StructType, StructField, StringType, LongType
myManualSchema = StructType(
    [StructField('some', StringType(), True),
    StructField('col', StringType(), True),
    StructField('names', LongType(), False)]
)
myRow = Row('Hello', None, 1)
mdDf = spark.createDataFrame([myRow], myManualSchema)
mdDf.show()

# select selectExpr
df.select('DEST_COUNTRY_NAME').show()
select DEST_COUNTRY_NAME from dfTable limit 2

>>> df.select(expr('DEST_COUNTRY_NAME'), col('DEST_COUNTRY_NAME'), column('DEST_COUNTRY_NAME'))

- alias
df.select(expr('DEST_COUNTRY_NAME as destination')).show(2)
select DEST_COUNTRY_NAME as destinations from dfTable limit 2

df.select(expr('DEST_COUNTRY_NAME as destination').alias('DEST_COUNTRY_NAME')).show(2)

- selectExpr
df.selectExpr('DEST_COUNTRY_NAME as destination', 'DEST_COUNTRY_NAME').show(2)
df.selectExpr('*', '(DEST_COUNTRY_NAME=ORIGIN_COUNTRY_NAME) as withCountry').show(2)

select *, (DEST_COUNTRY_NAME=ORIGIN_COUNTRY_NAME) as withCountry from dfTable limit 2

df.selectExpr('avg(count)', 'count(distinct(DEST_COUNTRY_NAME))').show(2)
select avg(count), count(distinct(DEST_COUNTRY_NAME)) from dfTable


# lit transform to spark type
from pyspark.sql.functions import lit
df.select(expr('*'), lit(1).alias('one')).show(2)
select *, 1 as one from dfTable limit 2

# add column
df.withColumn('numberOne', lit(1)).show(2)
select *, 1 as numberOne from dfTable
df.withColumn('withinCountry', expr('DEST_COUNTRY_NAME==ORIGIN_COUNTRY_NAME')).show(2)

- rename
df.withColumn('Destination', expr('DEST_COUNTRY_NAME')).columns

# withColumnRenamed
df.withColumnRenamed('DEST_COUNTRY_NAME', 'dest').show(2)

# keyword
dfWithLongColName = df.withColumn('This Long Column-Name', expr('ORIGIN_COUNTRY_NAME'))
dfWithLongColName.selectExpr('`This Long Column-Name`', '`This Long Column-Name` as `new col`').show(2)
dfWithLongColName.createOrReplaceTempView('dfTableLone')
select `This Long Column-Name`,  `This Long Column-Name` as `new col` from dfTableLong limit 2
dfWithLongColName.select(expr('`This Long Column-Name`')).columns

# set 
set spark.sql.caseSensitive true

# drop columns
df.drop('ORIGIN_COUNTRY_NAMES').columns
dfWithLongColName.drop('ORIGIN_COUNTRY_NAMES', 'DEST_COUNTRY_NAMES')

# change type
df.withColumn('count2', col('count').cast('long'))

# where and filter
df.where('count < 2').show(2)
df.filter(col('count') < 2).show(2)

df.where(col('count') < 2).where(col('ORIGIN_COUNTRY_NAME') != 'Croatia').show(2)
select count, ORIGIN_COUNTRY_NAME from dfTable where count < 2 and ORIGIN_COUNTRY_NAME != 'Croatia' limit 2

# filter duplicate row: count(), distinct()
df.select('ORIGIN_COUNTRY_NAME', 'DEST_COUNTRY_NAME').distinct().count()
select count(distinct(ORIGIN_COUNTRY_NAME, DEST_COUNTRY_NAME)) from dfTable

# random sample
seed = 5
withReplacement = False
fraction = 0.5
df.sample(withReplacement, fraction, seed).count()

dataFrame = df.randomSplit([0.75, 0.25], seed)
train_df = dataFrame[0]
test_df = dataFrame[1]

# Union add Row must have same column and name
from pyspark.sql import Row
schema = df.schema
newRows = [Row('New Country', 'Other Country', 5), Row('New Country 2', 'Other Country 2', 1)]
parallelizedRows = spark.sparkContext.parallelize(newRows)
newDF = spark.createDataFrame(parallelizedRows, schema)
temp_df = df.union(newDF).where('count=1').where(col('ORIGIN_COUNTRY_NAME') != 'United States').show()
temp_df.createOrReplacTempView('tempUnionTable')


# sort row -- orderBy()  
from pyspark.sql.functions import desc, asc
df.sort('count').show(5)
df.orderBy(col('count'), col('DEST_COUNTRY_NAME')).show(5)
df.orderBy(col('count').desc(), col('DEST_COUNTRY_NAME).asc()).show(5)

select count, DEST_COUNTRY_NAME from dfTable limit 5 

# partitions
df.rdd.getNumPartitions()
df.repartition(5)

df.repartition(5, col('DEST_COUNTRY_NAME')).coalesce(2)


# driver obtain row 
collectDF = df.limit(10)
collectDF = df.take(3)
collectDF.show()
collectDF.collect()
collectDF.toLocalIterator()