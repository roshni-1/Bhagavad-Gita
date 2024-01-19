from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load Feature Mapping
with open('feature_mapping.pkl', 'rb') as file:
    feature_mapping = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['user_input']

    matching_features = []
    for feature, keywords in feature_mapping.items():
        if any(keyword in user_input.lower() for keyword in keywords):
            matching_features.append(feature)

    relevant_quotes = []
    for feature in matching_features:
        for verse in feature_mapping[feature]:
            relevant_quotes.append({
                'Title': verse['Title'],
                'Chapter': verse['Chapter'],
                'Verse': verse['Verse'],
                'Sanskrit Anuvad': verse['Sanskrit Anuvad'],
                'Hindi Anuvad': verse['Hindi Anuvad'],
                'English Translation': verse['Enlgish Translation']
            })

    return render_template('result.html', user_input=user_input, relevant_quotes=relevant_quotes)

if __name__ == '__main__':
    app.run(debug=True)
