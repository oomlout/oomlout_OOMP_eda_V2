
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF"
    oIndex = "Skyworks_SKY13575_639LF"
    hexID = "FZKRFSKYWORKSSKY13575639LF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Skyworks_SKY13575_639LF', 'description': 'http://www.skyworksinc.com/uploads/documents/SKY13575_639LF_203270D.pdf', 'tags': 'Skyworks', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF.3dshapes/Skyworks_SKY13575_639LF.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF : Skyworks_SKY13575_639LF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

