
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "TLV320AIC23BxQE"
    hexID = "SZKAUDIOTLV32AIC23BXQE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV320AIC23BxQE', 'kicadSymbolFootprint': 'Package_BGA:Texas_MicroStar_Junior_BGA-80_5.0x5.0mm_Layout9x9_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv320aic23b.pdf', 'kicadSymbolki_keywords': 'audio codec 2ch 96kHz headphone amplifier', 'kicadSymbolki_description': 'Stero Audio CODEC, 8- to 96-kHz, With Integrated Headphone Amplifier, BGA-32', 'kicadSymbolki_fp_filters': '*MicroStar*Junior*BGA*5*x5*mm*P0.5mm*'}])
    newPart['name'].append('Audio : TLV320AIC23BxQE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

