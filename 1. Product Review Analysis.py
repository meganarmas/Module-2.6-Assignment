# Task 1: Keyword Highlighter
# Write a program that searches through reviews list and looks for keywords such as "good", 
# "excellent", "bad", "poor", and "average". We want you to capitalize those 
# keywords then print out each review. Print out each review with the keywords in 
# uppercase so they stand out.

reviews = ["This product is really good. I'm impressed with its quality.", 
           "The performance of this product is excellent. Highly recommended!",
           "I had a bad experience with this product. It didn't meet my expectations.",
           "Poor quality product. Wouldn't recommend it to anyone.", 
           "The product was average. Nothing extraordinary about it."]

keywords = ['good.', 'excellent.', 'bad', 'Poor', 'average.']

def reviews_cap():
    for review in reviews:
        hold_review = []
        words = review.split()
        for word in words:
            hold_word = word
            for keyword in keywords:
              if word == keyword:
                  hold_word = word.upper()
                  break
            hold_review.append(hold_word)
        final_review = " ".join(hold_review)
        print(final_review)

reviews_cap()

# So for the first string in the reviews list, we want it to say: 
# "This product is really GOOD. I'm impressed with its quality."

# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.

# .count

#positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
#negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

words = ["good", "excellent", "great", "awesome", "fantastic", "superb", 
         "amazing", "bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

descri_words = reviews.count([words])
total = sum(descri_words)
print(total)

# Task 3: Review Summary
#Implement a script that takes the first 30 characters of a review and appends "…" 
# to create a summary. Ensure that the summary does not cut off in the middle of a word.
# Example: "This product is really good. I'm...",
review_4 = ("Poor quality product. Wouldn't recommend it to anyone.")

sliced_review = review_4[0:30]
print(sliced_review + "...")