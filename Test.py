def test(chapter):
  i = 1
  answered = False
  
  while "end" not in chapter[i]:
    print(chapter[i]["text"])
    for choice,choices in chapter[i]["choices"].items():
      print(choice, ":", choices["text"])
    while answered == False:
      answer = int(input())
      if answer in chapter[i]["choices"]:
        i = chapter[i]["choices"][answer]["path"]
        answered = True
      else:
        print("Sorry, that's not an option. Try again buddy. \n")
  print(chapter[i]["text"] + "\nend")

  