
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Mini-Circuits_FG873-4_3x3mm"
    hexID = "FZKDFNMCIRCUITSFG87343X3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mini-Circuits_FG873-4_3x3mm', 'description': 'Mini Circuits Case style FG (https://ww2.minicircuits.com/case_style/FG873.pdf)', 'tags': 'FG873', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Mini-Circuits_FG873-4_3x3mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : Mini-Circuits_FG873-4_3x3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

