
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JST"
    oIndex = "JST_JWPF_B06B-JWPF-SK-R_2x03_P2.00mm_Vertical"
    hexID = "FZKCNJSTJSTJWPFB6BJWPFSKR2X3P2VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JST_JWPF_B06B-JWPF-SK-R_2x03_P2.00mm_Vertical', 'description': 'JST JWPF series connector, B06B-JWPF-SK-R (http://www.jst-mfg.com/product/pdf/eng/eJWPF1.pdf), generated with kicad-footprint-generator', 'tags': 'connector JST JWPF side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JST.3dshapes/JST_JWPF_B06B-JWPF-SK-R_2x03_P2.00mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_JST : JST_JWPF_B06B-JWPF-SK-R_2x03_P2.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

