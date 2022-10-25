
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "JAE_FF0871SA1_2Rows-71Pins_P0.40mm_Horizontal"
    hexID = "FZKCNFFCFPCJAEFF871SA12ROWS71PINSP4HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JAE_FF0871SA1_2Rows-71Pins_P0.40mm_Horizontal', 'description': 'Molex JAE 0.2mm pitch, 1mm overall height FFC/FPC connector, FF0871SA1, 71 Circuits (http://www.jae.com/z-en/pdf_download_exec.cfm?param=SJ108178.pdf), generated with kicad-footprint-generator', 'tags': 'connector JAE  top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/JAE_FF0871SA1_2Rows-71Pins_P0.40mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : JAE_FF0871SA1_2Rows-71Pins_P0.40mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

