
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Power_Module"
    oIndex = "FP25R12W2T4"
    hexID = "SZKTRANSISTORPOWERMOFP25R12W2T4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A2C25S12M3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FP25R12W2T4', 'kicadSymbolFootprint': 'Transistor_Power_Module:Infineon_EasyPIM-2B', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-FP25R12W2T4-DS-v02_02-EN.pdf?fileId=db3a3043163797a60116389cdaeb0183', 'kicadSymbolki_keywords': 'IGBT Power Module Trench Field Stop Technology', 'kicadSymbolki_description': '25A, 1200V, 175W, 3-phase, Freewheeling Diode, Brake Chopper, Diode Rectifier, 5k NTC, EasyPIM-2B', 'kicadSymbolki_fp_filters': 'Infineon*EasyPIM*2B*'}])
    newPart['name'].append('FP25R12W2T4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

