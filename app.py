from flask import Flask, render_template, flash, redirect, url_for, request, make_response, json

def create_app():
	app = Flask(__name__)
	app.secret_key = "lL882eTTDIetmdJGDuQhUnurAee6GNCTfqw2CjtWolKRH8uh9oct8qOG9veFr7kq5UzuGKRdCig3DhP4fuGRmhZQgUwIu2LzeHMSzLxKknlZMreiKLri696pqmjCxv8tdJJoI23xQUIGmFgOSnFVf1REirCRZGxXg7AGCTnWRghbHlDCPyFxAQGZdwl5dlkFVhB1C98rh9Rm1PjECyq5jJybt7SyZT47XQKRE1Wr0h1jmoSFoKwc2OdcL6d5bn5uTuTnLyeu77IMHvKwDIaFLed3Uy8sSO5E8Zix99WaE9VS"
	return app

app = create_app()

@app.route('/')
def index():
	return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
	return render_template('index.html')


app.run()
