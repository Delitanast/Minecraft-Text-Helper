print("Choose a language:")
print("1. English - United Kingdom")
print("2. Русский - Россия")
print("3. Español - España")
print("4. Português - Portugal")
print("5. Português - Brazil")
Language = int(input("Type number of language: "))
if Language == 1:
  print("")
  print("Hello! I am Minecraft text helper Damir. You can ask me your   question? and I can answer your question.")
  print("")
  print("Type command: (For help type /help)")
  print("")
  Question = str(input(""))
if Language == 2:
  print("")
  print("Привет! Я твой текстовый помощник по Minecraft Дамир. Ты можешьзадать свой вопрос, а я могу на него ответить.")
  print("")
  print("Type command: (For help type /help)")
  print("")
  Question = str(input(""))
if Language == 3:
  print("")
  print("Hola! Soy tu asistente de Texto para Minecraft Damir. Puedes   hacer tu propia pregunta y yo puedo responderla.")
  print("")
  print("Type command: (For help type /help)")
  print("")
  Question = str(input(""))
if Language == 4:
  print("")
  print("Olá! Eu sou seu assistente de texto para Minecraft Damir. Podesfazer a tua pergunta e eu posso responder.")
  print("")
  print("Type command: (For help type /help)")
  print("")
  Question = str(input(""))
if Language == 5:
  print("")
  print("Olá! Eu sou seu assistente de texto para Minecraft Damir. Podesfazer a tua pergunta e eu posso responder.")
  print("")
  print("Type command: (For help type /help)")
  print("")
  Question = str(input(""))
if Question == "/help":
  if Language == 1:
    print("1. Whats your name?")
    Question = str(input(""))
  if Language == 2:
    print("1. Как тебя зовут?")
    Question = str(input(""))
  if Language == 3:
    print("1. ¿Cómo te llamas?")
    Question = str(input(""))
  if Language == 4:
    print("1. Como te chamas?")
    Question = str(input(""))
  if Language == 5:
    print("1. Como te chamas?")
    Question = str(input(""))
if Question == "Whats your name?":
  if Language == 1:
    print("My name is Damir.")
    Question = str(input(""))
  if Language == 2:
    print("Смените язык на английский язык.")
    Question = str(input(""))
  if Language == 3:
    print("Cambie el idioma al Inglés.")
    Question = str(input(""))
  if Language == 4:
    print("Mude o idioma para o inglês.")
    Question = str(input(""))
  if Language == 5:
    print("Mude o idioma para o inglês.")
    Question = str(input(""))
if Question == "Как тебя зовут?":
  if Language == 1:
    print("Change the language to Russian.")
    Question = str(input(""))
  if Language == 2:
    print("Меня зовут Дамир.")
    Question = str(input(""))
  if Language == 3:
    print("Cambie el idioma al ruso.")
    Question = str(input(""))
  if Language == 4:
    print("Mude o idioma para o russo.")
    Question = str(input(""))
  if Language == 5:
    print("Mude o idioma para o russo.")
    Question = str(input(""))
if Question == "¿Cómo te llamas?":
  if Language == 1:
    print("Change the language to Spanish.")
    Question = str(input(""))
  if Language == 2:
    print("Смените язык на испанский язык.")
    Question = str(input(""))
  if Language == 3:
    print("Me llamo Damir.")
    Question = str(input(""))
  if Language == 4:
    print("Mude o idioma para o espanhol.")
    Question = str(input(""))
  if Language == 5:
    print("Mude o idioma para o espanhol.")
    Question = str(input(""))
if Question == "Como te chamas?":
  if Language == 1:
    print("Change the language to Portuguese.")
    Question = str(input(""))
  if Language == 2:
    print("Смените язык на португальский.")
    Question = str(input(""))
  if Language == 3:
    print("Cambia el idioma al Portugués.")
    Question = str(input(""))
  if Language == 4:
    print("Chamo-me Damir.")
    Question = str(input(""))
