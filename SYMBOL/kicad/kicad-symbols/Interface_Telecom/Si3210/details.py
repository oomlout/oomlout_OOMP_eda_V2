
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Telecom"
    oIndex = "Si3210"
    hexID = "SZKINTERFACETELECOMSI321"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si3210', 'kicadSymbolFootprint': 'Package_SO:TSSOP-38_4.4x9.7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.mouser.com/ds/2/368/si3210-38974.pdf', 'kicadSymbolki_keywords': 'ProSLIC slic', 'kicadSymbolki_description': 'ProSLIC Programmable cmos slic/codec with ringing/battery voltage generation', 'kicadSymbolki_fp_filters': 'TSSOP*'}])
    newPart['name'].append('Si3210')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

