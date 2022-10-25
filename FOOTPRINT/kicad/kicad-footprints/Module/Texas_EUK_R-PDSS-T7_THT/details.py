
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Module"
    oIndex = "Texas_EUK_R-PDSS-T7_THT"
    hexID = "FZKMOTEXASEUKRPDSST7THT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_EUK_R-PDSS-T7_THT', 'description': 'Texas Instruments EUK 7 Pin Double Sided Module', 'tags': 'module pcb', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Module.3dshapes/Texas_EUK_R-PDSS-T7_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Module : Texas_EUK_R-PDSS-T7_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

