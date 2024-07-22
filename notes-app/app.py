from flask import Flask,render_template, redirect, request
from db import noteTablesCreate
from db import Note
from db import readAllNotes
from db import readNoteById
from db import updateNote
from db import createNote
from db import deleteNote
from db import searchNote

noteTablesCreate()
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('index.html',menu='Search')
    elif request.method == "POST":
        title = request.form["title"]
        notes_text = request.form["notes"]
        notes = searchNote(title,notes_text)
        for i in range(len(notes)):
            notes[i].SNO = i+1
        return render_template('list.html',notes=notes,menu='All')

@app.route("/create",methods=["GET","POST"])
def create_notes():
    note = Note()
    if request.method == "POST":
        note.title = request.form["title"]
        note.notes = request.form["notes"]
        createNote(note)
        return redirect('/list')
    elif request.method == "GET":
        return render_template('create.html',menu='New')

@app.route("/list",methods=["GET"])
def list_notes():
    notes = readAllNotes()
    for i in range(len(notes)):
        notes[i].SNO = i+1
    return render_template('list.html',notes=notes,menu='All')

@app.route("/list/view/<id>",methods=["GET"])
def view_notes(id):
    note = readNoteById(id)
    return render_template('view.html',note=note,menu='All')

@app.route("/list/edit/<id>",methods=["GET","POST"])
def edit_notes(id):
    note = readNoteById(id)
    if request.method == "GET":
        return render_template('edit.html',note=note,menu='All')
    elif request.method == "POST":
        note.title = request.form["title"]
        note.notes = request.form["notes"]
        updateNote(note)
        return redirect('/list')

@app.route("/delete",methods=["POST"])
def delete_notes():
    if request.method == "POST":
        id = request.form["id"]
        deleteNote(id)
        return redirect("/list")