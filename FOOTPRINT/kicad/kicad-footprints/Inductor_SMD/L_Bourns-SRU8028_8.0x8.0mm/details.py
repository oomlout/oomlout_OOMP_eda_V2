
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Bourns-SRU8028_8.0x8.0mm"
    hexID = "FZKINDUCTORSMLBOURNSSRU8288X8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Bourns-SRU8028_8.0x8.0mm', 'description': 'Bourns SRU8028 series SMD inductor', 'tags': 'Bourns SRU8028 SMD inductor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Bourns-SRU8028_8.0x8.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Bourns-SRU8028_8.0x8.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

