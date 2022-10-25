
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "TSOT-23-5_HandSoldering"
    hexID = "FZKPACKAGETOSOTSMTSOT235HANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TSOT-23-5_HandSoldering', 'description': '5-pin TSOT23 package, http://cds.linear.com/docs/en/packaging/SOT_5_05-08-1635.pdf', 'tags': 'TSOT-23-5 Hand-soldering', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/TSOT-23-5.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_SMD : TSOT-23-5_HandSoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

