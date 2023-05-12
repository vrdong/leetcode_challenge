import os
import requests
from requests.auth import HTTPBasicAuth


def download_pdf_file(url: str) -> bool:
    """Download PDF from given URL to local directory.

    :param url: The url of the PDF file to be downloaded
    :return: True if PDF file was successfully downloaded, otherwise False.
    """

    # Request URL and get response object
    basic = HTTPBasicAuth('OMNI', 'uC#3%6UOc0q%C$mBMilN6GB72Lr30$DV')
    response = requests.get(url, stream=True, auth=basic)

    # isolate PDF filename from URL
    pdf_file_name = os.path.basename(url)
    if response.status_code == 200:
        # Save in current working directory
        filepath = os.path.join(os.getcwd(), pdf_file_name)
        with open(filepath, 'wb') as pdf_object:
            pdf_object.write(response.content)
            print(f'{pdf_file_name} was successfully saved!')
            return True
    else:
        print(f'Uh oh! Could not download {pdf_file_name},')
        print(f'HTTP response status code: {response.status_code}')
        return False


if __name__ == '__main__':
    # URL from which pdfs to be downloaded
    URL = 'https://invoice-service.dgl-dev.tekoapis.net/invoice-service/service/download?orderId=230405120978260_SBN01&taxIdentify=OMNI_SELLER_SB'
    download_pdf_file(URL)