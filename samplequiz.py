questions= [
    {
        "Question": "What is a valid keyword in python",
        "Options": {
            "A": "global",
            "B": "elseif",
            "C": "download",
            "D": "export"
        },
        "Answer": "A"
    },

    {
        "Question": "What are the control statements in python",
        "Options": {
            "A": "break",
            "B": "break and continue",
            "C": "continue",
            "D": "control"
        },
        "Answer": "B"
    },

    {
        "Question": "What Does .split() do in python?",
        "Options": {
            "A": "Combines strings",
            "B": "Removes spaces",
            "C": "Splits a string into parts",
            "D": "Converts string to integer"
        },
        "Answer": "C"
    },

    {
        "Question": "What will this code output? x=[1,2,3] x.append([4,5]) print(len(x))",
        "Options": {
            "A": "3",
            "B": "4",
            "C": "5",
            "D": "Error"
        },
        "Answer": "B"
    },

    {
        "Question": "Which data structure stores key-value pairs?",
        "Options": {
            "A": "List",
            "B": "Tuple",
            "C": "Dictionary",
            "D": "Set"
        },
        "Answer": "C"
    },

    {
        "Question": "What does this function return? def fun(a,b=2): return a*b print(fun(5))",
        "Options": {
            "A": "5",
            "B": "7",
            "C": "10",
            "D": "Error"
        },
        "Answer": "C"
    },

    {
        "Question": "What is the output? s='Python' print(s[1:4])",
        "Options": {
            "A": "yth",
            "B": "Pyt",
            "C": "tho",
            "D": "ytho"
        },
        "Answer": "A"
    },

    {
        "Question": "Which loop is best when the number of iterations is unknown beforehand?",
        "Options": {
            "A": "for loop",
            "B": "while loop",
            "C": "nested loop",
            "D": "infinite loop"
        },
        "Answer": "B"
    },

    {
        "Question": "What will this print? nums=[2,4,6,8] print(nums[-2])",
        "Options": {
            "A": "4",
            "B": "6",
            "C": "8",
            "D": "-2"
        },
        "Answer": "B"
    },

    {
        "Question": "What is the output? for i in range(1,5): if i==3: break print(i,end=' ')",
        "Options": {
            "A": "1 2 3 4",
            "B": "1 2",
            "C": "3",
            "D": "1 2 3"
        },
        "Answer": "B"
    }
]
name=input("Name:")
rollnumber=input("RollNumber:")
score=0
for ch in questions: 
     print(ch["Question"])
     for key,value in ch["Options"].items(): 
          print(key,value)
     option=input("Enter Option(A/B/C/D)")
     if option == ch["Answer"]:
        print("Correct!")
        score+=1
     else:
        print("Wrong!")
        print(f"Correct Answer: {ch['Answer']}")
print(f"Name: {name}")
print(f"RollNumber: {rollnumber}")
print(f"Score : {score}")