formatter = "{} {} {} {}"
#Defines a variable with 4 {} to be formatted
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(

	"Try your",
	"Own text here",
	"Maybe a poem",
	"or a song about fear"

	))

#Calls the ".format" function to replace the {} with different variables. 