
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Power_Module"
    oIndex = "FP50R06W2E3"
    hexID = "SZKTRANSISTORPOWERMOFP5R6W2E3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A2C25S12M3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FP50R06W2E3', 'kicadSymbolFootprint': 'Transistor_Power_Module:Infineon_EasyPIM-2B', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-FP50R06W2E3-DS-v02_02-EN.pdf?fileId=db3a30431b3e89eb011b455c99987d24', 'kicadSymbolki_keywords': 'IGBT Power Module Trench Field Stop Technology', 'kicadSymbolki_description': '50A, 600V, 175W, 3-phase, Freewheeling Diode, Brake Chopper, Diode Rectifier, 5k NTC, EasyPIM-2B', 'kicadSymbolki_fp_filters': 'Infineon*EasyPIM*2B*'}])
    newPart['name'].append('FP50R06W2E3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

