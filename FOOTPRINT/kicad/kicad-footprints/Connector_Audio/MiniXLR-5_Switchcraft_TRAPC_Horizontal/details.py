
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "MiniXLR-5_Switchcraft_TRAPC_Horizontal"
    hexID = "FZKCNAUDIOMXLR5SWITCHCRAFTTRAPCHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MiniXLR-5_Switchcraft_TRAPC_Horizontal', 'description': 'http://www.switchcraft.com/ProductSummary.aspx?Parent=620 http://www.switchcraft.com/Drawings/TRAPC_X-TRASM_X_SERIES_CD.PDF', 'tags': 'THT Mini XLR 5Pin right angle', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/MiniXLR-5_Switchcraft_TRAPC_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : MiniXLR-5_Switchcraft_TRAPC_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

