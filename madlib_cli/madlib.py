
print("Welcome to the Madlib ")
print("To get started, simply fill in the blanks with different types of words.")
print("Once you've filled in all the blanks, the program will generate a funny story using your words!")

def read_template(path):
    try:
       with open(path,"r") as file1:
         #print(file1.read())
         return file1.read()

    except FileNotFoundError:
       raise FileNotFoundError(f"No such file or directory: '{path}'")

#read_template("assets/dark_and_stormy_night_template.txt")
#read_template("assets/Madlib_template.txt")

def parse_template(content):
    array = []
    text = ""
    index = 0
    while index < len(content):
        if content[index] == "{":
            close = content.find("}", index)
            try:
                close == -1
            except:
                raise ValueError("Invalid")
            part = content[index+1:close]
            array.append(part)
            text += "{}"
            index = close + 1
        else: 
            text += content[index]
            index += 1
    #print(text, tuple(array))
    return text, tuple(array) # creates a new tuple object from the array
    


def merge(template, values):
    Sections = template.split('{}')
    #print (Sections)
    
    output = Sections[0]
    i = 0
    while i < len(values):
        output += str(values[i]) + Sections[i+1]
        i += 1
    print (output)
    with open("assets/dark_copy.txt","w") as file:
        file.write(output)
    return output




if __name__ =='__main__':
  #output = parse_template("It was a {Adjective} and {Adjective} {Noun}.")
  output = parse_template(read_template("assets/Madlib_template.txt"))
  values = []
  for i in output[1]:
    value = str(input ("Enter a " + i +" "))
    values.append(value)
  #print (values)


  #merge("It was a {} and {} {}.", values)
  merge(output[0],values)