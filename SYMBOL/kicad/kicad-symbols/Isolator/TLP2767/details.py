
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TLP2767"
    hexID = "SZKISOLATORTLP2767"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP2767', 'kicadSymbolFootprint': 'Package_SO:SO-6L_10x3.84mm_P1.27mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=36717&prodName=TLP2767', 'kicadSymbolki_keywords': 'Photocouple highspeed non inverting push-pull output', 'kicadSymbolki_description': '50-Mbps high speed inverting photocouple,5 kVrms, 2.7 - 5.5 Vdd, push-pull output', 'kicadSymbolki_fp_filters': 'SO*6L*10x3.84mm*P1.27mm*'}])
    newPart['name'].append('Isolator : TLP2767')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

