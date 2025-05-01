import json

class first:
    def __init__(self,dataset):
        self.dataset1=self.load(dataset)

    def load(self,path):
        with open(path,'r')as file:
            data=json.load(file)
            return data  

    def get_data(self,user):
        user=user.lower()
        for item in self.dataset1:
            if item['question']==user:
                return item["answer"]
        return "Dont know how to respond."   
    def start(self):
        print("Chatbot: Hello! Type'quit' to end chat.")
        while True:
            user=input("You: ")
            if user.lower()=='quit':
                print("chatbot:you have Exited the chat")
                break
            response=self.get_data(user)
            print("chatbot: ",response)

if __name__ == "__main__" :
     bot=first("dataset.json")
     bot.start()
