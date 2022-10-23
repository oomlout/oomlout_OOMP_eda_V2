
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_RJ"
    oIndex = "RJ45_Abracon_ARJP11A-MA_Horizontal"
    hexID = "FZKCNRJRJ45ABRACONARJP11AMAHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RJ45_Abracon_ARJP11A-MA_Horizontal', 'description': 'Shielded RJ45 ethernet connector with transformer and POE (https://abracon.com/Magnetics/lan/ARJP11A.PDF)', 'tags': 'ethernet 8p8c transformer poe rj45', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Abracon_ARJP11A-MA_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_RJ : RJ45_Abracon_ARJP11A-MA_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

