
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "ECS-2520MV-xxx-xx"
    hexID = "SZKOCSECS252MVXXXXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'ECS-2520MV-xxx-xx', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_ECS_2520MV-xxx-xx-4Pin_2.5x2.0mm', 'kicadSymbolDatasheet': 'https://www.ecsxtal.com/store/pdf/ECS-2520MV.pdf', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator ECS SMD', 'kicadSymbolki_description': 'HCMOS Crystal Clock Oscillator, 2.5x2.0 mm SMD', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*ECS*2520MV*2.5x2.0mm*'}])
    newPart['name'].append('ECS-2520MV-xxx-xx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

