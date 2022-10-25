
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_AVX_LMLP07A7"
    hexID = "FZKINDUCTORSMLAVXLMLP7A7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_AVX_LMLP07A7', 'description': 'Inductor, AVX Kyocera, LMLP Series, style D, 6.6mmx7.3mm, 3.0mm height. (Script generated with StandardBox.py) (https://datasheets.avx.com/LMLPD.pdf)', 'tags': 'Inductor LMLP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_AVX_LMLP07A7.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Inductor_SMD : L_AVX_LMLP07A7')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

