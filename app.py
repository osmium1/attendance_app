from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

app = Flask(__name__)

# Function to plot the graph
def plot_attendance(n):
    x = np.arange(10, 41)
    y = np.array([(x_val - n) / x_val * 100 for x_val in x])

    plt.figure(figsize=(16, 8))  # Larger figure size
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Projected Attendance')

    def round_attendance(value):
        if value % 1 >= 0.5:
            return np.ceil(value)
        else:
            return np.floor(value)

    y_rounded = np.array([round_attendance(val) for val in y])

    plt.fill_between(x, y, where=(y_rounded <= 60), color='red', alpha=0.3, edgecolor='none', label='≤ 60%')
    plt.fill_between(x, y, where=(y_rounded > 60) & (y_rounded <= 74), color='yellow', alpha=0.3, edgecolor='none', label='61% - 74%')
    plt.fill_between(x, y, where=(y_rounded > 74) & (y_rounded <= 80), color='#CCFFCC', alpha=0.3, edgecolor='none', label='75% - 80%')
    plt.fill_between(x, y, where=(y_rounded > 80) & (y_rounded <= 85), color='#99FF99', alpha=0.3, edgecolor='none', label='81% - 85%')
    plt.fill_between(x, y, where=(y_rounded > 85) & (y_rounded <= 90), color='#66FF66', alpha=0.3, edgecolor='none', label='86% - 90%')
    plt.fill_between(x, y, where=(y_rounded > 90) & (y_rounded <= 95), color='#33FF33', alpha=0.3, edgecolor='none', label='91% - 95%')
    plt.fill_between(x, y, where=(y_rounded > 95), color='cyan', alpha=0.3, edgecolor='none', label='96% - 100%')

    plt.xlim(10, 40)
    plt.ylim(0, 100)
    plt.xticks(np.arange(10, 41, 1))
    plt.xlabel('Total Classes Held')
    plt.ylabel('Projected Attendance (%) If no more classes are missed')
    plt.title('Projected Attendance Based on Classes Missed')
    plt.legend()
    plt.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return plot_url


@app.route('/', methods=['GET', 'POST'])
def index():
    plot_url = None
    if request.method == 'POST':
        n = int(request.form['n'])
        plot_url = plot_attendance(n)
    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run()
