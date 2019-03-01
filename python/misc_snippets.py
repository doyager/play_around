
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


# create and assign age group bins 



                # create ages dataframe with dummuy values 
                df_ages = pd.DataFrame({'age': np.random.randint(20, 100, 40)})
                df_ages.head()
                age
                0	37
                1	37
                2	84
                3	99
                4	93

                #create age bins 
                age_ranges = ["{0} - {1}".format(age, age + 9) for age in range(20, 100, 10)]
                age_ranges
                ['20 - 29',
                 '30 - 39',
                 '40 - 49',
                 '50 - 59',
                 '60 - 69',
                 '70 - 79',
                 '80 - 89',
                 '90 - 99']

                #  count of items in the age_ranges lis
                count_unique_age_ranges = len(age_ranges)
                count_unique_age_ranges
                8

                df_ages['age_range'] = pd.cut(x=df_ages['age'], bins=count_unique_age_ranges, labels=age_ranges)

                df_ages.head()
                age	age_range
                0	37	30 - 39
                1	37	30 - 39
                2	84	80 - 89
                3	99	90 - 99
                4	93	90 - 99

                age_by_decade = ["{0}s".format(age) for age in range(20, 100, 10)]
                age_by_decade
                ['20s', '30s', '40s', '50s', '60s', '70s', '80s', '90s']
                #Create a variable count_unique_age_decades that's the count of items in the age_by_decade list above.

                count_unique_age_decades = len(age_by_decade)
                count_unique_age_decades
                8

                df_ages['age_by_decade'] = pd.cut(x=df_ages['age'], bins=count_unique_age_decades, labels=age_by_decade)
                Preview the first 5 rows of df_ages.

                df_ages.head()
                age	age_range	age_by_decade
                0	37	30 - 39	30s
                1	37	30 - 39	30s
                2	84	80 - 89	80s
                3	99	90 - 99	90s
                4	93	90 - 99	90s

# calculate tenure in years, tenure period , multiple columns udf 
               
        from datetime import datetime
        from datetime import 
        from dateutil.relativedelta import relativedelta

                def member_tenure(row):
                    #born = datetime.strptime(born, "YYYY-MM-DD HH:MM:SS.s").date()
                    start_dt = datetime.strptime(row['mbr_enrlmnt_dt'], "%Y-%m-%d %H:%M:%S.%f").date()
                    end_dt = datetime.strptime( row['mbr_term_dt'], "%Y-%m-%d %H:%M:%S.%f").date()
                    today = date.today()
                    from dateutil.relativedelta import relativedelta
                    #difference_in_years = relativedelta(end_date, start_date).years
                    if end_dt < today :
                        return relativedelta(end_dt, start_dt).years #end_dt - start_dt
                    else:
                        return relativedelta(today, start_dt).years
                        #today.year - start_dt.year - ((today.month, today.day) < (start_dt.month, start_dt.day))

                input_1M['member_tenure'] = input_1M.apply(member_tenure , axis=1)

                input_1M[['mbr_term_dt', 'mbr_enrlmnt_dt','member_tenure']].tail(4)

                                  mbr_term_dt         mbr_enrlmnt_dt  member_tenure
                999997  2088-12-31 00:00:00.0  2018-01-01 00:00:00.0              1
                999998  2018-10-31 00:00:00.0  2017-11-01 00:00:00.0              0
                999999  2080-12-31 00:00:00.0  2018-01-01 00:00:00.0              1
                999996  2018-09-30 00:00:00.0  2017-10-01 00:00:00.0              0

                                                
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
