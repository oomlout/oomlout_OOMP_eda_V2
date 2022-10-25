
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IRF7607PBF"
    hexID = "SZKTRANSISTORFETIRF767PBF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRF7607PBF', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.irf.com/product-info/datasheets/data/irf7607pbf.pdf', 'kicadSymbolki_keywords': 'HexFET Power MOSFET N-MOS', 'kicadSymbolki_description': '5.2A Id, 20V Vds, HexFET N-MOS Power MOSFET, Ronon 0.03R, Micro8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Transistor_FET : IRF7607PBF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

