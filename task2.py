from PIL import Image, ImageDraw, ImageFont


import requests
import random

def funcd(x):

  url = 'https://api.quotable.io/random'

  r = requests.get(url)
  quote = r.json()
  #print(quote)
  # print(quote['content'])
  # print('     -',quote['author'])

  #variables for image size
  x1 = 612
  y1 = 612


#my quote
# sentence = "Everybody is a genius. But if you judge a fish by its ability to climb a tree, it will live its whole life believing that it is stupid. -Albert Einstein"
  sentence = f"{quote['content']}   \n  \n ~{quote['author']}"

  #choose a font
  fonts = ['./fonts/font1.ttf','./fonts/font1.ttf','./fonts/font2.ttf','./fonts/font3.ttf','./fonts/font4.ttf','./fonts/font5.ttf','./fonts/font6.ttf','./fonts/font7.ttf','./fonts/font8.ttf','./fonts/font9.ttf']
  # for i in fonts:
  fnt = ImageFont.truetype(fonts[random.randint(0,8)], 30)

  img = Image.new('RGB', (x1, y1), color = (10,10,10))
  d = ImageDraw.Draw(img)

  #find the average size of the letter
  sum = 0
  for letter in sentence:
    sum += d.textsize(letter, font=fnt)[0]

  average_length_of_letter = sum/len(sentence)

  #find the number of letters to be put on each line
  number_of_letters_for_each_line = (x1/1.618)/average_length_of_letter
  incrementer = 0
  fresh_sentence = ''

  #add some line breaks
  for letter in sentence:
    if(letter == '-'):
      fresh_sentence += '\n\n' + letter
    elif(incrementer < number_of_letters_for_each_line):
      fresh_sentence += letter
    else:
      if(letter == ' '):
        fresh_sentence += '\n'
        incrementer = 0
      else:
        fresh_sentence += letter
    incrementer+=1

  print(fresh_sentence)

  #render the text in the center of the box
  dim = d.textsize(fresh_sentence, font=fnt)
  x2 = dim[0]
  y2 = dim[1]

  qx = (x1/2 - x2/2)
  qy = (y1/2-y2/2)

  d.text((qx,qy), fresh_sentence ,align="center",  font=fnt, fill=(227, 222, 222))

  img.save(f'./img/quote{x}.jpg')

def funcw(x):

  url = 'https://api.quotable.io/random'

  r = requests.get(url)
  quote = r.json()
  #print(quote)
  # print(quote['content'])
  # print('     -',quote['author'])

  #variables for image size
  x1 = 612
  y1 = 612


#my quote
# sentence = "Everybody is a genius. But if you judge a fish by its ability to climb a tree, it will live its whole life believing that it is stupid. -Albert Einstein"
  sentence = f"{quote['content']}   \n  \n ~{quote['author']}"

  #choose a font
  fonts = ['./fonts/font1.ttf','./fonts/font1.ttf','./fonts/font2.ttf','./fonts/font3.ttf','./fonts/font4.ttf','./fonts/font5.ttf','./fonts/font6.ttf','./fonts/font7.ttf','./fonts/font8.ttf','./fonts/font9.ttf']
  # for i in fonts:
  fnt = ImageFont.truetype(fonts[random.randint(0,8)], 30)

  img = Image.new('RGB', (x1, y1), color = (255, 255, 255))
  d = ImageDraw.Draw(img)

  #find the average size of the letter
  sum = 0
  for letter in sentence:
    sum += d.textsize(letter, font=fnt)[0]

  average_length_of_letter = sum/len(sentence)

  #find the number of letters to be put on each line
  number_of_letters_for_each_line = (x1/1.618)/average_length_of_letter
  incrementer = 0
  fresh_sentence = ''

  #add some line breaks
  for letter in sentence:
    if(letter == '-'):
      fresh_sentence += '\n\n' + letter
    elif(incrementer < number_of_letters_for_each_line):
      fresh_sentence += letter
    else:
      if(letter == ' '):
        fresh_sentence += '\n'
        incrementer = 0
      else:
        fresh_sentence += letter
    incrementer+=1

  print(fresh_sentence)

  #render the text in the center of the box
  dim = d.textsize(fresh_sentence, font=fnt)
  x2 = dim[0]
  y2 = dim[1]

  qx = (x1/2 - x2/2)
  qy = (y1/2-y2/2)

  d.text((qx,qy), fresh_sentence ,align="center",  font=fnt, fill=(10,10,10))

  img.save(f'./img/quote{x}.jpg')

funcd(1)
funcw(2)
funcd(3)
funcw(4)
funcd(5)
funcw(6)
funcd(7)
funcw(8)
funcd(9)
funcw(10)
