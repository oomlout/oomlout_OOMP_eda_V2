
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "SparkFun-Eagle-Libraries"
    oDesc = "LilyPad-Wearables"
    oIndex = "PETAL-LARGE-2SIDE"
    hexID = "FZSLWPETALL2SIDE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('LilyPad-Wearables : PETAL-LARGE-2SIDE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

