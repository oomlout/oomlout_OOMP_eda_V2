
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "L200"
    hexID = "SZKREGULATORLINEARL2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L200', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-5_P3.4x3.8mm_StaggerOdd_Lead7.13mm_TabDown', 'kicadSymbolDatasheet': 'http://www.zen22142.zen.co.uk/Circuits/Power/l200.pdf', 'kicadSymbolki_keywords': '2A Regulator Adjustable Positive', 'kicadSymbolki_description': 'Adjustable voltage and current regulator, 2A, 36V', 'kicadSymbolki_fp_filters': 'TO?220*StaggerOdd*'}])
    newPart['name'].append('L200')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

