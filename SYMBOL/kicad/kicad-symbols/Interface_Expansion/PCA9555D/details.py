
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "PCA9555D"
    hexID = "SZKINTERFACEEXPANSIONPCA9555D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCA9555D', 'kicadSymbolFootprint': 'Package_SO:SOIC-24W_7.5x15.4mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PCA9555.pdf', 'kicadSymbolki_keywords': 'I2C TWI IO expander', 'kicadSymbolki_description': 'IO expander 16 GPIO, I2C 400kHz, Interrupt, 2.3 - 5.5V, SOIC-24', 'kicadSymbolki_fp_filters': 'SOIC*7.5x15.4mm*P1.27mm*'}])
    newPart['name'].append('Interface_Expansion : PCA9555D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

