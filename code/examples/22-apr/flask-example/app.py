from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        text = request.form['input_text']
        print(text)
        # do whatever with the text
        redirect('/')
    name = 'class anemone'
    temperature = 12
    nums = [1, 2, 3, 42, 56, 167]  
    return render_template('index.html', name=name, temperature=temperature, nums=nums)

app.run(debug=True)