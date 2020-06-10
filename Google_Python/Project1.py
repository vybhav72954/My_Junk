!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

# To upload your text file, run the following cell that contains all the code for a custom uploader widget. 
# Once you run this cell, a "Browse" button should appear below it. Click this button and navigate the window 
# to locate your saved text file.

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

# Write a function in the cell below that iterates through the words in file_contents, removes punctuation, 
# and counts the frequency of each word. Oh, and be sure to make it ignore word case, 
# words that do not contain all alphabets and boring words like "and" or "the". 
# Then use it in the generate_from_frequencies function to generate your very own word cloud!

def calculate_frequencies(file_contents):
    words = file_contents.lower().split()
    result = {}
    
        
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just" \
    "for", "in", "on", "not", "into", "could", "up", "now", "should", "must", "for", "so", "then", "till"]
    
    for word in words:
        if word not in uninteresting_words and word.isalpha():
            if word not in result and word:
                result[word] = 1
            else:
                result[word] += 1
    
            
    # LEARNER CODE START HERE
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(result)
    return cloud.to_array()
    
    # Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

