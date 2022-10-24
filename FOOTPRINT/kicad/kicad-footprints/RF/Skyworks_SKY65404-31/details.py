
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF"
    oIndex = "Skyworks_SKY65404-31"
    hexID = "FZKRFSKYWORKSSKY654431"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Skyworks_SKY65404-31', 'description': 'http://www.skyworksinc.com/uploads/documents/SKY65404_31_201512K.pdf', 'tags': 'Skyworks', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF.3dshapes/Skyworks_SKY65404-31.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('RF : Skyworks_SKY65404-31')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

