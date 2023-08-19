from flask import Flask, render_template, request, redirect, url_for, session
from Amazon import Amazon
from Cleaning import Cleaning
import threading
from Flipkart import Flipkart
from Croma import Croma
import numpy as np
import pandas as pd
from Cleancsv import Cleancsv

app = Flask(__name__, template_folder='template')

# Home page that displays the input form
@app.route('/')
def home():
    return render_template('home.html')

# Output page that displays the processed data
@app.route('/output', methods=['POST'])
def output():
    # Get the data from the input form
    if 'file' in request.files:
        file = request.files['file']
        if file.filename.endswith('.csv'):
            csv_data = pd.read_csv(file)
            x = Cleancsv(csv_data)
            df = x.clean(csv_data)
            df, s1, s2 = x.predict(df)
            y = x.group(df)

            type = ['Product', 'Polarity', 'Price', 'Link', 'Avg Rating']

            q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = x.aspect_based_sentiment(y)

            q1 = zip(type, q1)
            q2 = zip(type, q2)
            q3 = zip(type, q3)
            q4 = zip(type, q4)
            q5 = zip(type, q5)
            q6 = zip(type, q6)
            q7 = zip(type, q7)
            q8 = zip(type, q8)
            q9 = zip(type, q9)
            q10 = zip(type, q10)


            #process_csv(csv_data)
            #return render_template('output.html', best_pro=best_pro[0], pol = pol, l = l, pri=pri, ra=ra)
        else:
            csv_data = ''
            data1 = request.form.get('data1')
            data2 = request.form.get('data2')
            data3 = request.form.get('data3')
            # data4 = request.form['data4']

            data2 = int(data2)
            data3 = int(data3)
            # data4 = int(data4)

            # amazon
            # amazon = Amazon(data1, data2, data3)
            z = Amazon(data1, data2, data3)  # , data4
            x = Croma(data1, data2, data3)  # , data4
            y = Flipkart(data1, data2, data3)  # , data4

            t3 = threading.Thread(target=z.run(data3))
            t1 = threading.Thread(target=x.run(data3))
            t2 = threading.Thread(target=y.run(data3))


            t3.start()
            t1.start()
            t2.start()

            t3.join()
            t1.join()
            t2.join()

            # data collection
            review = []
            price = []
            avg_rating = []
            all_rating = []
            link = []

            for i in [x, y, z]:
                x, y, z, a, b = i.result_queue.get()
                review.append(x)
                price.append(y)
                avg_rating.append(z)
                all_rating.append(a)
                link.append(b)

            # run
            # review_of_product, ratings_of_product, link_product, price_product, overall_r  = amazon.run(data3)

            # pass cleaning.
            print(all_rating)
            x = Cleaning(review, price, avg_rating, link)  # all_rating,
            df = x.clean(review, price, avg_rating, link)  # all_rating,
            df, s1, s2 = x.predict(df)
            y = x.group(df)

            type = ['Product', 'Polarity', 'Price', 'Link', 'Avg Rating']

            q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = x.aspect_based_sentiment(y)

            q1 = zip(type, q1)
            q2 = zip(type, q2)
            q3 = zip(type, q3)
            q4 = zip(type, q4)
            q5 = zip(type, q5)
            q6 = zip(type, q6)
            q7 = zip(type, q7)
            q8 = zip(type, q8)
            q9 = zip(type, q9)
            q10 = zip(type, q10)


    else:
        csv_data = ''
        data1 = request.form.get('data1')
        data2 = request.form.get('data2')
        data3 = request.form.get('data3')
        #data4 = request.form['data4']

        data2 = int(data2)
        data3 = int(data3)
        #data4 = int(data4)

        # amazon
        #amazon = Amazon(data1, data2, data3)
        z = Amazon(data1, data2, data3) # , data4
        x = Croma(data1, data2, data3) # , data4
        y = Flipkart(data1, data2, data3) #, data4

        t3 = threading.Thread(target=z.run(data3))
        t1 = threading.Thread(target=x.run(data3))
        t2 = threading.Thread(target=y.run(data3))


        t3.start()
        t1.start()
        t2.start()

        t3.join()
        t1.join()
        t2.join()


        # data collection
        review = []
        price = []
        avg_rating = []
        all_rating = []
        link = []

        for i in [x, y, z]:
            x, y, z, a, b = i.result_queue.get()
            review.append(x)
            price.append(y)
            avg_rating.append(z)
            all_rating.append(a)
            link.append(b)


        # run
        #review_of_product, ratings_of_product, link_product, price_product, overall_r  = amazon.run(data3)

        # pass cleaning.
        print(all_rating)
        x = Cleaning(review, price, avg_rating, link)  # all_rating,
        df = x.clean(review, price, avg_rating, link)  # all_rating,
        df, s1, s2 = x.predict(df)
        y = x.group(df)

        type = ['Product', 'Polarity', 'Price', 'Link', 'Avg Rating']

        q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = x.aspect_based_sentiment(y)

        q1 = zip(type, q1)
        q2 = zip(type, q2)
        q3 = zip(type, q3)
        q4 = zip(type, q4)
        q5 = zip(type, q5)
        q6 = zip(type, q6)
        q7 = zip(type, q7)
        q8 = zip(type, q8)
        q9 = zip(type, q9)
        q10 = zip(type, q10)


        # Render the output template with the processed data
    return render_template('output.html', q1 = q1, q2 = q2, q3 = q3 , q4 = q4, q5 = q5, q6 = q6, q7 = q7, q8 = q8, q9 = q9, q10 = q10, a1=a1, a2= a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, a8=a8, a9=a9, a10=a10)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='8080')
    #app.run()