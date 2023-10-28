# <span style="color: #1D6F58; font-weight: bold;">Práctica 3</span>


## <span style="color: #2A2929; font-weight: bold;">Enunciado del Problema:</span>
> π(i) desde i = 2 hasta 2n
Generar en while,do while ,for.

## <span style="color: #2A2929; font-weight: bold;">Análisis:</span>
> * Pedir el valor de 2n y verificar que sea positivo.
> * Inicializas una variable producto en 0.
> * Usas un bucle para repetir la variable hasta que se cumpla las condiciones.
> * Al final del bucle, el valor de producto contendrá el producto de 2n.



## <span style="color: #2A2929; font-weight: bold;">Diagrama de Flujo de Datos (DFD):</span>
**WHILE**
<p align="center">
  <img src="Imagenes/23.1.png"  width="600" height="500">
</p>

**DO WHILE**
<p align="center">
  <img src="Imagenes/23.2.png"  width="600" height="500">
</p>

**FOR**
<p align="center">
  <img src="Imagenes/23.3.png"  width="600" height="500">
</p>

## <span style="color: #2A2929; font-weight: bold;">Prueba de Escritorio</span>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style='font-size:16px;line-height:107%;font-family:"Arial",sans-serif;'>WHILE</span></strong></p>
<table style="width:425.0pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 23.85pt;border-top: none;border-left: 1pt solid windowtext;border-bottom: 1.5pt solid rgb(255, 217, 102);border-right: none;background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>n</span></strong></p>
            </td>
            <td style="width: 19.05pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i</span></strong></p>
            </td>
            <td style="width: 47.5pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>n &gt; 0</span></strong></p>
            </td>
            <td style="width: 94pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i &lt;= 2 * n</span></strong></p>
            </td>
            <td style="width: 63.5pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>Producto</span></strong></p>
            </td>
            <td style="width: 106.25pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>producto *= i</span></strong></p>
            </td>
            <td style="width: 70.85pt;border-top: none;border-left: none;border-bottom: 1.5pt solid rgb(255, 217, 102);border-right: 1pt solid windowtext;background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i += 2</span></strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 23.85pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>3</span></strong></p>
            </td>
            <td style="width: 19.05pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>2</span></p>
            </td>
            <td style="width: 47.5pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>3 &gt; 0 True</span></p>
            </td>
            <td style="width: 94pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>2 &lt;=2 * 3 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>4 &lt;=2 * 3 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>6 &lt;=2 * 3 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>12 &lt;=2 * 3 False</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
            <td style="width: 63.5pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>0</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>2</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>8</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>48</span></p>
            </td>
            <td style="width: 106.25pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>=2 (0 + 2)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>=8(2*4 (2 + 2))</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>=48(6 * 8(4 + 2))</span></p>
            </td>
            <td style="width: 70.85pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 4 (2+2)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 6 (2+4)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 12(6+6)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
        </tr>
    </tbody>
</table>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style='font-size:16px;line-height:107%;font-family:"Arial",sans-serif;'>DO WHILE</span></strong></p>
<table style="width:439.2pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 21.05pt;border-top: none;border-left: 1pt solid windowtext;border-bottom: 1.5pt solid rgb(255, 217, 102);border-right: none;background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>n</span></strong></p>
            </td>
            <td style="width: 21.25pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i</span></strong></p>
            </td>
            <td style="width: 42.5pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>n &gt; 0</span></strong></p>
            </td>
            <td style="width: 63.8pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>producto</span></strong></p>
            </td>
            <td style="width: 4cm;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>producto *= i</span></strong></p>
            </td>
            <td style="width: 3cm;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i += 2</span></strong></p>
            </td>
            <td style="width: 92.15pt;border-top: none;border-left: none;border-bottom: 1.5pt solid rgb(255, 217, 102);border-right: 1pt solid windowtext;background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i &lt;= 2 * n</span></strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 21.05pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>3</span></strong></p>
            </td>
            <td style="width: 21.25pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>2</span></p>
            </td>
            <td style="width: 42.5pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>3 &gt; 0 True</span></p>
            </td>
            <td style="width: 63.8pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>0</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>2</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>8</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>48</span></p>
            </td>
            <td style="width: 4cm;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>=2 (0 + 2)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>=8(2*4 (2 + 2))</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>=48(6 * 8(4 + 2))</span></p>
            </td>
            <td style="width: 3cm;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 4 (2+2)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 6 (2+4)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 12(6+6)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
            <td style="width: 92.15pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>2 &lt;=2 * 3 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>4 &lt;=2 * 3 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>6 &lt;=2 * 3 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>12 &lt;=2 * 3 False</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
        </tr>
    </tbody>
</table>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style='font-size:16px;line-height:107%;font-family:"Arial",sans-serif;'>FOR</span></strong></p>
<table style="width:433.45pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 24.65pt;border-top: none;border-left: 1pt solid windowtext;border-bottom: 1.5pt solid rgb(255, 217, 102);border-right: none;background: white;padding: 0cm 5.4pt;height: 13.45pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>n</span></strong></p>
            </td>
            <td style="width: 69pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;height: 13.45pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>n &gt; 0</span></strong></p>
            </td>
            <td style="width: 191.4pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;height: 13.45pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 2; i &lt;= 2 * n; i += 2</span></strong></p>
            </td>
            <td style="width: 42.15pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;height: 13.45pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>producto</span></strong></p>
            </td>
            <td style="width: 106.25pt;border-top: none;border-left: none;border-bottom: 1.5pt solid rgb(255, 217, 102);border-right: 1pt solid windowtext;background: white;padding: 0cm 5.4pt;height: 13.45pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>producto *= i</span></strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 24.65pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(255, 242, 204);padding: 0cm 5.4pt;height: 78.8pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>3</span></strong></p>
            </td>
            <td style="width: 69pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;height: 78.8pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>3 &gt; 0 True</span></p>
            </td>
            <td style="width: 191.4pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;height: 78.8pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 2; 2 &lt;=2 * 3; i = 4 (2+2) True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 4 &lt;=2 * 3; i = 6(2+4) True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 6 &lt;=2 * 3; i = 12 (6+6) True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 12 &lt;=2 * 3 False</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
            <td style="width: 42.15pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;height: 78.8pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>0</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>2</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>8</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>48</span></p>
            </td>
            <td style="width: 106.25pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;height: 78.8pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>=2 (0 + 2)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>=6 (2 + 4)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>=12 (6 + 6)</span></p>
            </td>
        </tr>
    </tbody>
</table>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'><span style='font-size:16px;line-height:107%;font-family:"Arial",sans-serif;'>&nbsp;</span></p>

## Ejecución
<p align="center">
  <img src="Imagenes/3.png"  width="600" height="500">
</p>