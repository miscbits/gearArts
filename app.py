from flask import Flask, render_template, flash, redirect, url_for, request, make_response, json

app = create_app()


@app.route('/')
def index():
	return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
	return render_template('index.html')


app.run()
