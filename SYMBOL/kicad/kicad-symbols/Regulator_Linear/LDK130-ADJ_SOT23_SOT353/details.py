
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LDK130-ADJ_SOT23_SOT353"
    hexID = "SZKREGULATORLINEARLDK13ADJSOT23SOT353"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LDK130-ADJ_SOT23_SOT353', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.st.com/content/ccc/resource/technical/document/datasheet/29/10/f7/87/2f/66/47/f4/DM00076097.pdf/files/DM00076097.pdf/jcr:content/translations/en.DM00076097.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo adjustable positive low noise low quienscent current', 'kicadSymbolki_description': '300mA low dropout linear regulator, low quiescent current very, low noise, shutdown pin, adjustable positive output, SOT-23-5/SOT-353-5/SC-70-5', 'kicadSymbolki_fp_filters': 'SOT?23* SOT?353* *SC?70*'}])
    newPart['name'].append('Regulator_Linear : LDK130-ADJ_SOT23_SOT353')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

