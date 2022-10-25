
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_TDK_SLF7032"
    hexID = "FZKINDUCTORSMLTDKSLF732"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_TDK_SLF7032', 'description': 'Inductor, TDK, SLF7032, 7.0mmx7.0mm (Script generated with StandardBox.py) (https://product.tdk.com/info/en/document/catalog/smd/inductor_commercial_power_slf7032_en.pdf)', 'tags': 'Inductor TDK_SLF7032', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_TDK_SLF7032.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Inductor_SMD : L_TDK_SLF7032')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

