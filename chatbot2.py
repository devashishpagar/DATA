responses = {
    "hi": "Hello,what is your name Sir/madam ?",
    "deva": "welcome to institute chatbot, How can help you? ",
    "services" : "1. admission  2. about campus   3.  courses  4.contact   5.address  6.fee",
    "admission" : "entrance score acceped 1.MHT-CET 2.JEE ",
    "courses" : "1.Engineering 2.MBA 3.Diploma 4.Pharmacy",
    "about campus" :"10-acers fully digital campus   lab available   canteen.......many more",
    "contact" : "1223345566",
    "address" : "adgaon,nashik-maharastra",
    "fee" : "1.enginnering 2.mba 3.diploma 4.pharmacy",
    "engineering" : "60000",
    "mba" : "60000",
    "diploma" : "60000",
    "pharmacy" : "60000",
	
    
    
}




def get_response(message):
    message = message.lower()
    if message in responses:
        return responses[message]
    else:
        return "I'm sorry, I don't understand that."





def main():
    print("Welcome to the chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(get_response(user_input))

            break
        else:
            print("Bot:", get_response(user_input))



if __name__ == "__main__":
    main()
