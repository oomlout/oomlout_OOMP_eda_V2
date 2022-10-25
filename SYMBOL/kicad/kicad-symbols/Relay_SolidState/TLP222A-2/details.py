
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay_SolidState"
    oIndex = "TLP222A-2"
    hexID = "SZKRELAYSOLIDSTATETLP222A2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP222A-2', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=17036&prodName=TLP222A', 'kicadSymbolki_keywords': 'Dual MOSFET Output Photorelay 1-Form-A', 'kicadSymbolki_description': 'Dual MOSFET Photorelay 1-Form-A, Voff 60V, Ion 0,5A, DIP8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Relay_SolidState : TLP222A-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

