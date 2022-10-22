
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "Phototransistor_4.4x1.5mm_P2.54_Radial"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSPHOTOTRANSISTOR44X15P254R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Phototransistor_4.4x1.5mm_P2.54_Radial', 'description': 'http://optoelectronics.liteon.com/upload/download/DS20-2000-343/1CHKxKNN.pdf', 'tags': None, 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('digikey-footprints : Phototransistor_4.4x1.5mm_P2.54_Radial')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

