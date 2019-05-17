


################################
#spark-shell-open-command:

  spark2-shell --master yarn --deploy-mode client --driver-cores 4 --driver-memory 4G --jars spark-cobol-0.4.2.jar,scodec-core_2.11-1.10.3.jar,scodec-bits_2.11-1.1.4.jar,cobol-parser-0.4.2.jar


#spark-code:
        #place scheam file in hdfs
        #place dat [ Data file ] in hdfs

  val df = spark.read.format("cobol").option("copybook", "test3_copybook.cob").load("TRAN2.AUG31.DATA.dat")
  df.show(false)


Output:

  +-------------------------------------------------------+                                   
  |TRANSDATA                                              |                               
  +-------------------------------------------------------+                                             
  |[GBP, S9276511, Delta Pivovar, 0021213441, 0, 988.91]  |                                          
  |[CAD, S9276511, Robotrd Inc., 0039801988, 1, 713.22]   |                                                      
  |[CAD, S9276511, ECSRONO, 0039567812, 0, 59.80]         |                                                        
  |[USD, S9276511, Xingzhoug, 8822278911, 0, 428.65]      |
  |[CHF, S9276511, Joan Q & Z, 0039887123, 1, 292.00]     |
  |[ZAR, S9276511, Joan Q & Z, 0039887123, 0, 873.44]     |
  |[CHF, S9276511, Test Bank, 0092317899, 1, 429.55]      |
  |[CYN, S9276511, Xingzhoug, 8822278911, 1, 602.85]      |
  |[ZAR, S9276511, Test Bank, 0092317899, 1, 536.19]      |
  |[ZAR, S9276511, Pear GMBH., 0002377771, 0, 352.45]     |
  |[ZAR, S9276511, Beierbauh., 0038903321, 1, 154.88]     |
  |[CZK, S9276511, Beierbauh., 0038903321, 0, 471.30]     |
  |[GBP, S9276511, Xingzhoug, 8822278911, 1, 763.92]      |
  |[ZAR, S9276511, Joan Q & Z, 0039887123, 0, 126.98]     |
  |[ZAR, S9276511, Eqartion Inc., 0039003991, 1, 60112.00]|
  |[USD, S9276511, ZjkLPj, 0034412331, 0, 190.53]         |
  |[CYN, S9276511, Xingzhoug, 8822278911, 1, 55.52]       |
  |[ZAR, S9276511, Beierbauh., 0038903321, 0, 857.62]     |
  |[ZAR, S9276511, Robotrd Inc., 0039801988, 1, 704.78]   |
  |[ZAR, S9276511, Test Bank, 0092317899, 0, 334.97]      |
  +-------------------------------------------------------+
  only showing top 20 rows
