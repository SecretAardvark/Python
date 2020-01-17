import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
    'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiznum in range(35):
        #todo: create the quiz and answer key files 

        #todo : Write out the header for the quiz

        #todo: Shuffle the order of the states 

        #todo loop through all 50 states, making a q for each

    #creates the quiz files
    quizfile = open('capitalsquiz%s.txt' %(quiznum +1), 'w')
    answerkey = open('capitalquiz_answers%s.txt' %(quiznum+1), 'w')

    #Creates the header for the quiz
    quizfile.write('Name: \nDate: \nPeriod: \n')
    quizfile.write((' '*20) + 'State Capitals quiz(Form%s)'%(quiznum+1))
    quizfile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)


for questionNum in range(50):
    correctanswer = capitals[states[questionNum]]
    wronganswer = list(capitals.values())
    del wronganswer[wronganswer.index(correctanswer)]
    wronganswer = random.sample(wronganswer, 3)
    answerOptions = wronganswer + [correctanswer]
    random.shuffle(answerOptions)

quizfile.write('%s. What is the capital of %s?\n'%(questionNum +1, states[questionNum]))
for i in range(4):
    quizfile.write('%s. %s\n'%(questionNum +1, 'ABCD'[answerOptions.index(correctanswer)]))

quizfile.close()
answerkey.close()