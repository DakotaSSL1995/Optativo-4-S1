{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Mercado libre.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMUOMGDLK/4Z8Cv1OpbvHDp",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DakotaSSL1995/Optativo-4-S1/blob/main/Mercado_libre.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 37,
      "metadata": {
        "id": "xYk5dmlUsDNl",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8850f0f6-0d1c-45c4-d667-637898a13aec"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: selenium in /usr/local/lib/python3.7/dist-packages (4.1.3)\n",
            "Requirement already satisfied: urllib3[secure,socks]~=1.26 in /usr/local/lib/python3.7/dist-packages (from selenium) (1.26.9)\n",
            "Requirement already satisfied: trio~=0.17 in /usr/local/lib/python3.7/dist-packages (from selenium) (0.20.0)\n",
            "Requirement already satisfied: trio-websocket~=0.9 in /usr/local/lib/python3.7/dist-packages (from selenium) (0.9.2)\n",
            "Requirement already satisfied: outcome in /usr/local/lib/python3.7/dist-packages (from trio~=0.17->selenium) (1.1.0)\n",
            "Requirement already satisfied: sortedcontainers in /usr/local/lib/python3.7/dist-packages (from trio~=0.17->selenium) (2.4.0)\n",
            "Requirement already satisfied: async-generator>=1.9 in /usr/local/lib/python3.7/dist-packages (from trio~=0.17->selenium) (1.10)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.7/dist-packages (from trio~=0.17->selenium) (2.10)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.7/dist-packages (from trio~=0.17->selenium) (1.2.0)\n",
            "Requirement already satisfied: attrs>=19.2.0 in /usr/local/lib/python3.7/dist-packages (from trio~=0.17->selenium) (21.4.0)\n",
            "Requirement already satisfied: wsproto>=0.14 in /usr/local/lib/python3.7/dist-packages (from trio-websocket~=0.9->selenium) (1.1.0)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.7/dist-packages (from urllib3[secure,socks]~=1.26->selenium) (2021.10.8)\n",
            "Requirement already satisfied: pyOpenSSL>=0.14 in /usr/local/lib/python3.7/dist-packages (from urllib3[secure,socks]~=1.26->selenium) (22.0.0)\n",
            "Requirement already satisfied: cryptography>=1.3.4 in /usr/local/lib/python3.7/dist-packages (from urllib3[secure,socks]~=1.26->selenium) (37.0.1)\n",
            "Requirement already satisfied: PySocks!=1.5.7,<2.0,>=1.5.6 in /usr/local/lib/python3.7/dist-packages (from urllib3[secure,socks]~=1.26->selenium) (1.7.1)\n",
            "Requirement already satisfied: cffi>=1.12 in /usr/local/lib/python3.7/dist-packages (from cryptography>=1.3.4->urllib3[secure,socks]~=1.26->selenium) (1.15.0)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.7/dist-packages (from cffi>=1.12->cryptography>=1.3.4->urllib3[secure,socks]~=1.26->selenium) (2.21)\n",
            "Requirement already satisfied: h11<1,>=0.9.0 in /usr/local/lib/python3.7/dist-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.13.0)\n",
            "Requirement already satisfied: typing-extensions in /usr/local/lib/python3.7/dist-packages (from h11<1,>=0.9.0->wsproto>=0.14->trio-websocket~=0.9->selenium) (4.2.0)\n",
            "Get:1 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]\n",
            "Hit:2 http://archive.ubuntu.com/ubuntu bionic InRelease\n",
            "Get:3 http://archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]\n",
            "Hit:4 https://cloud.r-project.org/bin/linux/ubuntu bionic-cran40/ InRelease\n",
            "Hit:5 http://ppa.launchpad.net/c2d4u.team/c2d4u4.0+/ubuntu bionic InRelease\n",
            "Get:6 http://archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]\n",
            "Hit:7 http://ppa.launchpad.net/cran/libgit2/ubuntu bionic InRelease\n",
            "Hit:8 http://ppa.launchpad.net/deadsnakes/ppa/ubuntu bionic InRelease\n",
            "Hit:9 http://ppa.launchpad.net/graphics-drivers/ppa/ubuntu bionic InRelease\n",
            "Ign:10 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  InRelease\n",
            "Ign:11 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  InRelease\n",
            "Hit:12 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  Release\n",
            "Hit:13 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  Release\n",
            "Get:14 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages [3,167 kB]\n",
            "Fetched 3,419 kB in 6s (621 kB/s)\n",
            "Reading package lists... Done\n",
            "Reading package lists... Done\n",
            "Building dependency tree       \n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (100.0.4896.127-0ubuntu0.18.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 48 not upgraded.\n",
            "Requirement already satisfied: bs4 in /usr/local/lib/python3.7/dist-packages (0.0.1)\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.7/dist-packages (from bs4) (4.6.3)\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.7/dist-packages (4.6.3)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.7/dist-packages (1.3.5)\n",
            "Requirement already satisfied: python-dateutil>=2.7.3 in /usr/local/lib/python3.7/dist-packages (from pandas) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.7/dist-packages (from pandas) (2022.1)\n",
            "Requirement already satisfied: numpy>=1.17.3 in /usr/local/lib/python3.7/dist-packages (from pandas) (1.21.6)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil>=2.7.3->pandas) (1.15.0)\n"
          ]
        }
      ],
      "source": [
        "#Instalacion de requisitos\n",
        "!pip install selenium\n",
        "!apt-get update # to update ubuntu to correctly run apt install\n",
        "!apt install chromium-chromedriver\n",
        "!pip install bs4\n",
        "!pip install beautifulsoup4\n",
        "!pip install pandas\n",
        "\n",
        "#Importando librerias\n",
        "import sys\n",
        "from selenium import webdriver\n",
        "import math\n",
        "from bs4 import BeautifulSoup\n",
        "import pandas as pd\n",
        "\n",
        "#Configuraciones iniciales\n",
        "sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')\n",
        "options = webdriver.ChromeOptions()\n",
        "options.add_argument('--headless')\n",
        "options.add_argument('--no-sandbox')\n",
        "options.add_argument('--disable-dev-shm-usage')\n",
        "wd = webdriver.Chrome('chromedriver',options=options)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Pagina principal\n",
        "wd.get(\"https://listado.mercadolibre.cl/inmuebles/casas/\")\n",
        " #Se obtiene el Html\n",
        "html_code = wd.page_source\n",
        "#Se crea un objeto apartir del html\n",
        "soup = BeautifulSoup(html_code, 'lxml')\n",
        "\n",
        "#Parceo de la direccion\n",
        "def get_address(ubicacion):\n",
        "  part = ubicacion.split(\",\")\n",
        "  partAmount = len(part)\n",
        "  if(partAmount == 3):\n",
        "    return {'direccion' : part[0], 'ciudad' : part[1], 'region' : part[2]}\n",
        "  elif(partAmount > 3): \n",
        "    return {'direccion' : \" \".join(part[:len(part)-3]), 'cuidad' : part[partAmount-2], 'region' : part[partAmount-1]}\n",
        "  elif(partAmount < 3): \n",
        "    for i in range(0,100):\n",
        "      print(\"Error:\")\n",
        "      print(ubicacion)\n",
        "    return {'direccion' : 'Fallo', 'ciudad' : 'Fallo', 'region' : ubicacion}\n",
        "\n",
        "#Obtiene los detalles individuales\n",
        "def casa_li_html_to_obj(casa_li_html): \n",
        "  #Obtiene la url de la Imagen \n",
        "  img = casa_li_html.find(\"img\")\n",
        "  try: \n",
        "    img_url = img['data-src']\n",
        "  except:\n",
        "    img_url = img['src']\n",
        "\n",
        "  #Obtiene el precio\n",
        "  precio = casa_li_html.find(class_=\"price-tag-fraction\").text.replace(\".\",\"\")\n",
        "  #Obtiene el titulo de la publicacion\n",
        "  titulo = casa_li_html.find(class_=\"ui-search-item__title\").text\n",
        "  #Obtiene la Ubicacion\n",
        "  ubicacion = casa_li_html.find(class_=\"ui-search-item__location\").text\n",
        "  ubicacion = get_address(ubicacion)\n",
        "  #Obtiene tamaño y/o cantidad de habitaciones\n",
        "  atributos = casa_li_html.find_all(class_=\"ui-search-card-attributes__attribute\")\n",
        "  tamanio = \"\"\n",
        "  cuartos =  \"\"\n",
        "  if(len(atributos) > 0): \n",
        "    if (\"útiles\" in atributos[0].text):\n",
        "      tamanio = atributos[0].text\n",
        "    else:\n",
        "      cuartos = atributos[0].text\n",
        "  if(len(atributos) > 1):\n",
        "    cuartos = atributos[1].text\n",
        "  #Obtiene el Url de la publicacion\n",
        "  url = casa_li_html.find(\"a\")[\"href\"]\n",
        "  #Devuelve el objeto\n",
        "  return {\"img_url\" : img_url, \"precio\" : precio, \"titulo\" : titulo, \"direccion\" : ubicacion['direccion'], \"ciudad\" : ubicacion['ciudad'], \"region\" : ubicacion['region'], \"tamañio\" : tamanio, \"cuartos\" : cuartos, \"url\" : url}\n",
        "\n",
        "#Funcion que obtiene la pagina\n",
        "def get_page_url(PN):\n",
        "  #Mercado libre tiene sistema de paginacion basado en la cantidad de productos en pagina\n",
        "  #Estos se limitan a 48 productos, el valor PN que se entrega es dado por el for que \n",
        "  #Pasea en las paginas\n",
        "  inicial_rango = 1 + 48 * (PN - 1)\n",
        "  #Url Base\n",
        "  base_pa_url = \"https://listado.mercadolibre.cl/inmuebles/casas/\"\n",
        "  #El valor difencial de la url es sustituido por el paramento inical_rango\n",
        "  base_pa_url = base_pa_url + \"_Desde_{}_NoIndex_True\".format(inicial_rango)\n",
        "  return base_pa_url\n",
        "\n",
        "def parse_y_guardar(url_pag):\n",
        "  #Me da el url que quiero\n",
        "  wd.get(url_pag)\n",
        "  #Se obtiene el Html\n",
        "  html_code = wd.page_source\n",
        "  #Se crea un objeto apartir del html\n",
        "  soup = BeautifulSoup(html_code, 'lxml')\n",
        "  #Obtiene todos los resultados de la pagina actual\n",
        "  casas_li = soup.find_all(\"li\", class_=\"ui-search-layout__item\")\n",
        "  #Los convierte en objetos y las guarda\n",
        "  for casa_li_html in casas_li:\n",
        "    casa_obj = casa_li_html_to_obj(casa_li_html)\n",
        "    df = pd.DataFrame({\"casa_obj\" :  casa_obj})\n",
        "    df.to_csv('casas.csv')\n",
        "\n",
        "#Contador de resultados \n",
        "cantidad_c = soup.findAll('span', {'class_' : \"ui-search-search_result__quantity-results\"}).text.split(\" \")[0].replace(\".\",\"\")\n",
        "#Contador de paginas\n",
        "NumeroP = math.ceil(cantidad_c/48)\n",
        "#Parseador de paginas\n",
        "for actual_pag in range(1, NumeroP+1):\n",
        "  url_pag = get_page_url(actual_pag)\n",
        "  parse_y_guardar(url_pag)\n",
        "\n",
        "\n",
        "\n",
        "  "
      ],
      "metadata": {
        "id": "fwRjJqC22s9m",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 373
        },
        "outputId": "9dedfd60-6843-47a6-cf0b-a8c11a228328"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "error",
          "ename": "AttributeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-41-6cf2e0b6c951>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     80\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     81\u001b[0m \u001b[0;31m#Contador de resultados\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 82\u001b[0;31m \u001b[0mcantidad_c\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msoup\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfindAll\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'span'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m'class_'\u001b[0m \u001b[0;34m:\u001b[0m \u001b[0;34m\"ui-search-search_result__quantity-results\"\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\" \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreplace\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\".\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     83\u001b[0m \u001b[0;31m#Contador de paginas\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     84\u001b[0m \u001b[0mNumeroP\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mceil\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcantidad_c\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0;36m48\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/bs4/element.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   1882\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__getattr__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1883\u001b[0m         raise AttributeError(\n\u001b[0;32m-> 1884\u001b[0;31m             \u001b[0;34m\"ResultSet object has no attribute '%s'. You're probably treating a list of items like a single item. Did you call find_all() when you meant to call find()?\"\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1885\u001b[0m         )\n",
            "\u001b[0;31mAttributeError\u001b[0m: ResultSet object has no attribute 'text'. You're probably treating a list of items like a single item. Did you call find_all() when you meant to call find()?"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "  "
      ],
      "metadata": {
        "id": "K8x3X8Od4eA8"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}