
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "VL53L0CXV0DH_1"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSVL53LCXVDH1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VL53L0CXV0DH_1', 'description': 'http://www.st.com/content/ccc/resource/technical/document/datasheet/group3/b2/1e/33/77/c6/92/47/6b/DM00279086/files/DM00279086.pdf/jcr:content/translations/en.DM00279086.pdf', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('digikey-footprints : VL53L0CXV0DH_1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

