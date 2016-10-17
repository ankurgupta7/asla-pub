class LeapMotionInterface(object):
	'''gets leap motion hand data'''
    def getHandCoordinates():

    ''' open leapMotion port. automatically finds the port it is attached to '''
    def open():

    ''' does the calcullation on the model and predicts the label'''
    def predictForGesture(gesture):

    ''' starts recording from the Leap Motion'''    	
    def startRecording():
