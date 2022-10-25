
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "Oscillator_MEMS_SIT1533AI-H4-DCC-32.768E"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSOCSMEMSSIT1533AIH4DCC32768E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_MEMS_SIT1533AI-H4-DCC-32.768E', 'description': 'https://www.sitime.com/products/datasheets/sit1533/SiT1533-datasheet.pdf', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('digikey-footprints : Oscillator_MEMS_SIT1533AI-H4-DCC-32.768E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

