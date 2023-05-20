from flask import Flask, request
import zipfile
from gensim.models import KeyedVectors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# Create a Flask application
app = Flask(__name__)

# zip_path = './wiki.vi.model.zip'
# word2vec_file = './data' # Replace with the path to the Word2Vec file inside the ZIP
# # Replace with the path to your ZIP file
# with zipfile.ZipFile(zip_path, 'r') as zip_file:
#     zip_file.extractall(word2vec_file)

word_vectors = KeyedVectors.load_word2vec_format('./data/wiki.vi.model.bin', binary=True)

# Define a route and its corresponding handler for POST requests
@app.route("/text-api", methods=["POST"])
def handle_post():

    data = request.get_json()  # Retrieve JSON data from the request
    if 'doc1' in data and 'doc2' in data:
        doc1 = data['doc1']
        doc2 = data['doc2']
        # Preprocess documents and calculate TF-IDF vectors
        corpus = [doc1, doc2]
        vectorizer = TfidfVectorizer()
        tfidf_vectors = vectorizer.fit_transform(corpus)

        # Calculate cosine similarity between TF-IDF vectors
        similarity_matrix = cosine_similarity(tfidf_vectors)
        similarity = similarity_matrix[0][1]
        print(similarity)
        # Return a response
        response = {"similarity": similarity}
        return response, 200  # Return JSON response with status code 200
        return "doc1 and doc2 received and processed successfully"
    else:
        return "Error: 'doc1' and/or 'doc2' keys not found in JSON data", 400


# Run the server
if __name__ == "__main__":
    app.run()
