
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "ESD9B5.0ST5G"
    hexID = "SZKDIODEESD9B5ST5G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'ESD9B5.0ST5G', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-923', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/ESD9B-D.PDF', 'kicadSymbolki_keywords': 'diode TVS ESD', 'kicadSymbolki_description': 'ESD protection diode, 5.0Vrwm, SOD-923', 'kicadSymbolki_fp_filters': 'D*SOD?923*'}])
    newPart['name'].append('ESD9B5.0ST5G')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

