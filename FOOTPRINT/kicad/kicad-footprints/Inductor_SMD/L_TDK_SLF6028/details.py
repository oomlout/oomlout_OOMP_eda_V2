
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_TDK_SLF6028"
    hexID = "FZKINDUCTORSMLTDKSLF628"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_TDK_SLF6028', 'description': 'Inductor, TDK, SLF6028, 6.0mmx6.0mm (Script generated with StandardBox.py) (https://product.tdk.com/info/en/document/catalog/smd/inductor_commercial_power_slf6028_en.pdf)', 'tags': 'Inductor TDK_SLF6028', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_TDK_SLF6028.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Inductor_SMD : L_TDK_SLF6028')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

