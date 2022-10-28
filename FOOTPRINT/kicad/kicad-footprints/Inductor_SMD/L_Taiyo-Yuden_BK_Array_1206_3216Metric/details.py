
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Taiyo-Yuden_BK_Array_1206_3216Metric"
    hexID = "FZKINDUCTORSMLTAIYOYUDENBKARRAY1263216METRIC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Taiyo-Yuden_BK_Array_1206_3216Metric', 'description': 'Ferrite Bead Array 4x0603, Taiyo Yuden BK Series (see https://www.yuden.co.jp/productdata/catalog/mlci09_e.pdf)', 'tags': 'ferrite bead array', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Taiyo-Yuden_BK_Array_1206_3216Metric.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Taiyo-Yuden_BK_Array_1206_3216Metric')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

