
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "Molex_502244-2430_1x24-1MP_P0.5mm_Horizontal"
    hexID = "FZKCNFFCFPCMX522442431X241MPP5HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_502244-2430_1x24-1MP_P0.5mm_Horizontal', 'description': 'Molex 0.50mm Pitch Easy-On Type FFC/FPC Connector, For LVDS, 2.33mm Height, Right Angle, Surface Mount, ZIF, Bottom Contact Style, 24 Circuits (http://www.molex.com/pdm_docs/sd/5022441530_sd.pdf)', 'tags': 'molex FFC/FPC connector Pitch 0.5mm right angle', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Molex_502244-2430_1x24-1MP_P0.5mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : Molex_502244-2430_1x24-1MP_P0.5mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

