import re
import pyperclip
class phone_email_picker():
	def __init__ (self, pasting_documents): # Initializes the data
		self.pasting_documents = pasting_documents

	def phoneNumber(self):
		actual_number = []
		number_filter = re.compile(r'''(
	        (\d{3}|\(\d{3}\))?					# It is for area or country code
	        (\s|-|\.)?							# number separator by - or .
	        (\d{3})								# first 3 digits of the number
	        (\s|-|\.)							# number separator by - or .
	        (\d{4})								# last 4 digits of the number
	        (\s*(ext|x|ext.)\s*(\d{2,5}))?		# extension on an optional case
	        )''', re.VERBOSE)

		for groups in number_filter.findall(self.pasting_documents):
			phone_number_with_replacement = groups[0].replace(groups[0][3],'-')
			actual_number.append(phone_number_with_replacement)
		return actual_number

	def emailAddress(self):
		email_filter = re.compile(r'''(
			[a-zA-Z0-9._%+-]+			# username like nirajkharel of nirajkharel923@gmail.com
			@							# @ symbol, as usual
			[a-zA-Z0-9.-]+				# domain name, like gmail of nirajkharel923@gmail.com
			\.[a-zA-Z]{2,4}			    # may be like extension, like .com of nirajkharel923@gmail.com
			)''', re.VERBOSE)
		actual_email = email_filter.findall(self.pasting_documents)
		return actual_email

	def analyze_result(final_number, final_email):
		# Checking if both the list are empty or not
		if final_number == [] and final_email == []:
			final_number_email_copy = "Phone numbers and Email address not found."
			pyperclip.copy(str(final_number_email_copy))
			print("Done")

		# Declaring what to do if phone number exist and email dont.
		elif final_number == [] and final_email != []:
			final_number_email_copy = "Phone numbers not found!!"+"\n\n"+str(len(final_email))+" Email address found: "+ str(final_email)
			pyperclip.copy(str(final_number_email_copy))
			print("Done")

		# Declaring what to do if phone number does not exist and email does.
		elif final_number != [] and final_email == []:
			final_number_email_copy = str(len(final_number))+ " Phone numbers found: "+ str(final_number) +"\n\nEmail address not found!"
			pyperclip.copy(str(final_number_email_copy))
			print("Done")

		# Declaring what to do if both phone numbers and email address exists
		else:
			final_number_email_copy = str(len(final_number))+ " Phone numbers found: "+ str(final_number) +"\n\n"+ str(len(final_email))+" Email address found: "+ str(final_email)
			pyperclip.copy(str(final_number_email_copy))
			print("Done")

	analyze_result = staticmethod(analyze_result)

# Paste the data copied from the source which is stored on a variable and filtered on later.
pasting_documents = pyperclip.paste()

# Object of the class is initialize on variable copied_doc
copied_doc = phone_email_picker(pasting_documents)

# Methods phoneNumber() and emailAddress() are called using class object.
final_number = copied_doc.phoneNumber()
final_email = copied_doc.emailAddress()

# The method analyze_result belongs to class and not to the object it means
# we can define it as static method or clas method depending on whether we need to know which class we are part of.
# Since we don't need such information, we will go for staticmethod
phone_email_picker.analyze_result(final_number, final_email)
