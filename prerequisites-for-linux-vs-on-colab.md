# Requisitos

Los siguientes requisitos son para poder ejecutar el código en una instancia de visual studio code en Google Colab. En el siguiente vídeo se explica como poder utilizar visual studio code en Google Colab. [Run VSCode on Google Colab using Colab Code](https://youtu.be/ah_7J0w1Wac).

De todas formas los comandos servirán para utilizar en una máquina con Ubuntu fuera de Google Colab pero hay que tener en cuenta la versión de **cudatoolkit** a utilizar. En el siguiente enlace se encuentra con mayor detalle los requisitos para las distintas versiones de Pytorch y cudatoolkit. [GET STARTED with Pytorch](https://pytorch.org/get-started/previous-versions/).

## Instalar anaconda

En el siguiente enlace se puede encontrar los pasos exactos a seguir para la instalación de anaconda en una máquina con linux. En el caso del tutorial lo hace en Ubuntu 20.04 pero esta comprobad que sirve también en otras versiones como lo serían la 18.04. [Cómo instalar la distribución Anaconda de Python en Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-20-04-es)

### Crear ambiente para ejecutar el modelo

En la consola de comandos, hay que ingresar lo siguiente para instalar las librerias necesarias que permitirán ejecutar el modelo. Si

```
conda create -n RepbySS python=3.7.4 opencv=3.4.2 tqdm=4.54.1 pytorch==1.4.0 torchvision==0.5.0 cudatoolkit=10.1 -c pytorch
```

Con el ambiente ya creado, hay que activarlo con el siguiente comando

```
conda activate RepbySS
```

Estando en el ambiente, hay que instalar librosa en su versión 0.8.0 con el siguiente comando.

```
conda install -c conda-forge librosa=0.8.0
```

Con todo lo anterior listo ya se podrá ejecutar el archivo **run_demo.py** sin problemas.

## Clonar el proyecto desde GitHub

Antes de clonar el proyecto desde GitHub, hay que ubicarse en el directorio donde se guardaran los archivos del repositorio, ya que cada vez que se inicie la instancia de Visual Studio Code hay que realizar todos estos pasos, no es muy importante el directorio, sin embargo, se recomienda hacerlo en el directorio de archivos temporales o en el directorio root donde se encuentra instalado Anaconda.

**Nota:** En el siguiente enlace se deja una página con varios comandos para el manejo de archivos y carpetas desde la consola de comando. [La Terminal de Linux (II). Comandos para Manejar Archivos y Carpetas](https://computernewage.com/2013/04/10/como-manejar-archivos-y-carpetas-desde-la-terminal-de-linux/#:~:text=El%20comando%20mkdir%20te%20permitir%C3%A1,en%20el%20que%20te%20encuentres.).

Para clonar el proyecto, hay que ingresar el siguiente comando.

```
git clone https://github.com/crisfreak036/RepASightSound.git RepbySS
```

Con el repositorio clonado, hay que ubicarse dentro del directorio y en él descargar los archivos _sr_checkpoint.pt_ y _visual_checkpoint.pt_ con los siguientes comandos.

Descargar **sr_checkpoint.pt**
```
wget --no-check-certificate 'https://drive.google.com/file/d/1wZYWFV-o7ElRn0wy0EAbQFSGqeIAx_Ma/view?usp=sharing' -O sr_checkpoint.pt
```

Descargar **visual_checkpoint.pt**
```
wget --no-check-certificate 'https://drive.google.com/file/d/1G2uCYnRKm1fSNunBH9_fQXNv70RvwaXR/view?usp=sharing' -O visual_checkpoint.pt
```

## Ejecutar el demo

Finalmente con todos los archivos descargados, procurando estar en el ambiente creado y posicionados en el directorio del proyecto en la consola de comandos, se debe utilizar el siguiente comando para ejecutar el demo que trae el proyecto.

```
python run_demo.py
```

La salida esperada es la siguiente.
```
Conteo por sonido:  4.546907424926758
Conteo por vista:  12.449081897735596
0.49737322330474854
Conteo final:  8.0
0.0 1
```