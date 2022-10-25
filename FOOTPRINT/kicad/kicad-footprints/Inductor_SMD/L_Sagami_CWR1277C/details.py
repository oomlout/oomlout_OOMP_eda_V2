
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Sagami_CWR1277C"
    hexID = "FZKINDUCTORSMLSAGAMICWR1277C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Sagami_CWR1277C', 'description': 'Sagami power inductor, CWR1242C, H=7.7mm (http://www.sagami-elec.co.jp/file/16Car_SMDCwr.pdf)', 'tags': 'inductor sagami cwr12xx smd', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Sagami_CWR1277C.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Sagami_CWR1277C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

