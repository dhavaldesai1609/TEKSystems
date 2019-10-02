import requests


class Geography(object):

    def __init__(self, name=None, code=None):
        self.name = name
        self.code = code
        self.code_url = 'https://restcountries.eu/rest/v2/callingcode/%s' % self.code
        self.name_url = url = 'https://restcountries.eu/rest/v2/name/%s' % self.name

    def __call__(self, *args, **kwargs):
        self.get_capital_city()

    def get_capital_city(self):
        url = self.code_url
        if self.name:
            url = self.name_url
        resp = requests.get(url)
        if resp.status_code == 200 and resp.json()[0].get('capital'):
            result = resp.json()[0]['capital']
        else:
            result = "Invalid City name or City Not Found"

        return result


if __name__ == '__main__':
    print('Type "q" to exit.')
    while True:
        city = ''
        city_name = ''
        city_code = ''
        try:
            city = input("Please enter city name or code: ")
            city_code = int(city)
        except ValueError:
            city_name = city

        if city_name == 'q':
            break
        if not city:
            print('Please provide city name or code.')
            continue
        geo = Geography(name=city_name, code=city_code)
        geo()
