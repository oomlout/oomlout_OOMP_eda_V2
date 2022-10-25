
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSB013NE2LXI"
    hexID = "SZKTRANSISTORFETBSB13NE2LXI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSB008NE2LX', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSB013NE2LXI', 'kicadSymbolFootprint': 'Package_DirectFET:DirectFET_MX', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BSB013NE2LXI-DS-v02_04-en.pdf?fileId=db3a30432e398416012e47a158802577', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '163A Id, 25V Vds, 1.3mOhm Rds, N-Channel MOSFET, DirectFET MX', 'kicadSymbolki_fp_filters': 'DirectFET*MX*'}])
    newPart['name'].append('Transistor_FET : BSB013NE2LXI')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

