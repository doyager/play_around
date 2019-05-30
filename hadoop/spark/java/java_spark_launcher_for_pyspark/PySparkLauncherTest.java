package com.company.test.pysparktest;

import org.apache.spark.launcher.SparkAppHandle;
import org.apache.spark.launcher.SparkLauncher;

public class PySparkLauncherTest {

	public static void main(String[] args) {

		System.out.println("********************Inside PySparkLauncherTest ");
		System.out.println("********************args length " + String.valueOf(args.length));
		System.out.println("********************args  " + args);

		String appName = "ci_pyspark_test";
		String sparkHome = "/opt/cloudera/parcels/SPARK2-2.3.0.cloudera4-1.cdh5.13.3.p0.611179/lib/spark2";
		String pythonScript = "/home/mac/test_area/pyspark_read_hive_table.py";
		String sparkMaster = "yarn";
		String sparkExecutorCores = "4";
		String sparkExecutorMemory = "5G";
		String sparkDriverMemory = "5G";
		String yarnQueue = "dev_yarn";

		if (args.length == 2) {

			System.out.println("********************Inside if ");
			pythonScript = args[1];
			System.out.println("********************pythonScript :  " + pythonScript);

		}

		try {


			Process spark = new SparkLauncher().setAppName(appName).setSparkHome(sparkHome).setAppResource(pythonScript)
					// .setMainClass(sparkMainClass)
					.setMaster(sparkMaster).setConf("spark.dynamicAllocation.enabled", "true")
					.setConf("spark.sql.broadcastTimeout", "1200")
					.setConf("spark.sql.hive.caseSensitiveInferenceMode", "NEVER_INFER")
					.setConf("spark.streaming.stopGracefullyOnShutdown", "true").setConf("spark.task.maxFailures", "2")
					.setConf("spark.kryoserializer.buffer", "1024").setConf("spark.kryoserializer.buffer.max", "2047")
					.setConf("spark.yarn.maxAppAttempts", "1").setConf("spark.schedular.mode", "FAIR")
					.setConf("spark.locality.wait", "1m").setConf(SparkLauncher.EXECUTOR_CORES, sparkExecutorCores)
					.setConf(SparkLauncher.EXECUTOR_MEMORY, sparkExecutorMemory)
					.setConf(SparkLauncher.DRIVER_MEMORY, sparkDriverMemory)
					// .setConf("spark.yarn.queue", yarnQueue)
					// .addAppArgs(appName)
					// .addPyFile(pythonScript)
					.launch();

			InputStreamReaderRunnable inputStreamReaderRunnable = new InputStreamReaderRunnable(spark.getInputStream(),
					"input");
			Thread inputThread = new Thread(inputStreamReaderRunnable, "LogStreamReader input");
			inputThread.start();

			InputStreamReaderRunnable errorStreamReaderRunnable = new InputStreamReaderRunnable(spark.getErrorStream(),
					"error");
			Thread errorThread = new Thread(errorStreamReaderRunnable, "LogStreamReader error");
			errorThread.start();

			System.out.println("Waiting for finish...");
			int exitCode = spark.waitFor();
			System.out.println("Finished! Exit code:" + exitCode);
			System.out.println("********************Exiting PySparkLauncherTest ");

		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
