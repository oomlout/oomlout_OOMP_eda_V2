
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "TLP2748"
    hexID = "SZKISOLATORTLP2748"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLP2748', 'kicadSymbolFootprint': 'Package_SO:SO-6L_10x3.84mm_P1.27mm', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=29407&prodName=TLP2748', 'kicadSymbolki_keywords': 'Photocouple highspeed inverting push-pull output', 'kicadSymbolki_description': '10-Mbps inverting photocouple,5 kVrms, 4.5 - 30 Vdd, push-pull output, SO-6L', 'kicadSymbolki_fp_filters': 'SO*6L*10x3.84mm*P1.27mm*'}])
    newPart['name'].append('Isolator : TLP2748')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

