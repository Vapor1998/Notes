
import numpy as np
import re
import pandas as pd
from textblob import TextBlob
import nltk
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
import nltk
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer



class Cleancsv:
    def __init__(self, df):
        self.df = df

    def clean(self, df):
        x = self.df['Avg Rating']
        for i, j in enumerate(x):
            if type(j) == list():
                j = j[0]
                y = re.sub(r'[^0-9.]+', '', j)
                y = y + '   '
                y = y[:3].strip()
                self.df.loc[i, 'Avg Rating'] = y
            else:
                if type(j) == str:
                    y = re.sub(r'[^0-9.]+', '', j)
                    y = y + '   '
                    y = y[:3].strip()
                    self.df.loc[i, 'Avg Rating'] = y

        # cleeaning price
        x = self.df['Price']
        index = 0
        for i in x:
            if type(i) == list:
                y = i[0]
                y = y.split('.')
                y = y[0]
                y = re.findall(r'\d', y)
                string = ' '
                for j in y:
                    string += j
                y = float(string)
                # print(y)
                self.df.loc[index, 'Price'] = y
            else:
                y = i
                if '\n' in y:
                    y = y.split('\n')
                    y = y[0]
                y = y.split('.')
                y = y[0]
                y = re.sub(r'[\n₹,]', '', y)
                y = re.findall(r'\d', y)
                string = ' '
                for j in y:
                    string += j
                if len(string) == 0 or len(string) == 1:
                    string = 0
                else:
                    y = float(string)
                # print(y)
                self.df.loc[index, 'Price'] = y

            index += 1

        # cleaning review
        cleaned = []
        for i in self.df['Review']:
            i = str(i)
            x = re.sub(r"[^a-zA-Z\s.,!?']", "", i)
            y = re.sub(r'READ MORE', '', x)
            # y = re.sub(r'[^\x00-\x7F]+', '', x)
            cleaned.append(y)

        # tokenizing
        token = []
        stop_words = set(stopwords.words('english'))
        for i in cleaned:
            word_tokens = word_tokenize(i)
            # print(word_tokens)
            filtered_words = [word for word in word_tokens if not word.lower() in stop_words]
            word = ' '.join(filtered_words)
            words = re.sub('[^a-zA-Z0-9 \n]', '', word)
            print(words)
            token.append(words)
        self.df['Cleaned1'] = token
        return self.df

    # print('-------------')
    def predict(self, data):
        def get_sentiment(text):
            return TextBlob(text).sentiment.polarity

        self.df['sentiment'] = self.df['Cleaned1'].apply(get_sentiment)
        sentiment = self.df['sentiment']
        avg = self.df.groupby('Product')['sentiment'].mean().sort_values(ascending=False)[:1]
        best_product = avg.index
        polarity = avg.values
        price = self.df.loc[self.df['Product'] == best_product[0], 'Price'].values[0]
        link = self.df.loc[self.df['Product'] == best_product[0], 'Link'].values[0]
        rate = self.df.loc[self.df['Product'] == best_product[0], 'Avg Rating'].values[0]
        pro = self.df.Product.unique()
        pro_d = {}
        ex = []
        for i in self.df.Link:
            match = re.search(r'www\.(.*?)\.(?:com|in)', i)
            extract = match.group(1)
            ex.append(extract)
        self.df['Website'] = ex
        for i in pro:
            #     p = df.loc[df.Product == i]
            #     print(p.Link[])
            p = self.df.loc[self.df.Product == i]
            l = p.Link.unique()[0]
            match = re.search(r'www\.(.*?)\.(?:com|in)', l)
            if match:
                extract = match.group(1)
                pro_d[extract] = pro_d.get(extract, 0) + 1

        sent = {}
        x = self.df.groupby('Website')['sentiment'].agg('mean')
        for i, j in x.items():
            sent[i] = j
        return self.df, pro_d, sent

    def group(self, df):
        groupby_of_all = df.groupby('Product')['Cleaned1'].apply(list)
        return groupby_of_all

    def aspect_based_sentiment(self, groupby_of_all):
        se = {}
        prods = groupby_of_all.index
        for i, j in enumerate(groupby_of_all.values):
            list = []
            for k in j:
                x = nltk.word_tokenize(k)
                y = nltk.pos_tag(x)
                list.append(y)
            se[prods[i]] = list

        products_review_with_sentiments = {}
        for i, j in se.items():
            d1 = {}
            for k in j:
                for l, m in enumerate(k):
                    if len(m[0]) > 4 and '...' not in m[0] and '....':
                        if m[1] == 'NN' or m[1] == 'VB':
                            aspect = m[0]
                            sentence = ''
                            if aspect not in d1.keys():
                                d1[aspect] = []
                            for n in k[l:]:
                                sentence += n[0] + ' '
                                if m[1] == 'JJ':
                                    break
                            x = d1[aspect]
                            x.append(sentence.strip())
                products_review_with_sentiments[i] = d1

        def sentiment(d):
            sid = SentimentIntensityAnalyzer()
            for i, j in d.items():
                # print(j)
                for k, l in j.items():
                    d2 = {}
                    for m in l:
                        sentiment = sid.polarity_scores(m)
                        d2[m] = sentiment

                    d[i][k] = d2
            return d

        x = sentiment(products_review_with_sentiments)

        # overall sentiment
        compound_aspect = {}
        for i in x.keys():
            asp = x[i]
            pos = 0
            neg = 0
            neu = 0
            compound = 0
            count = 0
            for j in asp.keys():
                comment = x[i][j]
                for k in comment.values():
                    pos += k['pos']
                    neg += k['neg']
                    neu += k['neu']
                    compound += k['compound']
                    count += 1
            try:
                compound_aspect[i] = compound / count
            except ZeroDivisionError:
                compound_aspect[i] = 0

        # each aspect overall sentiment
        pro_asp_info = {}
        for i in x.keys():
            asp = x[i]
            aspect_info = {}
            for j in asp.keys():
                pos = 0
                neg = 0
                neu = 0
                compound = 0
                count = 0
                comment = x[i][j]
                # print(comment)
                # print(j)
                for k in comment.values():
                    pos += k['pos']
                    neg += k['neg']
                    neu += k['neu']
                    compound += k['compound']
                    count += 1

                info = {'pos': pos / count, 'neg': neg / count, 'neu': neu / count, 'compound': compound / count}

                aspect_info[j] = info
            pro_asp_info[i] = aspect_info

        best_products = {}
        data = self.df.Price
        low = 1
        high = 10
        for i in range(10):

            if low == 1:
                lower_quartile = data.min()
            lower_quartile = np.percentile(data, low)
            high_quartile = np.percentile(data, high)

            # quartile
            closest_min_value = min(data, key=lambda x: abs(x - lower_quartile))
            closest_max_value = min(data, key=lambda x: abs(x - high_quartile))

            s1 = self.df.loc[(self.df.Price >= closest_min_value) & (self.df.Price <= closest_max_value)]

            pro = s1.Product.unique()
            fore = {}
            for i in pro:
                x1 = compound_aspect[i]
                fore[i] = x1
                # print(i)
            maxe = max(fore.values())
            # print("Products between {} - {} Quartile".format(low, high))

            pro = [k for k, v in fore.items() if v == maxe]
            # print(pro)

            prods = {}
            prods[pro[0]] = maxe
            best_products['Products between {} - {} Quartile'.format(low, high)] = prods

            # print('==============')
            # print()
            low += 10
            high += 10
            if high > 100:
                break
        price = {}
        link = {}
        rating = {}
        # print(best_products)
        for k, v in best_products.items():
            price1 = {}
            link1 = {}
            rat = {}
            print(v)
            # print(list(v.keys()))
            a = [k for k, v1 in v.items()][0]
            #             for i in v.keys():
            #                 print(i)
            x1 = self.df.loc[self.df.Product == a]
            p = x1.Price.unique()[0]
            links = x1.Link.unique()[0]
            ratings = x1['Avg Rating'].unique()[0]
            price1[a] = p
            link1[a] = links
            rat[a] = ratings

            rating[k] = rat
            price[k] = price1
            link[k] = link1

        quartile1 = []
        quartile2 = []
        quartile3 = []
        quartile4 = []
        quartile5 = []
        quartile6 = []
        quartile7 = []
        quartile8 = []
        quartile9 = []
        quartile10 = []

        q1asp = []
        q2asp = []
        q3asp = []
        q4asp = []
        q5asp = []
        q6asp = []
        q7asp = []
        q8asp = []
        q9asp = []
        q10asp = []

        asp_for_best = {}
        for i, j in best_products.items():
            k = [l for l, v in j.items()][0]
            x = pro_asp_info[k]
            asp_for_best[k] = x

        for k, v in best_products.items():
            if '10' in k:
                key = [k1 for k1, v1 in v.items()][0]
                pol = [v1 for k1, v1 in v.items()][0]

                q1asp.append(asp_for_best[key])
                quartile1.append(key)
                quartile1.append(pol)

                pr = price[k]
                pri = [v1 for k1, v1 in pr.items()][0]
                quartile1.append(pri)

                li = link[k]
                links = [v1 for k1, v1 in li.items()][0]
                quartile1.append(links)

                ra = rating[k]
                ratings = [v1 for k1, v1 in ra.items()][0]
                quartile1.append(ratings)

            if '20' in k:
                key = [k1 for k1, v1 in v.items()][0]
                pol = [v1 for k1, v1 in v.items()][0]

                q2asp.append(asp_for_best[key])
                quartile2.append(key)
                quartile2.append(pol)

                pr = price[k]
                pri = [v1 for k1, v1 in pr.items()][0]
                quartile2.append(pri)

                li = link[k]
                links = [v1 for k1, v1 in li.items()][0]
                quartile2.append(links)

                ra = rating[k]
                ratings = [v1 for k1, v1 in ra.items()][0]
                quartile2.append(ratings)
            if '30' in k:
                key = [k1 for k1, v1 in v.items()][0]
                pol = [v1 for k1, v1 in v.items()][0]

                q3asp.append(asp_for_best[key])
                quartile3.append(key)
                quartile3.append(pol)

                pr = price[k]
                pri = [v1 for k1, v1 in pr.items()][0]
                quartile3.append(pri)

                li = link[k]
                links = [v1 for k1, v1 in li.items()][0]
                quartile3.append(links)

                ra = rating[k]
                ratings = [v1 for k1, v1 in ra.items()][0]
                quartile3.append(ratings)
            if '40' in k:
                key = [k1 for k1, v1 in v.items()][0]
                pol = [v1 for k1, v1 in v.items()][0]

                q4asp.append(asp_for_best[key])
                quartile4.append(key)
                quartile4.append(pol)

                pr = price[k]
                pri = [v1 for k1, v1 in pr.items()][0]
                quartile4.append(pri)

                li = link[k]
                links = [v1 for k1, v1 in li.items()][0]
                quartile4.append(links)

                ra = rating[k]
                ratings = [v1 for k1, v1 in ra.items()][0]
                quartile4.append(ratings)
            if '50' in k:
                key = [k1 for k1, v1 in v.items()][0]
                pol = [v1 for k1, v1 in v.items()][0]

                q5asp.append(asp_for_best[key])
                quartile5.append(key)
                quartile5.append(pol)

                pr = price[k]
                pri = [v1 for k1, v1 in pr.items()][0]
                quartile5.append(pri)

                li = link[k]
                links = [v1 for k1, v1 in li.items()][0]
                quartile5.append(links)

                ra = rating[k]
                ratings = [v1 for k1, v1 in ra.items()][0]
                quartile5.append(ratings)
            if '60' in k:
                key = [k1 for k1, v1 in v.items()][0]
                pol = [v1 for k1, v1 in v.items()][0]

                q6asp.append(asp_for_best[key])
                quartile6.append(key)
                quartile6.append(pol)

                pr = price[k]
                pri = [v1 for k1, v1 in pr.items()][0]
                quartile6.append(pri)

                li = link[k]
                links = [v1 for k1, v1 in li.items()][0]
                quartile6.append(links)

                ra = rating[k]
                ratings = [v1 for k1, v1 in ra.items()][0]
                quartile6.append(ratings)
            if '70' in k:
                key = [k1 for k1, v1 in v.items()][0]
                pol = [v1 for k1, v1 in v.items()][0]

                q7asp.append(asp_for_best[key])
                quartile7.append(key)
                quartile7.append(pol)

                pr = price[k]
                pri = [v1 for k1, v1 in pr.items()][0]
                quartile7.append(pri)

                li = link[k]
                links = [v1 for k1, v1 in li.items()][0]
                quartile7.append(links)

                ra = rating[k]
                ratings = [v1 for k1, v1 in ra.items()][0]
                quartile7.append(ratings)
            if '80' in k:
                key = [k1 for k1, v1 in v.items()][0]
                pol = [v1 for k1, v1 in v.items()][0]

                q8asp.append(asp_for_best[key])
                quartile8.append(key)
                quartile8.append(pol)

                pr = price[k]
                pri = [v1 for k1, v1 in pr.items()][0]
                quartile8.append(pri)

                li = link[k]
                links = [v1 for k1, v1 in li.items()][0]
                quartile8.append(links)

                ra = rating[k]
                ratings = [v1 for k1, v1 in ra.items()][0]
                quartile8.append(ratings)
            if '90' in k:
                key = [k1 for k1, v1 in v.items()][0]
                pol = [v1 for k1, v1 in v.items()][0]

                q9asp.append(asp_for_best[key])
                quartile9.append(key)
                quartile9.append(pol)

                pr = price[k]
                pri = [v1 for k1, v1 in pr.items()][0]
                quartile9.append(pri)

                li = link[k]
                links = [v1 for k1, v1 in li.items()][0]
                quartile9.append(links)

                ra = rating[k]
                ratings = [v1 for k1, v1 in ra.items()][0]
                quartile9.append(ratings)
            if '100' in k:
                key = [k1 for k1, v1 in v.items()][0]
                pol = [v1 for k1, v1 in v.items()][0]

                q10asp.append(asp_for_best[key])
                quartile10.append(key)
                quartile10.append(pol)

                pr = price[k]
                pri = [v1 for k1, v1 in pr.items()][0]
                quartile10.append(pri)

                li = link[k]
                links = [v1 for k1, v1 in li.items()][0]
                quartile10.append(links)

                ra = rating[k]
                ratings = [v1 for k1, v1 in ra.items()][0]
                quartile10.append(ratings)

        return quartile1, quartile2, quartile3, quartile4, quartile5, quartile6, quartile7, quartile8, quartile9, quartile10, q1asp, q2asp, q3asp, q4asp, q5asp, q6asp, q7asp, q8asp, q9asp, q10asp

    #return best_products, price, link, rating

        # groupby_of_all = df.groupby('Product')['Cleaned1'].apply(list)
    # bp, p, l, r = aspect_based_sentiment(groupby_of_all)

#     groupby_of_all = df.groupby('Product')['Cleaned1'].apply(list)
#     m1 = aspect_based_sentiment(groupby_of_all)


# return best_product, polarity, link, price, rate
