class Solution {
public:
    int reverseDegree(string s) {
        int i,len,sum=0,n;
        len=s.length();
        for(i=0; i<len; i++){
            n=122-(static_cast<int>(s[i]))+1;

            sum+=(n*(i+1));

            
        }
        return sum;
        
    }
};