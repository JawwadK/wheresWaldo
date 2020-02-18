#Name: Jawwad Khan
#Student No: 500895949
#Description: This program finds waldo given a scene by comparing target image to background throughout picture
#Date: November 26, 2018

bigScene = makePicture('scene.jpg')
smallScene = makePicture('tinyscene.jpg')
bigWaldo = makePicture('waldo.jpg')
smallWaldo = makePicture('tinywaldo.jpg')

#Function that compares template and search image at x1 and y1 and 
#calulates the SAD value at that point
def compareOne(template, searchImage, x1, y1):
  W = getWidth(template)
  H = getHeight(template)
  sum = 0

  for x in range(0,W):
    for y in range(0,H):
      pixel = getPixel(template,x,y)
      pixel1lumi = getRed(pixel)
      pixel2 = getPixel(searchImage,x1 + x,y1 + y)
      pixel2lumi = getRed(pixel2)
      sum += abs(int(pixel2lumi-pixel1lumi))
  return sum

#Function runs compareOne on every pixel within the searchImage, returns matrix of luminance difference values
def compareAll(template, searchImage):
  W = getWidth(template) 
  W2 = getWidth(searchImage) 
  H = getHeight(template) 
  H2 = getHeight(searchImage) 
  
  #making 2D matrix of same dimensions as picture
  matrix = [[999999 for i in range(W2)] for j in range(H2)]
  
  #setting limit for the search, so that search doesn't overgo 
  #the size of template as it goes through all pixels in picture 
  for x in range (W2 - W + 1):
    for y in range(H2 - H + 1):
      luminance = compareOne(template,searchImage,x,y)
      matrix[y][x] = luminance 
  return matrix
      
#Function that returns coordinate where the luminance difference is minimum (minrow,mincol)
def find2Dmin(matrix):
  mincol = 0
  minrow = 0
  for x in range(len(matrix)):
    for y in range(len(matrix[x])):
      #compare between current and min value(automatically first number in matrix) to see which is smaller
      if matrix[x][y] < matrix[mincol][minrow]:
        minrow = y
        mincol = x
  return(minrow,mincol)

#Function that displays a box around waldo when he is found 
def displayMatch(searchImage, x1, y1, w1, h1, color):
  H = h1
  W = w1
  border = 3
  for x in range(x1,W + x1):
    for y in range(y1,H + y1):
      if x not in range(x1 + border, W + x1 - border): 
        pixel = getPixel(searchImage,x,y)
        setColor(pixel,color)
      if y not in range(y1 + border, H + y1 - border):
        pixel = getPixel(searchImage,x,y)
        setColor(pixel,color)     
  return searchImage

#Function thats greyscales the image
def grayscale(picture):
  W = getWidth(picture)
  H = getHeight(picture)
  for x in range(W):
    for y in range(H):
      pixel = getPixel(picture,x,y)
      r = getRed(pixel)
      g = getGreen(pixel)
      b = getBlue(pixel)
      grayValue = (r + g + b)/3
      grayColor = makeColor(grayValue,grayValue,grayValue)
      setColor(pixel,grayColor)
  return picture
  
#Main function that runs all the helping functions to find waldo in background
def findWaldo(gTRG, gSRCH):
  #run the functions required to find waldo
  gTRG = grayscale(gTRG)
  gSRCH = grayscale(gSRCH)
  lumimatrix = compareAll(gTRG,gSRCH)
  mx,my = find2Dmin(lumimatrix)
  displayMatch(gSRCH, mx, my, getWidth(gTRG), getHeight(gTRG), yellow)
  

  #show the final image
  show(gSRCH)

