#search engine
def matchingWords(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score +=1
    return score

if __name__ == "__main__":
    sentences = ["Python is a good", "this is snake", "harry is a good boy", "subscribe now"]

    query = input("Please enter the query string: ")
    scores = [matchingWords(query, sentence) for sentence in sentences]
    sortSentScore = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True) if sentScore[0] !=0]

    print(f"{len(sortSentScore)} results found!")
    for score, item in sortSentScore:
        print(f" \"{item}\": with a score of {score}")
