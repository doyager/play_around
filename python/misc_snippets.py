


#installation error , install

        #ssl error
        """
        Could not fetch URL https://pypi.org/simple/kmodes/: There was a problem confirming the ssl certificate: 
        HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/kmodes/
        (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'ssl3_get_server_certificate', 'certificate verify failed')],)",),)) - skipping
          Could not find a version that satisfies the requirement kmodes (from versions: )
        No matching distribution found for kmodes

        """
        pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org kmodes
