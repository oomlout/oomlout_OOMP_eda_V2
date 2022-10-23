
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Security"
    oIndex = "ATECC608A-MAHDA"
    hexID = "SZKSECURITYATECC68AMAHDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATECC608A-MAHDA', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x2mm_P0.5mm_EP1.3x1.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/ATECC608A-CryptoAuthentication-Device-Summary-Data-Sheet-DS40001977B.pdf', 'kicadSymbolki_keywords': 'Cryptographic coprocessor', 'kicadSymbolki_description': 'Cryptographic Co-Processor with Secure Hardware-based 16 Key Storage, ECDSA and ECDH support, I2C, UDFN-8', 'kicadSymbolki_fp_filters': 'DFN*8*1EP*3x2mm*P0.5mm*'}])
    newPart['name'].append('ATECC608A-MAHDA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

