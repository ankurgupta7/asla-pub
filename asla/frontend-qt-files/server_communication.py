class ServerCommunication(object):
	def __init__(self):
		self.profile = Profile()
		self.atoken = 0
		self.model = Model()
	'''verifies if the aauthentication token expert enetered is valid'''
	def verifyAuthTokenFromServer(atoken):

	''' fetch user profile from server'''
	def fetchProfileFromServer():

	''' updates model for the user if its stale'''
	def updateModel():

	''' loads Global Model into memory. for faster calcualtion'''
    def loadGlobalModel():

    ''' gets global classfier model from the server and pickles it on user machine'''
    def getGlobalModelFromServer():

    