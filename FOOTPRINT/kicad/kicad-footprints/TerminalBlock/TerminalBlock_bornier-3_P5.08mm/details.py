
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock"
    oIndex = "TerminalBlock_bornier-3_P5.08mm"
    hexID = "FZKTBTBBORNIER3P58"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_bornier-3_P5.08mm', 'description': 'simple 3-pin terminal block, pitch 5.08mm, revamped version of bornier3', 'tags': 'terminal block bornier3', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock.3dshapes/TerminalBlock_bornier-3_P5.08mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock : TerminalBlock_bornier-3_P5.08mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

