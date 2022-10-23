
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "Molex_502231-3300_1x33-1SH_P0.5mm_Vertical"
    hexID = "FZKCNFFCFPCMX52231331X331SHP5VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_502231-3300_1x33-1SH_P0.5mm_Vertical', 'description': 'Molex 0.50mm Pitch Easy-On Type FFC/FPC Connector, For LVDS, 6.05mm Height, Vertical, Surface Mount, ZIF, 33 Circuits (https://www.molex.com/pdm_docs/sd/5022313300_sd.pdf)', 'tags': 'molex FFC/FPC connector Pitch 0.5mm vertical', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Molex_502231-3300_1x33-1SH_P0.5mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_FFC-FPC : Molex_502231-3300_1x33-1SH_P0.5mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

