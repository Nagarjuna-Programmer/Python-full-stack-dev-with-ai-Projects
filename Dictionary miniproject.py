Dictionary = {}
while True:
    print("\nDictionary Management System")
    print("1. Add a word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete word")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        word=input("Enter the word : ").lower()
        meaning=input("Enter the meaning : ")
        Dictionary[word] = meaning
        print("Word added successfully!")
    elif choice == "2":
         word = input("Enter the word to serach ").lower()
         if word in Dictionary:
             print("Meaning : ",Dictionary[word])
         else :
             print("Word not found in the dictionary.")
    elif choice == "3":
        if Dictionary:
            print("All words in the dictionary:")
            for word, meaning in Dictionary.items():
                print(f"{word} : {meaning}")
        else:
            print("Dictionary is empty.")
    elif choice == "4":
         word = input("Enter the word to update meaning : ").lower()
         if word in Dictionary:
             new_meaning = input("Enter the new meaning : ")
             Dictionary[word] = new_meaning
             print("Meaning updated successfully!")
             print("Updated meaning :" ,{Dictionary[word]})
         else:
             print("Word not found in the dictionary.")
    elif choice == "5":
         word = input("Enter the word to delete : ").lower()
         if word in Dictionary:
             Dictionary.pop(word)
             print("Word deleted successfully!")
         else:
             print("Word not found in the dictionary.")
    elif choice == "6":
         print("Exiting...")
         break

    