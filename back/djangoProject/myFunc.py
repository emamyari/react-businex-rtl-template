import json
from time import sleep

import pyodbc as pyodbc
from rest_framework.decorators import api_view
import requests
from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import gaming, maping


def getConnection():
    connection = pyodbc.connect(
        'DRIVER={ODBC DRIVER 17 FOR SQL SERVER};Server=192.168.1.36;Database=emamyari;Port=1433;UID=sa;PWD=111')
    cursor = connection.cursor()
    return connection, cursor


@api_view(['GET', 'POST'])
def connect2(request):
    obj1 = maping()

    if request.method == 'POST':
        obj1.name = request.data['loginName']

        obj1.save()
    return render(request, 'register.html')


def getData(request):
    data = [{'id': 1, 'name': 'iphone', 'q': 10, 'color': 'red'},
            {'id': 2, 'name': 'airPod', 'q': 5, 'color': 'yellow'},
            {'id': 3, 'name': 'TV', 'q': 100, 'color': 'pink'},
            {'id': 4, 'name': 'adaptor', 'q': 5, 'color': 'white'},
            ]
    return HttpResponse(json.dumps(data), content_type='application/json')


def getaddress(request):
    data = [{'id': 1, 'title': 'مغازه', 'value': 'زنجان خیابان صفا پلاک 86'},
            {'id': 2, 'title': 'خانه', 'value': 'زنجان سعدی شمالی کوچه خادم پلاک 10'},
            ]
    return HttpResponse(json.dumps(data), content_type='application/json')


def getHistory(request):
    data = [{'id': 1, 'date': '1399/02/06', 'value': 'یرالما'},
            {'id': 2, 'date': '1401/05/26', 'value': 'سوغان'},
            ]
    return HttpResponse(json.dumps(data), content_type='application/json')


def getChartData(request):
    data = {'cat': ['1399-03-03', '1400-09-01', '1401-06-06', '1402-01-02', '1403-11-12', '1404-0402', '1405-08-09',
                    '1406-05-09']
        , 'data': [1000, 2000, 2500, 1500, 500, 900, 1400, 2150]}
    return HttpResponse(json.dumps(data), content_type='application/json')


def home(request):
    a = requests.get('http://parsianlotusfund.ir/data/nav').text
    d = json.loads(a)
    return render(request, 'test.html', context=d)


def aboutData(request):
    par = request.GET['name']
    connection, cursor = getConnection()

    cursor.execute("select * from foods where Name=?", par)
    rows = cursor.fetchall()
    print(rows)
    myList = []
    for item in rows:
        dict = {'id': item[0],
                'name': item[1],
                'price': item[2],
                'desc': item[3],
                'type': item[4]}
        myList.append(dict)
    data = {'foods': myList}
    return render(request, 'test.html', context=data)


def deleteData(request):
    par = request.GET['name']
    connection, cursor = getConnection()

    cursor.execute("delete from foods where Name=?", par)
    cursor.commit()
    return render(request, 'test.html')


def insertData(request):
    par1 = request.GET['name']
    par2 = request.GET['price']
    par3 = request.GET['type']
    connection, cursor = getConnection()

    cursor.execute("insert into foods (Name,Price,Type)values(?,?,?)", par1, par2, par3)
    cursor.commit()
    return render(request, 'test.html')


@api_view(['POST'])
def inData(request):
    print('---------------------------------')
    print(request.data)
    par1 = request.data['email']
    par2 = request.data['family']

    connection, cursor = getConnection()

    cursor.execute("insert into foods (Name,Description)values(?,?)", par1, par2)
    cursor.commit()
    return HttpResponse(json.dumps('ok'))


def basketData(request):
    a = [{'id': 1, 'title': 'iphone', 'qyt': 5, 'color': 'white', 'unitPrice': 100},
         {'id': 2, 'title': 'mac book', 'qyt': 0, 'color': 'gray', 'unitPrice': 90},
         {'id': 3, 'title': 'mac book', 'qyt': 0, 'color': 'gray', 'unitPrice': 90},
         {'id': 4, 'title': 'mac book', 'qyt': 0, 'color': 'gray', 'unitPrice': 90},
         {'id': 5, 'title': 'desk', 'qyt': 1, 'color': 'black', 'unitPrice': 70}, ]
    return HttpResponse(json.dumps(a), content_type='application/json')


@api_view(['POST'])
def inDataContract(request):
    print(request.data)
    par1 = request.data['Name']
    par2 = request.data['Family']
    par3 = request.data['Email']
    par4 = request.data['Tel']
    par5 = request.data['Text']
    par6 = request.data['File']

    connection, cursor = getConnection()

    cursor.execute("insert into Contact (Name,Family,Email,Tel,Text,FileContent)values(?,?,?,?,?,?)", par1, par2, par3,
                   par4, par5, par6)
    cursor.commit()
    return HttpResponse(json.dumps('ok'))


