
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_3.5mm_CUI_SJ1-3535NG_Horizontal_CircularHoles"
    hexID = "FZKCNAUDIOJ35CUISJ13535NGHORIZONTALCIRCULARH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_3.5mm_CUI_SJ1-3535NG_Horizontal_CircularHoles', 'description': 'TRS 3.5mm, horizontal, through-hole, with switch, circular holes, https://www.cui.com/product/resource/sj1-353xng.pdf', 'tags': 'TRS audio jack stereo horizontal circular', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_3.5mm_CUI_SJ1-3535NG_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Connector_Audio : Jack_3.5mm_CUI_SJ1-3535NG_Horizontal_CircularHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

