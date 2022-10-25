
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "RFM69W"
    hexID = "SZKRFMORFM69W"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RFM69HW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RFM69W', 'kicadSymbolFootprint': 'RF_Module:HOPERF_RFM69HW', 'kicadSymbolDatasheet': 'https://www.hoperf.com/data/upload/portal/20181127/5bfcbe34756e1.pdf', 'kicadSymbolki_keywords': 'Radio, ISM, Transceiver, Module, AES', 'kicadSymbolki_description': 'ISM Radio Transceiver Module, SPI interface', 'kicadSymbolki_fp_filters': 'HOPERF*RFM69HW*'}])
    newPart['name'].append('RF_Module : RFM69W')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

