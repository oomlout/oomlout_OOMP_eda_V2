
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "STK672-080-E"
    hexID = "SZKDRIVERMOTORSTK6728E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STK672-080-E', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/EN6507-D.PDF', 'kicadSymbolki_keywords': 'Stepper driver', 'kicadSymbolki_description': 'Stepper motor driver with microstepping controller, 2.8A', 'kicadSymbolki_fp_filters': 'STK672-080-E'}])
    newPart['name'].append('Driver_Motor : STK672-080-E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

