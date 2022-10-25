
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Security"
    oIndex = "ATECC608A-SSHDA"
    hexID = "SZKSECURITYATECC68ASSHDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATECC608A-SSHDA', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/ATECC608A-CryptoAuthentication-Device-Summary-Data-Sheet-DS40001977B.pdf', 'kicadSymbolki_keywords': 'Cryptographic coprocessor', 'kicadSymbolki_description': 'Cryptographic Co-Processor with Secure Hardware-based 16 Key Storage, ECDSA and ECDH support, I2C, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*8*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Security : ATECC608A-SSHDA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

