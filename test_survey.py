import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Pruebas para la clase AnonymousSurvey"""

    def setUp(self): #El metodo "" crea una instancia y una lista que se podra utilizar en todas la funciones test que empiecen por "test_"
        """Crea una encuesta y un conjunto de respuestas para usar en todos los metodos de la prueba"""
        question = "What's your favorite programming language?"  # Creamos la pregunta
        self.my_survey = AnonymousSurvey(question)  # Instanciamos un objeto de tipo AnonymousSurvey pasandole la pregunta
        self.responses = ['Python', 'Java', 'SQL']

    def test_store_single_response(self):
        """Comprueba si una respuesta simple se guarda bien"""
        self.my_survey.store_response(self.responses[0]) # Utilizamos el metodo "store_response() para guardar la respuesta
        self.assertIn(self.responses[0], self.my_survey.responses) # Utilizando el metodo "assertIn() comprobamos si esta dentro de la lista

    def test_store_five_responses(self):
        """Comprueba si se guardan correctamente 5 respuestas basicas"""

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()