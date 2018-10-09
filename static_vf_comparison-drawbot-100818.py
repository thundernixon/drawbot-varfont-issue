rect(0,0,1000,1000)

testString = "Lorem \nTestem \n845"
setLineHeight = 260
setFontSize = 250
xPos, yPos = 80, 664

lineHeight(setLineHeight)

# linking a specific font file for testing
font("EncodeSans-Regular.ttf", setFontSize)

fill(1,0,1)

text(testString, (xPos, yPos))

# Linking a specific font file for testing. The text() method fails for this font, even though the font works as expected in FontView and on Axis-Praxis.org
font("EncodeSans-mathfix-normal_wdth-VF.ttf", setFontSize)

# # It *does* work if I link to another variable font, such as Avenir Next Variable.
# font("AvenirNext_Variable.ttf", setFontSize)


for axis, data in listFontVariations().items():
    print((axis, data))

# when I set the fontVariations, the following text() method fails with NSInvalidArgumentException
fontVariations(wght=400.0,wdth=500.0)

blendMode("screen")
fill(0,.75,1)

# I recieve a NSInvalidArgumentException here, which Apple describes as "Name of an exception that occurs when you pass an invalid argument to a method, such as a nil pointer where a non-nil object is required." However, I only receive this error when I set the font variations of the above variable font. So, the arguments should be valid.
text(testString, (xPos, yPos))
