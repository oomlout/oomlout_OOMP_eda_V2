
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TLP291"
    hexID = "SZKISOLATORTLP291"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP291', 'kicadSymbolFootprint': 'Package_SO:SOIC-4_4.55x2.6mm_P1.27mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=12884&prodName=TLP291', 'kicadSymbolki_keywords': 'NPN DC Optocoupler', 'kicadSymbolki_description': 'DC Optocoupler, Vce 80V, CTR 50-100%, SOP4', 'kicadSymbolki_fp_filters': 'SOIC*4.55x2.6mm*P1.27mm*'}])
    newPart['name'].append('Isolator : TLP291')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

