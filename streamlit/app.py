import streamlit as st
import requests as r
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import re 

st.title('Spam Detection  App')
st.write('*Note: it will take up to 30 seconds to run the app.*')
form = st.form(key='message-form')
user_input = form.text_area('Enter your text')
submit = form.form_submit_button('Submit')
  
# Preprocess Heleper 
def preprocessor(text):
    text = re.sub('<[^>]*>', '', text) # Effectively removes HTML markup tags
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
    return text
	
st.image("./static/spam.jpg")

if submit:
    fig, ax = plt.subplots()
    item ={
      "message": 
         user_input
    }
	# interact with FastAPI endpoint
    prediction = r.post("http://fastapi:8000/predict-spam",  json=item)
    recommended_spam = prediction.json()
    label=recommended_spam['label']
    score=recommended_spam['spam_probability']
    if label == 'ham':
        st.success(f'This is a {label} : (score: {score})')
    else:
        st.error(f'OOPS it is a {label} : (score: {score})')
        
    classes = {0:'ham',1:'spam'}
    class_labels = list(classes.values())

    st.write("The predicted class is ",label)
    prob_ham= 1-score
    prob_spam = score
    probs = [prob_ham,prob_spam]
    ax = sns.barplot(probs ,class_labels, palette="winter", orient='h')
    ax.set_yticklabels(class_labels,rotation=0)
    plt.title("Probabilities of the Data belonging to each class")
    for index, value in enumerate(probs):
        plt.text(value, index,str(value))
    st.pyplot(fig) 