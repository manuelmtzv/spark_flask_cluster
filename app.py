from flask import Flask
from pyspark.sql import SparkSession
import uuid

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to my Spark-Flask app!"

@app.route("/run-analysis")
def run_analysis():        
    spark = SparkSession.builder.appName("Flask and Spark: ").master('spark://spark-master:7077').getOrCreate()
    data = [1, 2, 3, 4, 5]
    distData = spark.sparkContext.parallelize(data)
    result = distData.reduce(lambda a, b: a + b)    
    return str(result) + ' is the result of the analysis.'

@app.route('/read-file')
def read_file():
    spark = SparkSession.builder.appName("Flask and Spark: ").master('spark://spark-master:7077').getOrCreate()
    
    try:
        df = spark.read.csv('data/data.csv', header=True, inferSchema=True)
        return df.show()
    except Exception as e:   
        print(e)
        return 'File not found!', 404    

if __name__ == "__main__":    
    app.run(host='0.0.0.0', port=5000, debug=True)
