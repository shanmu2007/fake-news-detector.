from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Sample news for training
news = [
    "The government announced a new education program.",
    "The school opened a new computer laboratory.",
    "Scientists published a new research report.",
    "The company announced a new software product.",
    "The government launched a new public service.",
    
    "Aliens have landed on Earth and are living secretly.",
    "A miracle drink can make people live forever.",
    "Scientists say the moon will disappear tomorrow.",
    "A famous actor has been secretly replaced by a robot.",
    "Drinking this magic water gives you superpowers."
]

# 1 means real news and 0 means fake news
labels = [
    1, 1, 1, 1, 1,
    0, 0, 0, 0, 0
]


# Convert news text into numbers
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(news)


# Train the machine-learning model
model = LogisticRegression()

model.fit(X, labels)


def check_news(text):

    news_data = vectorizer.transform([text])

    prediction = model.predict(news_data)[0]

    confidence = model.predict_proba(news_data).max() * 100

    if prediction == 1:
        result = "Likely Real News"
    else:
        result = "Likely Fake News"

    return f"{result} - Confidence: {confidence:.1f}%"
    """
    Check whether the given news is likely to be real or fake.
    """

    text = vectorizer.transform([text])

    prediction = model.predict(text)[0]

    if prediction == 1:
        return "Likely Real News"
    else:
        return "Likely Fake News"