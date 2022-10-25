
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "NCP349MNAM"
    hexID = "SZKPOWERPROTECTIONNCP349MNAM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCP349MN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP349MNAM', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-6-1EP_2x1.6mm_P0.5mm_EP1.15x1.3mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pdf/datasheet/ncp349-d.pdf', 'kicadSymbolki_keywords': 'overvoltage protection', 'kicadSymbolki_description': '28V Positive Overvoltage Protection Controller, DFN-6', 'kicadSymbolki_fp_filters': 'DFN*1EP*2x1.6mm*P0.5mm*'}])
    newPart['name'].append('Power_Protection : NCP349MNAM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

