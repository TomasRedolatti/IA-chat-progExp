# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Coroutine, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from pyswip import Prolog, Query

class ActionLibraryInfo(Action):
    
	def name(self) -> Text:
		return "action_library_info"

	def run(self, dispatcher: CollectingDispatcher, 
		 	tracker: Tracker, 
			domain: DomainDict) -> Coroutine[Any, Any, List[Dict[Text, Any]]]:
		prolog = Prolog()
		prolog.consult('../librerias.pl')
		lenguage = next(tracker.get_latest_entity_values("programming_lenguage"), None)

		if not lenguage:
			msg = f"Para poder ayudarte, decime sobre que libreria necesitas información."
			dispatcher.utter_message(text=msg)
			return []
		
		if Prolog.query(libreria(lenguaje, _, _, _)):
			msg = f"Claro puedo ayudarte con la libreria {'lenguage'}."
			dispatcher.utter_message(text=msg)
			return []
	
		return []

