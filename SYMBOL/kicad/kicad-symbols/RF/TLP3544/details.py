
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF"
    oIndex = "TLP3544"
    hexID = "SZKRFTLP3544"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLP3543', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP3544', 'kicadSymbolFootprint': 'Package_DIP:DIP-6_W7.62mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=12661&prodName=TLP3544', 'kicadSymbolki_keywords': 'photocouplers photorelay solidstate relay normally opened (1-Form-A)', 'kicadSymbolki_description': 'Photo MOSFET optically coupled, ON 3.5A, 60mohm, OFF state 40V, Isolation 2500 VRMS, DIP-6', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('RF : TLP3544')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

