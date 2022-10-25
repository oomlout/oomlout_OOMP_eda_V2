
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_ACDC"
    oIndex = "Converter_ACDC_Hahn_HS-400xx_THT"
    hexID = "FZKCONCONHAHNHS4XXTHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_ACDC_Hahn_HS-400xx_THT', 'description': 'ACDC-Converter, 3W, Hahn-HS-400xx, THT https://www.schukat.com/schukat/schukat_cms_de.nsf/index/FrameView?OpenDocument&art=HS40009&wg=M7942', 'tags': 'Hahn ACDC-Converter THT', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_ACDC.3dshapes/Converter_ACDC_Hahn_HS-400xx_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_ACDC : Converter_ACDC_Hahn_HS-400xx_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

