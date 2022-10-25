
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_BarrelJack"
    oIndex = "BarrelJack_CUI_PJ-036AH-SMT_Horizontal"
    hexID = "FZKCNBARRELJBARRELJCUIPJ36AHSHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BarrelJack_CUI_PJ-036AH-SMT_Horizontal', 'description': 'Surface-mount DC Barrel Jack, http://www.cui.com/product/resource/pj-036ah-smt.pdf', 'tags': 'Power Jack SMT', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_BarrelJack.3dshapes/BarrelJack_CUI_PJ-036AH-SMT_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_BarrelJack : BarrelJack_CUI_PJ-036AH-SMT_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

