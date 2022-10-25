
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TLP185xSE"
    hexID = "SZKISOLATORTLP185XSE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLP185', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP185xSE', 'kicadSymbolFootprint': 'Package_SO:SOIC-4_4.55x3.7mm_P2.54mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=14111&prodName=TLP185(SE', 'kicadSymbolki_keywords': 'NPN DC Optocoupler', 'kicadSymbolki_description': 'DC Optocoupler, Vce 80V, CTR 50-100%, MFSOP6', 'kicadSymbolki_fp_filters': 'SOIC*4.55x3.7mm*P2.54mm*'}])
    newPart['name'].append('Isolator : TLP185xSE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

