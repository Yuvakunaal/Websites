from flask import Flask, render_template, redirect, request
from db import Vendor
from db import vendorTablesCreate
from db import createVendor
from db import updateVendor
from db import deleteVendor
from db import searchVendor
from db import readAllVendors
from db import readVendorById

vendorTablesCreate()
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('index.html',menu='Search')
    elif request.method == "POST":
        name = request.form["name"]
        location = request.form["location"]
        type = request.form["type"]
        rating = request.form["rating"]
        vendors = searchVendor(name,location,type,rating)
        for i in range(len(vendors)):
            vendors[i].SNO = i+1
        return render_template('list.html',vendors=vendors,menu='All')

@app.route("/create",methods=["GET","POST"])
def create_vendor():
    vendor = Vendor()
    if request.method == "POST":
        vendor.name = request.form["name"]
        vendor.location = request.form["location"]
        vendor.type = request.form["type"]
        vendor.rating = request.form["rating"]
        createVendor(vendor)
        return redirect('/list')
    elif request.method == "GET":
        return render_template('create.html',menu='New')

@app.route("/list",methods=["GET"])
def list_vendors():
    vendors = readAllVendors()
    for i in range(len(vendors)):
        vendors[i].SNO = i+1
    return render_template('list.html',vendors=vendors,menu='All')

@app.route("/list/view/<id>",methods=["GET"])
def view_vendors(id):
    vendor = readVendorById(id)
    return render_template('view.html',vendor=vendor,menu='All')

@app.route("/list/edit/<id>",methods=["GET","POST"])
def edit_vendors(id):
    vendor = readVendorById(id)
    if request.method == "GET":
        return render_template('edit.html',vendor=vendor,menu='All')
    elif request.method == "POST":
        vendor.name = request.form["name"]
        vendor.location = request.form["location"]
        vendor.type = request.form["type"]
        vendor.rating = request.form["rating"]
        updateVendor(vendor)
        return redirect('/list')

@app.route("/delete",methods=["POST"])
def delete_vendors():
    if request.method == "POST":
        id = request.form["id"]
        deleteVendor(id)
        return redirect("/list")