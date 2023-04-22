import streamlit as st
import pandas as pd
import pymongo
from streamlit import components

# เชื่อมต่อ MongoDB
client = pymongo.MongoClient("mongodb+srv://fishdb:fishdb@cluster0.6jeeb1j.mongodb.net/?retryWrites=true&w=majority")

# เลือก database
db = client["historycount"]

# เลือก collection
collection = db["count"]


# ดึงข้อมูลจาก MongoDB
datatable = list(collection.find())
dataGraph = list(collection.aggregate([
            {"$match": {"$and":[ {"$expr": {"$eq": [{ "$year": "$Date" }, 2023]}}
                                ,{"$expr": {"$eq": [{ "$month": "$Date"}, 4]}}
                                ,{"$expr": {"$eq": [{ "$dayOfMonth": "$Date" }, 20]}}]}}
            ,{"$project":{"_id":0,"count":1,"Date":{"$dateToString":{"format":"%d/%m/%Y %H:%M:%S","date":"$Date"}}}}]))

# แปลงข้อมูลให้อยู่ในรูปแบบ DataFrame ของ pandas
df = pd.DataFrame(datatable)
dfg = pd.DataFrame(dataGraph)
# สร้าง dropdown เพื่อให้ผู้ใช้เลือกจำนวนแถวที่ต้องการแสดง
row_count = st.sidebar.selectbox("แสดงจำนวนแถว", [10, 20, 50, 100, len(df)])

# แสดงข้อมูลในรูปแบบตารางโดยใช้ pandas
st.write(df.head(row_count))

st.line_chart(data=dfg,x="Date",y="count", width=3000, height=400)
st.bar_chart(data=dfg,x="Date",y="count", width=3000, height=400)
st.area_chart(data=dfg,x="Date",y="count", width=3000, height=400)