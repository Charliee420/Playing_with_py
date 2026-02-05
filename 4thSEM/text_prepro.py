import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
# nltk.download('omw-1.4')
text = "Hi.... Babes!🥰 How are you? Looking very gorgeous I Love you  ∞ × ∞  "
text = re.sub(r'[^\w\s]', '', text)
text =re.sub(r"\S+@\S+", "", text)
text = text.lower()
text = word_tokenize(text)
stop_words = set(stopwords.words('english'))
text = [word for word in text if word not in stop_words]
text = [WordNetLemmatizer().lemmatize(word) for word in text]
text = ' '.join(text)
print(text)