@api_view(['GET'])
def getServices(request):
    a = [{
        "id": 1,
        "title": "ایده های خلاقانه",
        "shortDesc": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
        "thumb": "service/01.jpg",
        "previewImages": [
            "service/details/01.jpg",
            "service/details/02.jpg",
            "service/details/03.jpg"
        ],
        "aboutServiceDesc": "<p>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.</p>",
        "features": [
            "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 1",
            "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 2"
        ]
    },
        {
            "id": 2,
            "title": "ایده های خلاقانه",
            "shortDesc": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "thumb": "service/01.jpg",
            "previewImages": [
                "service/details/01.jpg",
                "service/details/02.jpg",
                "service/details/03.jpg"
            ],
            "aboutServiceDesc": "<p>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.</p>",
            "features": [
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 1",
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 2"
            ]
        },
        {
            "id": 3,
            "title": "ایده های خلاقانه",
            "shortDesc": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "thumb": "service/01.jpg",
            "previewImages": [
                "service/details/01.jpg",
                "service/details/02.jpg",
                "service/details/03.jpg"
            ],
            "aboutServiceDesc": "<p>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.</p>",
            "features": [
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 1",
                "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم 2"
            ]
        }]

    return HttpResponse(json.dumps(a), content_type='application/json')


@api_view(['GET'])
def getSlider(request):
    a = [
        {
            "id": 1,
            "title": "امام یاری",
            "text": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "bg": "slider/h-2-01.jpg",
            "btnText": "اطلاعات کمتر",
            "btnLink": "/about"
        },
        {
            "id": 2,
            "title": "پول خود را هدر ندهید",
            "text": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "bg": "slider/h-2-02.jpg",
            "btnText": "اطلاعات بیشتر",
            "btnLink": "/about"
        }, {
            "id": 1,
            "title": "قالب ری اکت شرکتی",
            "text": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "bg": "slider/h-2-01.jpg",
            "btnText": "اطلاعات بیشتر",
            "btnLink": "/about"
        },
        {
            "id": 2,
            "title": "پول خود را هدر ندهید",
            "text": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.",
            "bg": "slider/h-2-02.jpg",
            "btnText": "اطلاعات بیشتر",
            "btnLink": "/about"
        }
    ]

    return HttpResponse(json.dumps(a), content_type='application/json')



@api_view(['GET'])
def getFunfact(request):
    a = [
            {
                "id": 1,
                "counterNumber": 1000,
                "counterText": "مشتری راضی"
            },
            {
                "id": 2,
                "counterNumber": 2000,
                "counterText": "پروژه انجام شده"
            },
            {
                "id": 3,
                "counterNumber": 3000,
                "counterText": "جایزه"
            },
            {
                "id": 4,
                "counterNumber": 4000,
                "counterText": "فنجان قهوه :)"
            }
        ]

    return HttpResponse(json.dumps(a), content_type='application/json')




@api_view(['GET'])
def getMenu(request):
    a = [

            {
                "id": 1,
                "title": "کاشانه",
                "link": "/",
                "megaMenu": False,
                "subMenu": [
                    {
                        "id": 1.1,
                        "title": "خانه 1",
                        "link": "/home-one"
                    },
                    {
                        "id": 1.2,
                        "title": "خانه 2",
                        "link": "/home-two"
                    }
                ]
            },
            {
                "id": 2,
                "title": "درباره",
                "link": "/about",
                "megaMenu": False,
                "subMenu": False
            },
            {
                "id": 3,
                "title": "خدمات",
                "link": "/services",
                "megaMenu": False,
                "subMenu": False
            },
            {
                "id": 4,
                "title": "تیم",
                "link": "/team",
                "megaMenu": False,
                "subMenu": False
            },
            {
                "id": 5,
                "title": "وبلاگ",
                "link": "/blog-grid-right-sidebar",
                "megaMenu": False,
                "subMenu": [
                    {
                        "title": "وبلاگ شبکه ای با ستون راست",
                        "link": "/blog-grid-left-sidebar"
                    },
                    {
                        "title": "وبلاگ شبکه ای با ستون چپ",
                        "link": "/blog-grid-right-sidebar"
                    },
                    {
                        "title": "وبلاگ شبکه ای بدون ستون",
                        "link": "/blog-grid-without-sidebar"
                    },
                    {
                        "title": "وبلاگ فهرستی با ستون راست",
                        "link": "/blog-list-left-sidebar"
                    },
                    {
                        "title": "وبلاگ فهرستی با ستون چپ",
                        "link": "/blog-list-right-sidebar"
                    },
                    {
                        "title": "جزئیات وبلاگ",
                        "link": "/blog/wild-life-workshop?id=14"
                    }
                ]
            },
            {
                "id": 6,
                "title": "تماس",
                "link": "/contact"
            }
        ]



    return HttpResponse(json.dumps(a), content_type='application/json')



@api_view(['GET'])
def getAbout(request):
    a =  {
  "title": "درباره ما",
  "heading": "ما بهترین کیک را برای شما پخت می کنیم",
  "since": "از سال 1391",
  "text": "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.",
  "btnText": "اطلاعات بیشتر",
  "btnLink": "/about",
  "thumb": "fun-fact-bg.jpg"
}




    return HttpResponse(json.dumps(a), content_type='application/json')


