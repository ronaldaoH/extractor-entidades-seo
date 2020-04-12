import requests

url = "https://entities.p.rapidapi.com/"

querystring = {"query":"{Desarrollo de sistemas a Medida - Empresa de desarrollo de software. . Desarrollo de sistemas a Medida. Desarrollo de Software a Medida. Metodologías de Desarrollo de Sistemas. Desarrollo de Software a la Medida. Desarrollo de Aplicaciones y Sistemas para Internet. -NECESITO UN SOFTWARE A LA MEDIDA-. Tecnologías que utilizamos. MARKETING DIGITAL. DESARROLLO DE PÁGINAS WEB. FABRICA DE SOFTWARE. . Nuestra empresa está enfocada al desarrollo de software, sistemas 100% personalizados, somos especialistas en programación de plataformas y aplicaciones web autoadministrables, estables y escalables, aportando soluciones prácticas a sus problemas. Ofrecemos los servicios de implementación de software en diversas tecnologías, cumpliendo con los estándares internacionales de calidad y metodologías.}"}

headers = {
    'x-rapidapi-host': "entities.p.rapidapi.com",
    'x-rapidapi-key': "a2e96ae540msh48131f24921eb19p1751d1jsn09590d8d1f66"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)