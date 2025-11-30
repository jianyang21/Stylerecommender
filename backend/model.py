import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class FashionRecommender:

    def __init__(self, csv_path):
        # load dataset
        self.df = pd.read_csv(csv_path)

        # combine all text fields into one
        self.df["combined"] = (
            self.df["title"].astype(str) + " " +
            self.df["description"].astype(str) + " " +
            self.df["style"].astype(str) + " " +
            self.df["color"].astype(str) + " " +
            self.df["season"].astype(str)
        )

        # vectorize text
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.vectors = self.vectorizer.fit_transform(self.df["combined"])

    def recommend(self, user_query, top_k=5):
        # convert user input into vector
        user_vec = self.vectorizer.transform([user_query])

        # compute similarity scores
        scores = cosine_similarity(user_vec, self.vectors).flatten()

        # pick top matches
        top_indices = scores.argsort()[::-1][:top_k]

        # return results cleanly
        return self.df.iloc[top_indices][[
            "title", "description", "style", "color", "season"
        ]].to_dict(orient="records")


