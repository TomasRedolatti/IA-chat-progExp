# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
 
from pyswip import Prolog

class ActionInformLibraries(Action):

	def name(self) -> Text:
		return "action_inform_libraries"

	def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		prolog = Prolog()
		prolog.consult('../librerias.pl')  

		lenguaje = next(tracker.get_latest_entity_values("programming_lenguage"), None)

		if not lenguaje:
			msg = f"Necesito más información para poder ayudarte. Me podrias decir el nombre de la libreria?"
			dispatcher.utter_message(text=msg)
			return[]

		resultados = list(prolog.quey(f'libreria_de("{lenguaje}", X).'))
		bibliotecas = [resultado['X'] for resultado in resultados]
		return bibliotecas

class ActionLibraryInfo(Action):

	def name(self) -> Text:
		return "action_library_info"

	def run(self, dispatcher: CollectingDispatcher,
           tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		library = next(tracker.get_latest_entity_values("library"), None)

		if not library:
			msg = f"Para poder ayudarte, por favor necesito el nombre de la libreria."
			dispatcher.utter_message(text=msg)
			return[]
		
		msg = f"Claro que puedo ayudarte con información sobre la libreria {library}."
		return[]

# Ejemplo de uso
#lenguaje = "Python"  # Esto podría provenir de la entidad detectada por Rasa
#respuesta = ActionInformLibraries()
#print(respuesta)  # Esto podría enviarse como respuesta a Rasa

# Aquí podrías implementar la integración con Rasa para enviar la respuesta adecuada

