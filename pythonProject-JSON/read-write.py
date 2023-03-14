# t=open("c:\\users\\jd mamangun\\pycharmprojects\\pythonProject-JSON\\test-write.txt","a")
# t.write("\nthird text appended on new line")
# t.close()

# r=open("c:\\users\\jd mamangun\\pycharmprojects\\pythonProject-JSON\\test-read-dialogue.txt","r")
# print(r.read())
# r.close()

# r=open("c:\\users\\jd mamangun\\pycharmprojects\\pythonProject-JSON\\test-read-dialogue.txt","r")
#
# for line in r:
#     print(line)
#
# r.close()

# r=open("c:\\users\\jd mamangun\\pycharmprojects\\pythonProject-JSON\\test-read-dialogue.txt","r")
#
# for line in r:
#     words=line.split(" ")
#     print(words)
#
# r.close()


# r=open("c:\\users\\jd mamangun\\pycharmprojects\\pythonProject-JSON\\test-read-dialogue.txt","r")
#
# for line in r:
#     words=line.split(" ")
#     print(words, "word count:",len(words))
#
# r.close()


# with open("c:\\users\\jd mamangun\\pycharmprojects\\pythonProject-JSON\\CONVERSATION.txt","w") as convo:
#     convo.write("Sam: hello Dean")
#     convo.write("\nDean: hi Sam")
#     convo.write("\nSam: Where's Castiel?")
#     convo.write("\nDean: idk. go figure.")

with open("c:\\users\\jd mamangun\\pycharmprojects\\pythonProject-JSON\\CONVERSATION.txt","r") as convo:
    for line in convo:
        words=line.split(" ")
        with open("c:\\users\\jd mamangun\\pycharmprojects\\pythonProject-JSON\\CONVERSATION_with_word-count.txt",
                  "a") as convoWC:
            convoWC.write("wordcount:" + str(len(words)) + " " + line)


