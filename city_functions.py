
def get_formatted_city(city, country):
    contents= f"{city}, {country}"
    return contents.title()

def get_formatted_city_people(city, country, people):
    contents= f"{city} - {country} - people {people}".title()
    return contents