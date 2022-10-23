
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay_SolidState"
    oIndex = "CPC1002N"
    hexID = "SZKRELAYSOLIDSTATECPC12N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CPC1002N', 'kicadSymbolFootprint': 'Package_SO:SOP-4_3.8x4.1mm_P2.54mm', 'kicadSymbolDatasheet': 'http://www.ixysic.com/home/pdfs.nsf/www/CPC1002N.pdf/$file/CPC1002N.pdf', 'kicadSymbolki_keywords': 'MOSFET Output Photorelay 1-Form-A', 'kicadSymbolki_description': 'Form A, Solid State Relay (Photo MOSFET) 60V, 0.7A, 0.55Ohm, SOP-4', 'kicadSymbolki_fp_filters': 'SOP*3.8x4.1mm*P2.54mm*'}])
    newPart['name'].append('CPC1002N')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

