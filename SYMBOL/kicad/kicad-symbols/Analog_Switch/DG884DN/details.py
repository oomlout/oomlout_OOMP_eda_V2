
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "DG884DN"
    hexID = "SZKANALOGSWITCHDG884DN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DG884DN', 'kicadSymbolFootprint': 'Package_LCC:PLCC-44', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/70071/dg884.pdf', 'kicadSymbolki_keywords': 'CMOS Analog Switch Video Crosspoint', 'kicadSymbolki_description': '8 x 4 Wideband Video Crosspoint Array, 45Ohm Ron, PLCC-44', 'kicadSymbolki_fp_filters': 'PLCC?44*'}])
    newPart['name'].append('DG884DN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

