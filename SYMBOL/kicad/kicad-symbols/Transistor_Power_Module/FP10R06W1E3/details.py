
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Power_Module"
    oIndex = "FP10R06W1E3"
    hexID = "SZKTRANSISTORPOWERMOFP1R6W1E3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A2C25S12M3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FP10R06W1E3', 'kicadSymbolFootprint': 'Transistor_Power_Module:Infineon_EasyPIM-1B', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-FP10R06W1E3-DS-v02_01-en_de.pdf?fileId=db3a304412b407950112b43312285a63', 'kicadSymbolki_keywords': 'IGBT Power Module Trench Field Stop Technology M series', 'kicadSymbolki_description': '10A, 600V, 68W, 3-phase, Freewheeling Diode, Brake Chopper, Diode Rectifier, 5k NTC, EasyPIM-1B', 'kicadSymbolki_fp_filters': 'Infineon*EasyPIM*1B*'}])
    newPart['name'].append('FP10R06W1E3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

