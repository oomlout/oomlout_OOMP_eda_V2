
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_RJ"
    oIndex = "RJ45_Amphenol_54602-x08_Horizontal"
    hexID = "FZKCNRJRJ45AMPHENOL5462X8HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RJ45_Amphenol_54602-x08_Horizontal', 'description': '8 Pol Shallow Latch Connector, Modjack, RJ45 (https://cdn.amphenol-icc.com/media/wysiwyg/files/drawing/c-bmj-0102.pdf)', 'tags': 'RJ45', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Amphenol_54602-x08_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_RJ : RJ45_Amphenol_54602-x08_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

