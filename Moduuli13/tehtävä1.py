from flask import Flask

app = Flask(__name__)
@app.route('/primenumber/<number>')
def primenumber(number):
    jako = False
    number = int(number)
    if number != 2 and not number % 2:
        jako = True
    for i in range(2, number):
        if not number % i:
            jako = True
        if jako:
            break
    if jako:
        jako = False
        answer = {
            "number" : number, "notPrime" : jako,
        }
        return answer
    if not jako and number != 1:
        jako = True
        answer = {
            "number" : number, "isPrime" : jako,
        }
        return answer

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)