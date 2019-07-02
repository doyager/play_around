


// Hash map Constant 

 public static final Map<String, String> AGENT_ARGS_SEPARATOR_MAP = initSeparatorMap();

  private static Map<String, String> initSeparatorMap() {
    Map<String, String> map = new HashMap<>();
    map.put("COMMA", ",");
    map.put("SPACE", " ");
    map.put("PIPE", "|");
    map.put("HYPHEN", "-");
    map.put("TAB", "\t");
    return Collections.unmodifiableMap(map);
  }
