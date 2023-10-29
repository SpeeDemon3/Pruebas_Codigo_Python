import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Pruebas para la clase AnonymousSurvey"""

    def test_store_single_response(self):
        """Comprueba si una respuesta simple se guarda bien"""
        question = "What's your favorite programming language?" # Creamos la pregunta

        my_survey = AnonymousSurvey(question) # Instanciamos un objeto de tipo AnonymousSurvey pasandole la pregunta
        my_survey.store_response('Python') # Utilizamos el metodo "store_response() para guardar la respuesta
        self.assertIn('Python', my_survey.responses) # Utilizando el metodo "assertIn() comprobamos si esta dentro de la lista

    def test_store_five_responses(self):
        """Comprueba si se guardan correctamente 5 respuestas basicas"""
        question = "What's your five favourite programming languages?"

        my_survey = AnonymousSurvey(question)
        responses = ['Python', 'Java', 'SQL']

        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()