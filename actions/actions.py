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
		prolog.consult('/home/tomas/Documentos/materias-actuales/programacion_exploratoria/proyectos/trabajo-practico/librerias.pl')
		library = next(tracker.get_latest_entity_values("library"), None)

		if not library:
			msg1 = f"Para poder ayudarte, decime sobre que libreria necesitas información."
			dispatcher.utter_message(text=msg1)
			return []


		result = bool(list(prolog.query(f"libreria( {library}, _, _, _)")))

		if result:   #Si se encuentra la libreria en la BD
			msg2 = f"Claro puedo ayudarte con la libreria {library}."
			dispatcher.utter_message(text=msg2)

			for description in prolog.query("libreria("+ library +", L, U, D)"):
				rta = f"{description['D']}"
				dispatcher.utter_message(text=rta)

			return []
		else:		
			msg3 = f"Los siento, no tengo información sobre la libreria {library}."
			dispatcher.utter_message(text=msg3)

			return []
	
		return []

class ActionInformLibraries(Action):

	def name(self) -> Text:
		return "action_inform_libraries"
	
	def run(self, dispatcher: CollectingDispatcher, 
		 tracker: Tracker, 
		 domain: DomainDict) -> Coroutine[Any, Any, List[Dict[Text, Any]]]:
		
		prolog = Prolog()
		prolog.consult('/home/tomas/Documentos/materias-actuales/programacion_exploratoria/proyectos/trabajo-practico/librerias.pl')
		language = next(tracker.get_latest_entity_values("programming_language"), None)

		return []
