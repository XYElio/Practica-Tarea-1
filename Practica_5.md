# <span style="color: #1D6F58; font-weight: bold;">Práctica 5</span>


## <span style="color: #2A2929; font-weight: bold;">Enunciado del Problema:</span>
> Obtener el producto de dos números enteros positivos mediante sumas sucesivas.

## <span style="color: #2A2929; font-weight: bold;">Análisis:</span>
> * Leer dos números enteros positivos, n1 y n2.
> * Inicializas una variable producto en 0.
> * Usas un bucle para repetir la suma de n1 en producto exactamente n2 veces.
> * Al final del bucle, el valor de producto contendrá el producto de los dos números.


## <span style="color: #2A2929; font-weight: bold;">Diagrama de Flujo de Datos (DFD):</span>
**WHILE**
<p align="center">
  <img src="Imagenes/25.1.png"  width="600" height="500">
</p>

**DO WHILE**
<p align="center">
  <img src="Imagenes/25.2.png"  width="600" height="500">
</p>

**FOR**
<p align="center">
  <img src="Imagenes/25.3.png"  width="600" height="500">
</p>

## <span style="color: #2A2929; font-weight: bold;">Prueba de Escritorio</span>
<table style="float: left;border-collapse:collapse;border:none;margin-left:4.8pt;margin-right:4.8pt;">
    <tbody>
        <tr>
            <td style="width: 43.05pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>i</span></strong></p>
            </td>
            <td style="width: 54.2pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>num1&nbsp;</span></strong></p>
            </td>
            <td style="width: 59.05pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>num1&gt;0</span></strong></p>
            </td>
            <td style="width: 46.85pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>num2</span></strong></p>
            </td>
            <td style="width: 55.15pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>num2&gt;0</span></strong></p>
            </td>
            <td style="width: 71.6pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>i&lt;=num2</span></strong></p>
            </td>
            <td style="width: 54.2pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>prod += num2</span></strong></p>
            </td>
            <td style="width: 57.8pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>i++</span></strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 43.05pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>1</span></strong></p>
            </td>
            <td style="width: 54.2pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>2</span></p>
            </td>
            <td style="width: 59.05pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>2&gt;0 True</span></p>
            </td>
            <td style="width: 46.85pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>2</span></p>
            </td>
            <td style="width: 55.15pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>2&gt;0 True</span></p>
            </td>
            <td style="width: 71.6pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>1 &lt;= 2 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>2 &lt;= 2 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>3 &lt;=2 False</span></p>
            </td>
            <td style="width: 54.2pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>= 0 +2</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>= 4(2 + 2)</span></p>
            </td>
            <td style="width: 57.8pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>=2(1+1)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>=3(2+1)</span></p>
            </td>
        </tr>
    </tbody>
</table>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong>WHILE</strong></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong>DO WHILE</strong></p>
<table style="border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 56pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>num1&nbsp;</span></strong></p>
            </td>
            <td style="width: 59.85pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>num1&gt;0</span></strong></p>
            </td>
            <td style="width: 47.75pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>num2</span></strong></p>
            </td>
            <td style="width: 55.45pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>num2&gt;0</span></strong></p>
            </td>
            <td style="width: 56pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>prod += num2</span></strong></p>
            </td>
            <td style="width: 47.05pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>i</span></strong></p>
            </td>
            <td style="width: 58.85pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>i++</span></strong></p>
            </td>
            <td style="width: 60.95pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>i&lt;=num2</span></strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 56pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>2</span></strong></p>
            </td>
            <td style="width: 59.85pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>2&gt;0 True</span></p>
            </td>
            <td style="width: 47.75pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>2</span></p>
            </td>
            <td style="width: 55.45pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>2&gt;0 True</span></p>
            </td>
            <td style="width: 56pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>= 0 +2</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>= 4(2 + 2)</span></p>
            </td>
            <td style="width: 47.05pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>1</span></p>
            </td>
            <td style="width: 58.85pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>=2(1+1)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>=3(2+1)</span></p>
            </td>
            <td style="width: 60.95pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>1 &lt;= 2 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>2 &lt;= 2 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>3 &lt;=2 False</span></p>
            </td>
        </tr>
    </tbody>
</table>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong>FOR</strong></p>
<table style="border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 48.6pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>num1&nbsp;</span></strong></p>
            </td>
            <td style="width: 56.5pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>num1&gt;0</span></strong></p>
            </td>
            <td style="width: 44.2pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>num2</span></strong></p>
            </td>
            <td style="width: 63.35pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>num2&gt;0</span></strong></p>
            </td>
            <td style="width: 127.55pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>i = 1; &nbsp; i &lt;= num1; &nbsp; i++</span></strong></p>
            </td>
            <td style="width: 92.15pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>prod += num2</span></strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 48.6pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-family:"Arial",sans-serif;color:black;'>2</span></strong></p>
            </td>
            <td style="width: 56.5pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>2&gt;0 True</span></p>
            </td>
            <td style="width: 44.2pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>2</span></p>
            </td>
            <td style="width: 63.35pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>2&gt;0 True</span></p>
            </td>
            <td style="width: 127.55pt;border-top: none;border-left: none;border-bottom: 1pt solid rgb(255, 217, 102);border-right: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>i=1;1 &lt;= 2; 2(1+1) True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>&nbsp; &nbsp; &nbsp; 2 &lt;= 2; 3(2+1) True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>&nbsp; &nbsp; &nbsp; 3 &lt;=2 False</span></p>
            </td>
            <td style="width: 92.15pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1pt solid rgb(255, 217, 102);background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>= 0 +2</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>= 4(2 + 2)</span></p>
            </td>
        </tr>
    </tbody>
</table>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'>&nbsp;</p>

## Ejecución
<p align="center">
  <img src="Imagenes/5.png">
</p>
