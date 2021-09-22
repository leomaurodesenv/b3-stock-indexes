# B3 Stock Indexes

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents (ToC)</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#running">Running</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The B3 S.A. - Brasil, Bolsa, Balcão (in English, B3 - Brazil Stock Exchange and Over-the-Counter Market), formerly BM&FBOVESPA, is a stock exchange located in São Paulo, Brazil, and the second oldest of the country ([Wikipedia](https://en.wikipedia.org/wiki/B3_(stock_exchange))). B3 hold the stock indexes, movements (sales and purchases) of the stock market in Brazil.

This project scraping stock indexes and their business segments from B3' [Market data and indices](http://www.b3.com.br/en_us/market-data-and-indices/). Basically, it is processed the CSV files and generate one single output file, i.e., [stock-indexes.csv](output/stock-indexes.csv).

-----
<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

[venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) allow you to manage separate package installations for different projects. They essentially allow you to create a 'virtual' isolated Python installation and install packages into that virtual installation (Python).

- Create a Python environment
    ```shell
    $ python -m venv .venv
    $ source .venv/bin/activate
    ```

- Install the dependencies
    ```shell
    $ pip install -r requirements.txt
    ```

### Running

- Runing the scraping
    ```shell
    $ python main.py
    ```

<!-- USAGE EXAMPLES -->
## Usage

Stock market data can be interesting to analyze and develop predictive models that generate financial returns. This scraping generates a dataset containing Brazilian stock market indexes information, such as stock code, company name, business segment, etc. You can combine this dataset with historical data (e.g., [ibovespa-stocks](https://www.kaggle.com/felsal/ibovespa-stocks)) to create more robust analysis and models.

<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

-----
<!-- CONTACT -->
## Contact

- Created by Leonardo Mauro ~ [leomaurodesenv](https://github.com/leomaurodesenv/)
