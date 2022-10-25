
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "Ethernet_Jack_ARJC02-111008B"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSETHERNETJARJC21118B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Ethernet_Jack_ARJC02-111008B', 'description': 'http://www.abracon.com/Magnetics/lan/Ethernet_Jack_ARJC02-111008B.PDF', 'tags': None, 'attributeType': None, 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('digikey-footprints : Ethernet_Jack_ARJC02-111008B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

