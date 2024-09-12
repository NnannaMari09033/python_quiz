
data = [
        {
            "question": "Which of these is not a renewable energy source?",
            "options": ["Solar", "Wind", "Coal", "Hydroelectric"],
            "answer": "3"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Jupiter", "Mars", "Saturn"],
            "answer": "2"
        },
        {
            "question": "Which country hosted the 2016 Summer Olympics?",
            "options": ["China", "Brazil", "United Kingdom", "Japan"],
            "answer": "2"
        },
        {
            "question": "What is the main gas found in the Earth's atmosphere?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"],
            "answer": "3"
        },
        {
            "question": "Who was the first President of the United States?",
            "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
            "answer": "3"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["O2", "H2O", "CO2", "HO"],
            "answer": "2"
        },
        {
            "question": "Which planet is known as the Morning Star?",
            "options": ["Venus", "Mars", "Mercury", "Jupiter"],
            "answer": "1"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Great White Shark"],
            "answer": "2"
        },
        {
            "question": "Who wrote the play 'Hamlet'?",
            "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"],
            "answer": "1"
        },
        {
            "question": "What is the capital city of Canada?",
            "options": ["Toronto", "Vancouver", "Ottawa", "Montreal"],
            "answer": "3"
        }
    ]


print(data[0].get("question")) #getting a particular item from a dictionary using the get method
print(data[0]["question"]) #using the index method
print(data[0]["options"]) 


def game():   
    score = 0 #local variable
    index = 0


    while index < len(data):

        print(f"1. {data[index]['options'][0]}") 
        print(f"2. {data[index]['options'][1]}") 
        print(f"3. {data[index]['options'][2]}")
        print(f"4. {data[index]['options'][3]}")


        answer = input("choose 1/2/3/4: ")

        if answer == data[index]['answer']:
        
            score += 1
            index += 1
            print(f"correct. Score:{score}/{len(data)}")
        else:
            index += 1
            print(f"correct. Score:{score}/{len(data)}") 
    else: 
        print(f"Your final score is {score}/{len(data)}")





game()

