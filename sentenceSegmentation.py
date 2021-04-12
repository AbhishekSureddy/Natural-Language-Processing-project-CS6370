from util import *
class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach i.e Assuming every sentence ends with pullstop.

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""
		segmentedText = text.split('.')

		return segmentedText
		
	def punkt(self, text):

		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		tokenizer = PunktSentenceTokenizer()
		segmentedText = tokenizer.tokenize(text)
		
		return segmentedText