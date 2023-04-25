# This is a sample Python script.from
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, request
import tensorflow as tf
from keras.models import load_model
import numpy as np

app = Flask(__name__)

model = load_model('model_seq')
model.compile()
print(model.predict(np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]).reshape(1, -1)))


@app.route('/', methods=['POST', 'GET'])
def index():
    message = ''
    if request.method == 'POST':
        param_list = ('plot', 'mup', 'ko', 'seg', 'tv', 'pp', 'mup', 'pr', 'ps', 'yn', 'shn', 'pln')
        params = []
        for i in param_list:
            param = request.form.get(i)
            params.append(param)
        params = [float(i.replace(',', '.')) for i in params]
        predict = model.predict(np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]).reshape(1, -1))
        #print(params)
        #print(model.predict(np.array(params)).reshape(1, -1))
        message = f'Спрогнозированное Соотношение матрица-наполнитель для введенных параметров:{round(float(predict),2)}'
    return render_template('index.html', message=message)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
