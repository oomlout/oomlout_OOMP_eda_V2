
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay_SolidState"
    oIndex = "CPC1017N"
    hexID = "SZKRELAYSOLIDSTATECPC117N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CPC1017N', 'kicadSymbolFootprint': 'Package_SO:SOP-4_3.8x4.1mm_P2.54mm', 'kicadSymbolDatasheet': 'http://www.ixysic.com/home/pdfs.nsf/www/CPC1017N.pdf/$file/CPC1017N.pdf', 'kicadSymbolki_keywords': 'MOSFET Output Photorelay 1-Form-A', 'kicadSymbolki_description': 'Form A, Solid State Relay (Photo MOSFET) 60V, 0.1A, 16Ohm, SO-4', 'kicadSymbolki_fp_filters': 'SOP*3.8x4.1mm*P2.54mm*'}])
    newPart['name'].append('Relay_SolidState : CPC1017N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

