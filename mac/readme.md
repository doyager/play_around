

# cpu and memory command:

      system_profiler SPHardwareDataType | grep "  Memory:"
      system_profiler SPHardwareDataType | grep Cores:
      system_profiler SPHardwareDataType | grep Processors:

      #or, if you want to go low-level, use sysctl:

      sysctl hw.memsize
      sysctl hw.ncpu

      #btw, there are a bunch of other interesting things you can get from sysctl. Try:

      sysctl -a | grep cpu
