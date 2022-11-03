
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "IQD-Frequency-Products"
    oIndex = "CO-08-5"
    hexID = "FZEIQDFREQUENCYPRODUCTSCO85"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('IQD-Frequency-Products : CO-08-5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

