
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Murata_LQH55DN_5.7x5.0mm"
    hexID = "FZKINDUCTORSMLMLQH55DN57X5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Murata_LQH55DN_5.7x5.0mm', 'description': 'Inductor, SMD, 5.7x5.0x4.7mm, https://search.murata.co.jp/Ceramy/image/img/P02/JELF243A-0045.pdf', 'tags': 'inductor smd', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Murata_LQH55DN_5.7x5.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Murata_LQH55DN_5.7x5.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

