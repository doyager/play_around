
#####################################
# .            UDF
#####################################


# calculate age from str date , age udf 
        from datetime import datetime
        from datetime import date

        #YYYY-MM-DDTHH:MM:SS+HH:MM
        # "%Y-%m-%d"
        # input : 1978-02-13 00:00:00.0     output : 41
        def calculate_age(born):
            #born = datetime.strptime(born, "YYYY-MM-DD HH:MM:SS.s").date()
            born = datetime.strptime(born, "%Y-%m-%d %H:%M:%S.%f").date()
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        input_1M['age'] = input_1M['member_birth_date'].apply(calculate_age)
        
        input_1M[['member_birth_date','age']].head(5)
        
        """"
         o/p:
         
        0       1978-02-13 00:00:00.0   41
        1       1978-02-13 00:00:00.0   41
        2       1957-01-24 00:00:00.0   62
        3       1969-04-13 00:00:00.0   49
        4       1992-03-13 00:00:00.0   26
        """


#####################################
# .            ERRORS
#####################################
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
