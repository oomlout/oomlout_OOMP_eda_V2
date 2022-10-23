
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Heatsink"
    oIndex = "Heatsink_AAVID_573300D00010G_TO-263"
    hexID = "FZKHHAAVID5733D1GTO263"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Heatsink_AAVID_573300D00010G_TO-263', 'description': 'Heatsink, 12.70mm x 26.16mm x 10.16, SMD, 18K/W, TO-263, D2 Pak, https://www.shopaavid.com/Product/573300D00000G', 'tags': 'Heatsink AAVID TO-263 D2 Pak', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Heatsink.3dshapes/Heatsink_AAVID_573300D00010G_TO-263.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Heatsink : Heatsink_AAVID_573300D00010G_TO-263')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

