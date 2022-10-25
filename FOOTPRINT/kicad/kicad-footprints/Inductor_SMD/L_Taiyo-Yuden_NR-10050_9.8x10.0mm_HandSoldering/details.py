
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Taiyo-Yuden_NR-10050_9.8x10.0mm_HandSoldering"
    hexID = "FZKINDUCTORSMLTAIYOYUDENNR1598X1HANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Taiyo-Yuden_NR-10050_9.8x10.0mm_HandSoldering', 'description': 'Inductor, Taiyo Yuden, NR series, Taiyo-Yuden_NR-10050, 9.8mmx10.0mm, https://ds.yuden.co.jp/TYCOMPAS/or/specSheet?pn=NR10050T1R3N', 'tags': 'inductor taiyo-yuden nr smd', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Taiyo-Yuden_NR-10050_9.8x10.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Taiyo-Yuden_NR-10050_9.8x10.0mm_HandSoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

