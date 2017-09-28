int betaExor(String s) {
    int res = 0;
    
    for (int i = 0; i < s.length(); i++) {
        res ^= (int)s.charAt(i);
    }
    
    return res;
}