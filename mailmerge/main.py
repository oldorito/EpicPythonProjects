import os

#INSTRUCTION
#In the Input folder change the name list and the
#content of invitation. Remember to leave "[name]"
#in the template. 


current_directory = os.getcwd()
input_letters_path = os.path.join(current_directory, "Input/Letters/starting_letter.txt")
input_names_path = os.path.join(current_directory,"Input/Names/invited_names.txt")
output_letters_directory = os.path.join(current_directory, "Output/ReadyToSend/")

with open(input_letters_path) as letter:
    content = letter.read()

with open(input_names_path) as name_list:
    # name_list.readlines()
    letter_num = 0
    for name in name_list.readlines():
        invitation = content.replace("[name]", name.strip())
        new_file_path = f"{output_letters_directory}/letter_{letter_num}.txt"
        with open(new_file_path, "w") as new_letter_file:
            new_letter_file.write(invitation)
        letter_num += 1
