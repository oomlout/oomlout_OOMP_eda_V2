
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "MC100EPT22DT"
    hexID = "SZKINTERFACEMC1EPT22DT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC100EPT22DT', 'kicadSymbolFootprint': 'Package_SO:TSSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MC100EPT22-D.PDF', 'kicadSymbolki_keywords': 'PECL buffer interface', 'kicadSymbolki_description': '3.3 V Dual LVTTL/LVCMOS to Differential LVPECL Translator, TSSOP-8', 'kicadSymbolki_fp_filters': 'TSSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Interface : MC100EPT22DT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

