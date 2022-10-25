
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSB014N04LX3"
    hexID = "SZKTRANSISTORFETBSB14N4LX3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSB008NE2LX', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSB014N04LX3', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MX', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BSB014N04LX3G-DS-v02_03-en.pdf?fileId=db3a304320d39d590121a02c6c737a9b', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '180A Id, 40V Vds, 1.4mOhm Rds, N-Channel MOSFET, DirectFET MX', 'kicadSymbolki_fp_filters': 'DirectFET*MX*'}])
    newPart['name'].append('Transistor_FET : BSB014N04LX3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

