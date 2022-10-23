
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_RJ"
    oIndex = "RJ45_OST_PJ012-8P8CX_Vertical"
    hexID = "FZKCNRJRJ45OSTPJ128P8CXVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RJ45_OST_PJ012-8P8CX_Vertical', 'description': 'RJ45 vertical connector https://www.on-shore.com/wp-content/uploads/PJ012-8P8CX.pdf', 'tags': 'RJ45 PJ012', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_OST_PJ012-8P8CX_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_RJ : RJ45_OST_PJ012-8P8CX_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

