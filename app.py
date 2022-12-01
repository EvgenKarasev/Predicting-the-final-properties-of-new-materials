import flask
from flask import render_template, request
import pickle
import sklearn
from sklearn.linear_model import SGDRegressor
import catboost
from catboost import CatBoostRegressor


app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['POST', 'GET'])

@app.route('/index', methods=['POST', 'GET'])
def processing():
    
    
    if flask.request.method == 'GET':
        return render_template('main.html')
    
    if request.method == 'POST':
        param_lst = []
        
        for i in range(1, 13):
            param = request.form.get(f'priznak{i}')
            param_lst.append(param)
            
        
        with open('best_model.pkl', 'rb') as f:
            model = pickle.load(f)
        
        prediction = model.predict([param_lst])
    
        message = round(float(prediction), 4)


        return render_template('main.html', message=message) 


if __name__ == '__main__':
    app.run()