def tokenize_text(text):
    tokens = text.split()
    return tokens

def count_words(tokens):
    wc = {}
    for token in tokens:
        if token.lower() in wc:
            wc[token.lower()] += 1
        else:
            wc[token.lower()] = 1
    return wc

def display_word_count(word_count):
    print("Word Frequency")
    print("======================")
    for word, count in word_count.items():
        print(f"{word}\t\t{count}")

text = '''
Se encargará de diseñar, desarrollar e implementar aplicaciones web y sistemas backend con tecnologías como SQL Server, ASP.NET, C#, Node.js, Angular y Python. El objetivo es asegurar el funcionamiento, seguridad y escalabilidad de las soluciones tecnológicas, optimizando los procesos internos.

Ofrecemos
Horario de 8:00 am - 4:00 pm
Prestaciones de ley
Salario competiivo

Requerimos
Conocimientos en lenguajes y tecnologías como:
ASP.NET, .NET Core, C#, Node.js, JavaScript, TypeScript, Angular (versión reciente), Python (INDISPENSABLE)
Bases de Datos y Backend:
SQL Server, API RESTful,
Herramientas y Control de Versiones:
Git, GitHub/GitLab, Docker (deseable), CI/CD, despliegue en Azure o AWS.
Mínimo 1 año de experiencia en puestos similares (Indispensable)
Últimos años de estudios en Ingeniería en Sistemas o carrera a fin
'''

token_list = tokenize_text(text)
word_count = count_words(token_list)
display_word_count(word_count)