class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s1.length() > s2.length()){
            return false;
        }
        int[] array1 = new int[26];
        for(int i = 0; i < s1.length();i++){
            array1[s1.charAt(i) - 'a']++;
        }
        for(int i = 0; i < s2.length()-s1.length()+1;i++){
            int[] array2 = new int[26];
            for(int j = 0; j < s1.length();j++){
                array2[s2.charAt(i+j) - 'a']++;
            }
            if(matches(array1, array2))
                return true;
        }
        return false;
        
    }
    public boolean matches(int[] a1, int[] a2){
        for(int i = 0; i < 26; i++){
            if(a1[i] != a2[i])
                return false;
        }
        return true;
    }
}