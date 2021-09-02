from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def main():
    return render_template('calc_main.html')


@app.route('/calc/<int:x>/<int:y>/div')
def calc_div(x, y):
    if y ==0:
        return render_template('error.html')
    else:
        return render_template('calc.html', x=x, sign='/', y=y, res=x/y)


@app.route('/calc/<int:x>/<int:y>/sum')
def calc_sum(x, y):
    return render_template('calc.html', x=x, sign='+', y=y, res=x+y)


@app.route('/calc/<int:x>/<int:y>/dif')
def calc_dif(x, y):
    return render_template('calc.html', x=x, sign='-', y=y, res=x-y)


@app.route('/calc/<int:x>/<int:y>/mult')
def calc_mult(x, y):
    return render_template('calc.html', x=x, sign='*', y=y, res=x*y)


@app.route('/template')
def template():
    return render_template('calc.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')