
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay_SolidState"
    oIndex = "CPC1117N"
    hexID = "SZKRELAYSOLIDSTATECPC1117N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CPC1017N', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CPC1117N', 'kicadSymbolFootprint': 'Package_SO:SOP-4_3.8x4.1mm_P2.54mm', 'kicadSymbolDatasheet': 'http://www.ixysic.com/home/pdfs.nsf/www/CPC1117N.pdf/$file/CPC1117N.pdf', 'kicadSymbolki_keywords': 'MOSFET Output Photorelay 1-Form-B NC', 'kicadSymbolki_description': 'Form B, Solid State Relay (Photo MOSFET) 60V, 0.15A, 16Ohm, SO-4', 'kicadSymbolki_fp_filters': 'SOP*3.8x4.1mm*P2.54mm*'}])
    newPart['name'].append('CPC1117N')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

