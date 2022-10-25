
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF"
    oIndex = "LBB110"
    hexID = "SZKRFLBB11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLP222A-2', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LBB110', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.ixysic.com/home/pdfs.nsf/www/LBB110.pdf/$file/LBB110.pdf', 'kicadSymbolki_keywords': 'Dual MOSFET Output Photorelay 1-Form-B', 'kicadSymbolki_description': 'Dual Single-Pole, Normally Closed OptoMOS® Relay, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('RF : LBB110')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

