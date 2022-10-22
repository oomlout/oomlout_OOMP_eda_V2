
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "USB_Mini_B_Female_548190519"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSUMBFEMALE54819519"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'USB_Mini_B_Female_548190519', 'tags': None, 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('digikey-footprints : USB_Mini_B_Female_548190519')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

