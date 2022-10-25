
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "STK672-040-E"
    hexID = "SZKDRIVERMOTORSTK6724E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STK672-040-E', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/EN5227-D.PDF', 'kicadSymbolki_keywords': 'Stepper driver', 'kicadSymbolki_description': 'Stepper motor driver with microstepping controller, 1.5A', 'kicadSymbolki_fp_filters': 'STK672-040-E'}])
    newPart['name'].append('Driver_Motor : STK672-040-E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

