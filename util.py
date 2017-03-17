# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xlwt
import pymongo
import traceback

try:
  client = pymongo.MongoClient(host='127.0.0.1', port=27017)
  db = client['chongqing']
  house = db['house']
  print(house.count())
except Exception:
  traceback.print_exc()

workbook = xlwt.Workbook(encoding= 'ascii')
worksheet = workbook.add_sheet('Fang')
# write title
titles = ['title', 'city', 'place', 'area', 'average_price', 'longitude', 'latitude', 'all_grade', 'traffic', 'ambitus', 'green']
for x in xrange(0,11):
  worksheet.write(0, x, titles[x])

for index, x in enumerate(house.find()):
  title = x['title'];
  city = x['city']
  place = x['place'];
  area = x['area'];
  average_price = x['average_price']
  longitude = x['lonlat']['longitude']
  latitude = x['lonlat']['latitude']
  if x.has_key('assesses'):
    all_grade = x['assesses']['all_grade']
    if all_grade.decode('utf-8') == u'暂无评分':
      all_grade == '0'
    traffic = x['assesses']['traffic'][:-1]
    ambitus = x['assesses']['ambitus'][:-1]
    green = x['assesses']['green'][:-1]
  for y in range(0, 11):
    if y == 0:
      worksheet.write(index+1, y, label = title)
    elif y == 1:
      worksheet.write(index+1, y, label = city)
    elif y == 2:
      worksheet.write(index+1, y, label = place)
    elif y == 3:
      worksheet.write(index+1, y, label = area)
    elif y == 4:
      worksheet.write(index+1, y, label = average_price)
    elif y == 5:
      worksheet.write(index+1, y, label = longitude)
    elif y == 6:
      worksheet.write(index+1, y, label = latitude)
    elif y == 7:
      if all_grade:
        worksheet.write(index+1, y, label = all_grade)
    elif y == 8:
      if traffic:
        worksheet.write(index+1, y, label = traffic)
    elif y == 9:
      if ambitus:
        worksheet.write(index+1, y, label = ambitus)
    elif y == 10:
      if green:
        worksheet.write(index+1, y, label = green)
    print('write one row')

workbook.save('fang.xls')