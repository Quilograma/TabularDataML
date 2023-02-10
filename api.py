from fastapi import FastAPI
import uvicorn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

app = FastAPI()

data = load_iris()

X, y, cols = data['data'], data['target'], data['feature_names']

print(data)


@app.get("/train")
def model_train():

    model = RandomForestClassifier()
    model.fit(X,y)

    return 'Modelo treinado fixe!'


if __name__ == "__main__":
    uvicorn.run(app,host='my_app',port=3000)