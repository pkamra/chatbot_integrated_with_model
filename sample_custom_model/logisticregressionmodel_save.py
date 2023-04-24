import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
# from sklearn.externals import joblib
import joblib


#Thsi was used for original training of the model
df = pd.read_csv    ('data_combined.csv')
# df = pd.read_excel('datacleansing_salesforce.xlsx', sheet_name='Model')
df = df[pd.notnull(df['tags'])]
df.head(10)

print(df['post'].apply(lambda x: len(x.split(' '))).sum())


# my_tags = \
#     ['Close their Account','Fees','Functionality','Investment Advice','Sign-up']

my_tags = \
    ['Close their Account','Fees','Functionality','Investment Advice','Sign-Up']


def print_plot(index):
    example = df[df.index == index][['post', 'tags']].values[0]
    if len(example) > 0:
        print(example[0])
        print('Tag:', example[1])

print_plot(10)

dont_remove = ['out','not','$','%']
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english')).difference(dont_remove)


def clean_text(text):
    """
        text: a string

        return: modified initial string
    """
    text = BeautifulSoup(text, "lxml").text  # HTML decoding
    text = text.lower()  # lowercase text
    text = REPLACE_BY_SPACE_RE.sub(' ', text)  # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = BAD_SYMBOLS_RE.sub('', text)  # delete symbols which are in BAD_SYMBOLS_RE from text
    # text = ' '.join(word for word in text.split() if word not in STOPWORDS)  # delete stopwors from text
    return text


df['post'] = df['post'].apply(clean_text)

print_plot(10)

print(df['post'].apply(lambda x: len(x.split(' '))).sum())


X = df.post
y = df.tags
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 42)

#
# #Logistic regression
#
logreg = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', LogisticRegression(n_jobs=1, C=1e5, max_iter=400)),
               ])
logreg.fit(X_train, y_train)

# Export the classifier to a file
joblib.dump(logreg, 'logistic_regression_xcel.pkl')

y_pred = logreg.predict(X_test)
#
print('accuracy %s' % accuracy_score(y_pred, y_test))
print(classification_report(y_test, y_pred,target_names=my_tags))
logregression_prediction = pd.concat([X_test,y_test], axis=1)
logregression_prediction['prediction0'] = y_pred
print("*****Data using Logistic Regression as classifier*******")
print(logregression_prediction)