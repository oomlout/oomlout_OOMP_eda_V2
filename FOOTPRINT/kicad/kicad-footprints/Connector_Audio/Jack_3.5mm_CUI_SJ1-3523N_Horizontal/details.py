
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_3.5mm_CUI_SJ1-3523N_Horizontal"
    hexID = "FZKCNAUDIOJ35CUISJ13523NHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_3.5mm_CUI_SJ1-3523N_Horizontal', 'description': 'TRS 3.5mm, horizontal, through-hole, https://www.cuidevices.com/product/resource/pdf/sj1-352xn.pdf', 'tags': 'TRS audio jack stereo horizontal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_3.5mm_CUI_SJ1-3523N_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Audio : Jack_3.5mm_CUI_SJ1-3523N_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

