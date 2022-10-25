
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "Jushuo_AFC07-S06FCA-00_1x6-1MP_P0.50_Horizontal"
    hexID = "FZKCNFFCFPCJUSHUOAFC7S6FCA1X61MPP5HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jushuo_AFC07-S06FCA-00_1x6-1MP_P0.50_Horizontal', 'description': 'Jushuo AFC07, FFC/FPC connector, AFC07-S06FCA-00, 6 Pins per row (https://datasheet.lcsc.com/lcsc/1811040204_JUSHUO-AFC07-S32FCC-00_C11061.pdf)', 'tags': 'connector jushuo horizontal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Jushuo_AFC07-S06FCA-00_1x6-1MP_P0.50_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : Jushuo_AFC07-S06FCA-00_1x6-1MP_P0.50_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

