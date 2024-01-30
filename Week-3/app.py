from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello():
    myname = request.cookies.get('my_name')
    return render_template('greet.html', name=myname)


@app.route('/greet', methods=['POST'])
def greet():
    name = request.form["name"]
    return render_template('greet.html', name=name)


@app.route('/trackName', methods=['GET'])
def track_name():
    name = request.args.get('name')
    response = make_response(redirect(url_for('my_name')))
    response.set_cookie('my_name', name)
    return response

@app.route('/sum.html')
def sum():
    return app.send_static_file('sum.html')


@app.route('/data', methods=['GET', 'POST'])
def data():
    number = request.args.get('number')  # to retrieve data from URL
    if number is None:
        return 'Lack of Parameter'

    if number.isdigit():  # to check if the number is an integer
        number = int(number)
        return render_template('data.html', number=number)
    else:
        return "Wrong Parameter"


@app.route('/myname', methods=['POST'])
def myname():
    name = request.form["name"]  # to retrieve data from the form
    response = make_response(f'HiHi, {name}!')
    response.set_cookie('my_name', name)
    return response


@app.route('/myName')
def my_name():
    input_name = request.cookies.get('my_name', 'World')
    return render_template('myname.html', name=input_name)


@app.route('/delete')
def delete():
    response = make_response(f'Ciao!')
    response.set_cookie('my_name', '')
    return response


if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)
