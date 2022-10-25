
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "UFBGA_WLCSP-62"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSUFBGAWLCSP62"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UFBGA_WLCSP-62', 'description': 'https://www.nordicsemi.com/eng/nordic/download_resource/62726/14/67410332/13358', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('digikey-footprints : UFBGA_WLCSP-62')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

