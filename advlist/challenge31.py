wordbank= ["indentation", "spaces"] 
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
wordbank.append(4)
num = input("Give me a number between 0 and 20\n")
num = int(num)
chosen_student = tlgstudents[num]
print(f'{chosen_student} always uses {wordbank[2]} {wordbank[1]} to indent.')
