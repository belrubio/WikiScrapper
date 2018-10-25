{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['ACTON', 'ANTHONY', 'SEAN', 'M', 'B', '26', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['AKERS', 'SYDNEY', 'RAE', 'F', 'W', '21', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['AL-AQUIL', 'MOHAMMED', 'NASSER', 'M', 'U', '27', 'ST. LOUIS', 'MO', '\\n\\xa0Details\\n'], ['ALLEN', 'JEREMY', 'ADRIAN', 'M', 'W', '40', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['ARMSTRONG', 'ANTIONE', 'LAMONT', 'M', 'B', '18', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['ASHFORD', 'NEELEY', 'DIANA', 'F', 'W', '41', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['AULL', 'JONATHAN', 'MORGAN', 'M', 'W', '37', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BAKER', 'CHAD', 'EDWARD', 'M', 'W', '30', 'THOMPSON', 'MO', '\\n\\xa0Details\\n'], ['BAKER', 'MEGUN', 'ANN', 'F', 'W', '31', 'PRAIRIE HOME', 'MO', '\\n\\xa0Details\\n'], ['BANKS', 'HAROLD', 'JOSEPH', 'M', 'B', '17', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BARNES', 'BRENDA', 'SUE', 'F', 'W', '40', 'ST. LOUIS', 'MO', '\\n\\xa0Details\\n'], ['BARNETTE-KRUGER', 'ANDREW', 'LAWRANCE', 'M', 'B', '25', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BARNEY', 'FELSON', 'DEVONE', 'M', 'B', '41', 'SPRINGFIELD', 'MO', '\\n\\xa0Details\\n'], ['BARNEY', 'FREDERICK', ' ', 'M', 'B', '34', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BARNEY', 'LARCELL', 'CHRISTOPHER', 'M', 'B', '44', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BARTON', 'KRISTE', 'MARIE', 'F', 'W', '33', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BENEDETTI', 'FRANK', 'DOMINICK', 'M', 'W', '29', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BLACK', 'ISAIAH', 'JAYSON', 'M', 'W', '21', 'STURGEON', 'MO', '\\n\\xa0Details\\n'], ['BLEVINS', 'JESSE', 'RAY', 'M', 'W', '29', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BLUMHORST', 'DWIGHT', 'THOMAS', 'M', 'W', '34', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BOWDEN', 'BRANDON', 'LEE', 'M', 'W', '32', 'ASHLAND', 'MO', '\\n\\xa0Details\\n'], ['BOYD', 'LEE', 'DEMAREO', 'M', 'B', '32', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BRAWLEY', 'DONALD', 'GLEN', 'M', 'W', '42', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BROWN', 'BARRY', 'RONELL', 'M', 'B', '31', 'FLORISSANT', 'MO', '\\n\\xa0Details\\n'], ['BUCHANAN', 'DYDREONTE', 'JONELL', 'M', 'B', '19', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BUCKNER', 'KEVIN', 'MAURICE', 'M', 'B', '19', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BUFFER', 'DOUGLAS', 'PRESTON', 'M', 'W', '37', 'IMPERIAL', 'MO', '\\n\\xa0Details\\n'], ['BUSH', 'CARL', 'PATRICK', 'M', 'W', '59', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BUSH', 'FRANK', 'LADON', 'M', 'B', '40', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BUSH', 'TRAVIS', 'ALLEN', 'M', 'B', '49', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['BUTLER', 'JEMELL', 'DUPRUE', 'M', 'B', '22', 'JEFFERSON CITY', 'MO', '\\n\\xa0Details\\n'], ['CAMPBELL', 'AUSTIN', 'JOSEPH', 'M', 'W', '21', 'SPRINGFIELD', 'MO', '\\n\\xa0Details\\n'], ['CARLSON', 'JACOBI', 'DANIEL', 'M', 'W', '31', 'MEXICO', 'MO', '\\n\\xa0Details\\n'], ['CARTER', 'DARIAN', 'MAURICE', 'M', 'B', '25', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['CAUDLE', 'LINDA', 'JOYCE', 'F', 'W', '56', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['CHEATOM', 'DARIEN', 'CAPRI', 'M', 'B', '25', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['COBBINS', 'TIMIS', 'BERNARD', 'M', 'B', '52', 'JEFFERSON CITY', 'MO', '\\n\\xa0Details\\n'], ['COLEMAN', 'BILLY', 'JOE', 'M', 'W', '32', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['COLLINS', 'RENEE', 'MICHELLE', 'F', 'W', '49', 'ROCHEPORT', 'MO', '\\n\\xa0Details\\n'], ['COMMANDER', 'JAVANTE', 'BRUCE', 'M', 'B', '23', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['CRONIN', 'JOHN', 'MICHAEL', 'M', 'W', '27', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['CROOM', 'ROBERT', 'LEE', 'M', 'B', '30', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['CURETON', 'ERIC', 'WAYNE', 'M', 'B', '51', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['DAVID', 'JACK', 'ALLEN', 'M', 'W', '25', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['DAVIDSON', 'SARAH', 'MARIE', 'F', 'W', '29', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['DAVIS', 'RAQUEL', 'ELIZABETH', 'F', 'W', '29', 'HALLSVILLE', 'MO', '\\n\\xa0Details\\n'], ['DAVIS', 'RONNELL', ' ', 'M', 'B', '21', 'KANSAS CITY', 'MO', '\\n\\xa0Details\\n'], ['DAVIS', 'SCOTT', 'HARRY', 'M', 'W', '47', 'KANSAS CITY', 'MO', '\\n\\xa0Details\\n'], ['DEVINE', 'STEVEN', 'PATRICK', 'M', 'W', '42', 'COLUMBIA', 'MO', '\\n\\xa0Details\\n'], ['DEY', 'DAVID', 'EARL', 'M', 'W', '33', 'MOBERLY', 'MO', '\\n\\xa0Details\\n'], []]\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'\n",
    "response = requests.get(url)\n",
    "html = response.content\n",
    "\n",
    "soup = BeautifulSoup(html)\n",
    "table = soup.find('tbody', attrs={'class': 'stripe'})\n",
    "#  print(table.prettify())\n",
    "list_of_rows = []\n",
    "for row in table.findAll('tr'):\n",
    "    list_of_cells = []\n",
    "    for cell in row.findAll('td'):\n",
    "        text = cell.text.replace('&nbsp;', '')\n",
    "        list_of_cells.append(text)\n",
    "    list_of_rows.append(list_of_cells)\n",
    "    \n",
    "print(list_of_rows)\n",
    "outfile = open(\"./inmates.csv\", newline='') as csvfile:\n",
    "writer = csv.writer(outfile)\n",
    "writer.writerows(list_of_rows)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
