
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7606PBF"
    hexID = "SZKTRANSISTORFETIRF766PBF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7606PBF', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.irf.com/product-info/datasheets/data/irf7606pbf.pdf', 'kicadSymbolki_keywords': 'HexFET Power MOSFET P-MOS', 'kicadSymbolki_description': '-3.6A Id, -30V Vds, HexFET P-MOS Power MOSFET, Ronon 0.09R, Micro8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Transistor_FET : IRF7606PBF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

