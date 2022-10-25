
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_THT"
    oIndex = "DX_5R5VxxxxU_D11.5mm_P5.00mm"
    hexID = "FZKCDX5R5VXXXXUD115P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DX_5R5VxxxxU_D11.5mm_P5.00mm', 'description': 'CP, Radial series, Radial, pin pitch=5.00mm, diameter=11.5mm, Supercapacitor, http://www.elna.co.jp/en/capacitor/double_layer/catalog/pdf/dx_e.pdf', 'tags': 'CP Radial series Radial pin pitch 5.00mm diameter 11.5mm supercapacitor', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_THT.3dshapes/DX_5R5VxxxxU_D11.5mm_P5.00mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Capacitor_THT : DX_5R5VxxxxU_D11.5mm_P5.00mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

