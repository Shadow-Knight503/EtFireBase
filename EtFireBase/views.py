from django.shortcuts import render
import pyrebase
from collections import OrderedDict

config = {
    "apiKey": "AIzaSyCR09EzSIGaIho5COhhDsrOFqooR3_5HeM",
    "authDomain": "fir-study-cc65b.firebaseapp.com",
    "databaseURL": "https://fir-study-cc65b-default-rtdb.firebaseio.com",
    "storageBucket": "fir-study-cc65b.appspot.com",

}
Firebase = pyrebase.initialize_app(config)
Auth = Firebase.auth()
DataBase = Firebase.database()


def Home(request):
    data = {}
    weeks = DataBase.child("Companies").child("DemoComp").child("Weeks").child("03-09-2022").get()
    for week in weeks.each():
        data[week.key()] = week.val()
    ctx = {
        "data": data,
    }
    return render(request, "Home.html", ctx)
