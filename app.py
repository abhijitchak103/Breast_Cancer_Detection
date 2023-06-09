from flask import Flask, render_template, request, jsonify
from src.pipeline.prediction_pipeline import PredictPipeline, CustomData


application = Flask(__name__)

app = application


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/predict", methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        data = CustomData(
            texture_mean = float(request.form.get('texture_mean')),
            area_mean = float(request.form.get('area_mean')), 
            smoothness_mean = float(request.form.get('smoothness_mean')), 
            concavity_mean = float(request.form.get('concavity_mean')),
            symmetry_mean = float(request.form.get('symmetry_mean')), 
            fractal_dimension_mean = float(request.form.get('fractal_dimension_mean')),
            texture_se = float(request.form.get('texture_se')),
            area_se = float(request.form.get('area_se')), 
            smoothness_se = float(request.form.get('smoothness_se')), 
            compactness_se = float(request.form.get('compactness_se')), 
            concavity_se = float(request.form.get('concavity_se')),
            concave_points_se = float(request.form.get('concave_points_se')), 
            symmetry_se = float(request.form.get('symmetry_se')), 
            fractal_dimension_se = float(request.form.get('fractal_dimension_se')),
            texture_worst = float(request.form.get('texture_worst')),
            area_worst = float(request.form.get('area_worst')), 
            smoothness_worst = float(request.form.get('smoothness_worst')), 
            concavity_worst = float(request.form.get('concavity_worst')),
            symmetry_worst = float(request.form.get('symmetry_worst')), 
            fractal_dimension_worst = float(request.form.get('fractal_dimension_worst'))
            )
        final_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict_label(final_data)

        if pred[0] == 1:
            return render_template('results.html', final_result = 'Malignant')
        else:
            return render_template('results.html', final_result = 'Benign')
        

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)