
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_RJ"
    oIndex = "RJ45_UDE_RB1-125B8G1A"
    hexID = "FZKCNRJRJ45UDERB1125B8G1A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RJ45_UDE_RB1-125B8G1A', 'description': '1 Port RJ45 Connector Through Hole 10/100/1000 Base-T, https://datasheet.lcsc.com/szlcsc/1901091107_UDE-Corp-RB1-125B8G1A_C363353.pdf#page=3', 'tags': 'RJ45 ethernet', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_UDE_RB1-125B8G1A.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_RJ : RJ45_UDE_RB1-125B8G1A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

